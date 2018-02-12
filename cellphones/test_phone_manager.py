import unittest
from phone_manager import Phone, Employee, PhoneAssignments, PhoneError

class TestPhoneManager(unittest.TestCase):

    def test_create_and_add_new_phone(self):

        testPhone1 = Phone(1, 'Apple', 'iPhone 6')
        testPhone2 = Phone(2, 'Apple', 'iPhone 5')
        testPhone3 = Phone(3, 'Samsung', 'Galaxy S7')

        testPhones = [ testPhone1, testPhone2, testPhone3 ]

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_phone(testPhone3)

        # assertCountEqual checks if two lists have the same items, in any order.
        # (Despite what the name implies)
        self.assertCountEqual(testPhones, testAssignmentMgr.phones)


    def test_create_and_add_phone_with_duplicate_id(self):
        # add a phone, add another phone with the same id, and verify an PhoneError exception is thrown
        testPhone1 = Phone(1, 'Apple', 'iPhone 6')
        testPhone2 = Phone(1, 'Apple', 'iPhone 5')
        testPhone3 = Phone(1, 'Apple', 'iPhone 6')

        testAssignmentMgr = PhoneAssignments()

        with self.assertRaises(PhoneError):
            testAssignmentMgr.add_phone(testPhone2)
        with self.assertRaises(PhoneError):
            testAssignmentMgr.add_phone(testPhone3)


    def test_create_and_add_new_employee(self):
        # Add some employees and verify they are present in the PhoneAssignments.employees list
        testEmployee1 = Employee(1, "Mark Hamil")
        testEmployee2 = Employee(2, "Carrie Fisher")
        testEmployee3 = Employee(3, "Harrison Ford")
        testPhoneAssigmentsMgr = PhoneAssignments()
        testPhoneAssigmentsMgr.add_employee(testEmployee3)

        testEmployees = [ testEmployee1, testEmployee2 ]

        self.assertCountEqual(testEmployees, testPhoneAssigmentsMgr.employees)


    def test_create_and_add_employee_with_duplicate_id(self):
        # This method will be similar to test_create_and_add_phone_with_duplicate_id

        testPhoneAssigmentsMgr = PhoneAssignments()
        testEmployee3 = Employee(1, "Harrison Ford")
        testEmployee1 = Employee(1, "Mark Hamil")

        with self.assertRaises(PhoneError):
            testPhoneAssigmentsMgr.add_employee(testEmployee1)
        with self.assertRaises(PhoneError):
            testPhoneAssigmentsMgr.add_employee(testEmployee3)


    def test_assign_phone_to_employee(self):

        testPhone1 = Phone(1, 'Apple', 'iPhone 6')
        testEmployee1 = Employee(1, "Mark Hamil")
        testPhoneAssigmentsMgr = PhoneAssignments()
        testPhoneAssigmentsMgr.assign(testPhone1, testEmployee1)

        self.assertTrue(testPhone1.employee_id == testEmployee1.id)


    def test_assign_phone_that_has_already_been_assigned_to_employee(self):
        # If a phone is already assigned to an employee, it is an error to assign it to a different employee. A PhoneError should be raised.

        testPhone1 = Phone(1, 'Apple', 'iPhone 6')
        testEmployee1 = Employee(1, "Mark Hamil")
        testEmployee3 = Employee(3, "Harrison Ford")
        testPhoneAssigmentsMgr = PhoneAssignments()

        testPhoneAssigmentsMgr.assign(testPhone1, testEmployee1)

        with self.assertRaises(PhoneError):
            testPhoneAssigmentsMgr.assign(testPhone1,testEmployee3)


    def test_assign_phone_to_employee_who_already_has_a_phone(self):

        testEmployee1 = Employee(1, "Mark Hamil")
        testPhoneAssigmentsMgr = PhoneAssignments()
        testPhone2 = Phone(2, 'Apple', 'iPhone 5')
        testPhone1 = Phone(1, 'Apple', 'iPhone 6')
        testPhoneAssigmentsMgr.assign(testPhone1, testEmployee1)

        with self.assertRaises(PhoneError):
            testPhoneAssigmentsMgr.assign(testPhone2,testEmployee1)


    def test_assign_phone_to_the_employee_who_already_has_this_phone(self):
        # The method should not make any changes but NOT raise a PhoneError if a phone
        # is assigned to the same user it is currenly assigned to.

        testEmployee1 = Employee(1, "Mark Hamil")
        testPhone1 = Phone(1, 'Apple', 'iPhone 6')

        testPhoneAssigmentsMgr = PhoneAssignments()
        testPhoneAssigmentsMgr.assign(testPhone1, testEmployee1)
        self.assertTrue(testPhone1.employee_id == testEmployee1.id)


    def test_un_assign_phone(self):
        # Assign a phone, unasign the phone, verify the employee_id is None
        testPhone1 = Phone(1, 'Apple', 'iPhone 6')
        testEmployee1 = Employee(1, "Mark Hamil")
        testPhoneAssigmentsMgr = PhoneAssignments()
        testPhoneAssigmentsMgr.assign(testPhone1, testEmployee1)
        testPhoneAssigmentsMgr.un_assign(testPhone1)

        self.assertTrue(testPhone1.employee_id == None)


    def test_get_phone_info_for_employee(self):
        # Create some phones, and employees, assign a phone,
        # call phone_info and verify correct phone info is returned

        # check that the method returns None if the employee does not have a phone
        # check that the method raises an PhoneError if the employee does not exist
        testPhone1 = Phone(1, 'Apple', 'iPhone 6')
        testEmployee1 = Employee(1, "Mark Hamil")
        testEmployee2 = Employee(2, "Carrie Fisher")
        testPhoneAssigmentsMgr = PhoneAssignments()
        testPhoneAssigmentsMgr.assign(testPhone1, testEmployee1)

        self.assertTrue(testPhoneAssigmentsMgr.phone_info(testEmployee1)==testPhone1)

        self.assertIsNone(testPhoneAssigmentsMgr.phone_info(testEmployee2))

        with self.assertRaises(PhoneError):
            testPhoneAssigmentsMgr.phone_info(testEmployee3)

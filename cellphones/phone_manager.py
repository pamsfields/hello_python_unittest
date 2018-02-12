# Manage a list of phones
# And a list of employees

# Each employee gets 0 or 1 phones

class Phone():

    def __init__(self, id, make, model):
        self.id = id
        self.make = make
        self.model = model
        self.employee_id = None


    def assign(self, employee_id):
        self.employee_id = employee_id


    def is_assigned(self):
        return self.employee_id is not None


    def __str__(self):
        return 'ID: {} Make: {} Model: {} Assigned to Employee ID: {}'.format(self.id, self.make, self.model, self.employee_id)



class Employee():

    def __init__(self, id, name):
        self.id = id
        self.name = name


    def __str__(self):
        return 'ID: {} Name {}'.format(self.id, self.name)



class PhoneAssignments():

    def __init__(self):
        self.phones = []
        self.employees = []


    def add_employee(self, employee):
        #raise exception if two employees with same ID are added
        self.employees.append(employee)
        for em in self.employees:
            if em.id== employee.id:
                raise PhoneError('An employee with this ID has already been added.')
        if employee in self.employees:
            raise PhoneError("This employee is already been added.")
        else:
            self.employees.append(employee)


    def add_phone(self, phone):
        # TODO raise exception if two phones with same ID are added
        self.phones.append(phone)
        for p in self.phones:
            if p.id == phone.id:
                raise PhoneError("This phone's ID is already in use.")
            if phone in self.phones:
                print(phone, '\t:\t', self.phones)
                raise PhoneError('This phone has already been added.')
            else:
                self.phones.append(phone)


    def assign(self, phone_id, employee):
        # Find phone in phones list
        for phone in self.phones:
            if phone.id == phone_id:
                if (phone.is_assigned()==True):
                    if PhoneAssignments.phone_info(self,employee) is None: #if phone is already assigned to an employee, do not change list, raise exception
                        raise PhoneError('Someone else is assigned to this phone.')
                    elif (PhoneAssignments.phone_info(self, employee) is not None) & (PhoneAssignments.phone_info(self,employee).id) != phone_id):
                        raise PhoneError('This employee already has a phone.')
                        #if employee already has a phone, do not change list, and raise exception
                    else:
                        return
                        #if employee already has this phone, don't make any changes. This should NOT raise an exception.
                elif (PhoneAssignments.phone_info(self, employee) is not None) & (PhoneAssignments.phone_info(self, employee) != phone_id):
                    #this phone isn't assigned to someone else, but this employee already has a phone
                    raise PhoneError("This employee already has a phone assigned to them.")
                else:
                    phone.assign(employee.id) #This phone isn't assigned to anyone else, and the employee doesn't have a phone
                    return


    def un_assign(self, phone_id):
        # Find phone in list, set employee_id to None
        for phone in self.phones:
            if phone.id == phone_id:
                phone.assign(None)   # Assign to None


    def phone_info(self, employee):
        # find phone for employee in phones list
        # should return None if the employee does not have a phone
        #the method should raise an exception if the employee does not exist
        if employee not in self.employees:
            raise PhoneError('This employee has not added yet.')
        else:
            for phone in self.phones:
                if phone.employee_id == employee.id:
                    return phone
            return None #phone wasn't assigned to this employee, but the employee exists


        return None


class PhoneError(Exception):
    pass

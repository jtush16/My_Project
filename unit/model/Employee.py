class Employee:
    count = 1

    def __init__(self, name, age, email):
        self.id = Employee.count
        self.name = name
        self.set_age(age)
        self.set_email(email)
        Employee.count = Employee.count + 1

    def __str__(self):
        return f'''\nID : {self.id}, NAME : {self._name}, AGE : {self._age}, EMAIL : {self._email} '''

    def __repr__(self):
        return str(self)

    def get_age(self):
        return self._age

    def set_age(self, age):
        if age <= 20:
            print('Invalid Age')
        else:
            self._age = age

    age = property(fget=get_age, fset=set_age)

    def get_email(self):
        return self._email

    def set_email(self, email):
        if len(email) < 5:
            print('Invalid Email')
        else:
            self._email = email

    email = property(fget=get_email, fset=set_email)

    def get_name(self):
        return self.set_name

    def set_name(self, name):
        if len(name) < 2:
            print('Invalid name')
        else:
            self._name = name

    name = property(fget=get_name, fset=set_name)

    @classmethod
    def validations(cls, name, age, email):
        if len(name) < 2:
            print('Invalid Name of Employee')
        elif type(age) != int or age <= 20:
            print('Please Enter valid age')
        elif len(email) < 5:
            print('Invalid Email address')
        else:
            return cls(name, age, email)


# E1 = Employee.validations('aa', 27, 'jtuhjbjsdbf')
# E2 = Employee.validations('jgsdf', 27, 'adfgcf')
# E3 = Employee.validations('akad', 27, 'jtuhjbjsdbf')
# print([E1,E2,E3])
# E1.age = -20
# E2.name = 'a'
# E3.email = 'we'
# print([E1,E2,E3])
# # print(E2)


class EmployeeServices:
    employees_list = []

    def addemp(self, emp: Employee):
        if type(emp) == Employee:
            EmployeeServices.employees_list.append(emp)
            print('Employee successfully added')
        else:
            print('Invalid Employee')


employee_service = EmployeeServices()


def age_validation():
    while True:
        try:
            age = int(input('Enter your age : '))
            return age
        except:
            print('Please Enter valid Age')
            continue


def get_input():
    name = input('Enter your Name : ')
    age = age_validation()
    email = input('Enter your Email address : ')
    return Employee.validations(name, age, email)


def add_employee():
    flag = False
    while True:
        emp = get_input()
        employee_service.addemp(emp)
        for i in range(3):
            choice = input('Do you want to continue [y/n] : ')
            if choice.lower() in ['no', 'n']:
                flag = True
                break
            elif choice.lower() in ['yes', 'y']:
                break
            else:
                if i == 2:
                    flag = True
                    break
                else:
                    print('Invalid Choice')
                    continue
        if flag:
            return


def get_employee():
    employees = employee_service.employees_list
    print(employees)


add_employee()
get_employee()

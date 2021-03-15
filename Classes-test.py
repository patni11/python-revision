import datetime


class Employee:

    raise_amount = 1.4
    num_employees = 0

    def __init__(self, name, last_name, pay):
        self.name = name
        self.last_name = last_name
        self.pay = pay

        Employee.num_employees += 1

    @property
    def email(self):
        return f"{self.name}.{self.last_name}@gmail.com"

    @property
    def full_name(self):
        return f"{self.name} {self.last_name}"

    @full_name.setter
    def full_name(self, new_name):
        first, last = new_name.split(" ")
        self.name, self.last_name = first, last

    def pay_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_string):
        first_name, last_name, pay = emp_string.split('-')
        return cls(first_name, last_name, pay)

    @staticmethod
    def is_weekday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    def __len__(self):
        return len(self.name)

    def __add__(self, employee2):
        return f"we have a newly married couple ->  {self.name} and {employee2.name}"

    def __repr__(self):
        return "Employee({}, {}, {})".format(self.name, self.last_name, self.pay)


class Developers(Employee):
    raise_amount = 1.1

    def __init__(self, name, last_name, pay, prog_lang):
        super().__init__(name, last_name, pay)
        self.prog_lang = prog_lang


class Managers(Employee):
    def __init__(self, name, last_name, pay, emp_incharge=None):
        super().__init__(name, last_name, pay)
        if emp_incharge is None:
            self.emp_incharge = []
        else:
            self.emp_incharge = emp_incharge

    def add_employee(self, emoployee):
        if emoployee not in self.emp_incharge:
            self.emp_incharge.append(emoployee)

    def del_emp(self, employee):
        if self.emp_incharge is not None:
            self.emp_incharge.remove(employee)

    def get_subordinates(self):
        for each in self.emp_incharge:
            print(f"--> {each.name} {each.last_name} ")


emp1 = Developers("crusader", "smith", 10000, "Python")
emp2 = Employee("john", "deer", 10000)
manager1 = Managers('ELon', 'Musk', 1)

print(emp1.full_name)
emp1.full_name = "Shubh Patni"
print(emp1.full_name)

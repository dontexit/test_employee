class Employee:
    num_of_emps = 0
    raise_amount = 1.04
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last +"@company.com"
        Employee.num_of_emps += 1
    def fullname(self):
        return('{} {}'.format(self.first,self.last))    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first,last,pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday () == 5:
            return False
        return True


class Developer(Employee):
    raise_amount = 1.10
    
    def __init__(self,first,last,pay, prog_lang):
        Employee.__init__(self,first,last,pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay,employees=None):
        Employee.__init__(self,first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def rem_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        if not self.employees:
            print("Employees not found under this manager.")
        
        for emp in self.employees:
                print("-->",emp.fullname()) 
        
dev_1 = Developer("Edwin","Hamal", 520000,"Python")

dev_2 = Developer("Dontexit","Lora", 45000,"PHP")

dev_3 = Developer("Gera","Guri", 8000,"Python")
dev_4 = Developer("Kera","Kuri", 89000,"Java")
dev_1.fullname()
dev_2.fullname()
dev_3.fullname()


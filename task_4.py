class EmployeeSalary():
    hourly_payment = 400
    def __init__(self, name, hours=None, rest_days=0, email=None):
        self.name = name
        self.rest_days = rest_days
        self.email = email
        self.hours = hours if hours else EmployeeSalary.get_hours(self.name, self.rest_days, self.email).hours

        if self.email is None: 
            self.email = EmployeeSalary.get_email(self.name, self.hours, self.rest_days).email

    @classmethod    
    def get_hours(cls, name, rest_days, email):
        hours = (7 - rest_days) * 8
        return cls(name, hours, rest_days, email)

    @classmethod    
    def get_email(cls, name, hours, rest_days):
        email = f"{name}@email.com"
        return cls(name, hours, rest_days, email)
    
    @classmethod    
    def set_hourly_payment(cls, hourly_payment=int):
        cls.hourly_payment = hourly_payment
    
    def salary(self):
        salary = self.hours * self.hourly_payment
        return salary

employee1 = EmployeeSalary("Иванов", hours=4, rest_days=2)
print("Имя сотрудника:", employee1.name, "количество выходных:", employee1.rest_days, "зарплата:", employee1.salary())

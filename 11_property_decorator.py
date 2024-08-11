class Employee:
    company = "Bharat Gas"
    salary = 560
    salarybouns = 200
   
    # totakSalary = 6100
   
    # setter method
    @property
    def totalSalary(self):
        return self.salary + self.salarybouns
    
    @totalSalary.setter
    def totalSalary(self, val):
        self.salarybouns = val - self.salary

    
e = Employee()
print(e.totalSalary)
e.totakSalary = 5800
print(e.salary)
print(e.salarybouns)
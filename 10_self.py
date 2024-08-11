class Employee:
    company = "Google"
    
    def getSalary(self,signature):
        print (f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")
    
    @staticmethod
    def great():
        print("Good morning,Sir")

harry = Employee()
harry.salary = 10000
harry.getSalary("Thanks!")
# Employee.getSalary(harry) 
harry.great()
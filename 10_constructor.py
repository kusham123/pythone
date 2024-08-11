class Employee:
    company = "Google"
    
    def __init__(self, name, salary, company):
        self.name = name
        self.salary =salary
        print("Employee is created!")

    def getDetails(self):
        print(f"The name of the employee is {self.name}")
        print(f"The salary of the employee is {self.salary}")
        print(f"The company of the employee is {self.company}")
    def getSalary(self,signature):
        print (f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")
    
    @staticmethod
    def great():
        print("Good morning,Sir")

harry = Employee("nitu", 10000, "Nokia")
# harry = Employee()  #thorw an missing 3 required positional arguments: 'name', 'salary', 'company'
harry.getDetails()
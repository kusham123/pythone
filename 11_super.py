class Person:
    country = "India"
    def __init__(self):
        print("Intializing Person...\n")
   
    def takeBreath(self):
        print("I am breathing..")

class Employee(Person):
    company = "Honda"
     
    def __init__(self):
         super().__init__()
         print("Intializing Employee...\n")

    def getSalary(self):
        print(f"Salary is {self.salary}")
    
    def takeBreath(self):
        super().takeBreath()
        print("I am an Employee so I am luckily breathing.. now")

class Programmer(Employee):
    company = "Fiverr"
    
    def __init__(self):
        super().__init__()
        print("Intializing Programmer...\n")
        
    def getSalary(self):
        print(f" No Salary to programmer")
    
    def takeBreath(self):
        super().takeBreath()
        print("I am a Programmer so I am breathing++..")

# p = Person()
# p.takeBreath()
# print(p.company)# throw an error 

# e = Employee()
# e.takeBreath()
# print(e.company)

pr = Programmer()
# pr.takeBreath()
# print(pr.country)
# print(pr.company)
# single inheritance
class Employee:
    company ="Google"
    def showDetail(self):
        print("this is an employee")

class Programmer(Employee):
    language = "Python"
    def getName(self):
        print(f"the lanuage is{self.language}")
    def showDetail(self):
        print("this is an programmer")
e = Employee()
e.showDetail()

P = Programmer()
P.showDetail()
print(P.company)
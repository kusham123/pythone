# Question-1
# make class programmer for storing info. of few programmers working at microsoft
# class Programmer:
#     company = "Microsoft"
#     def __init__(self,name, product):
#         self.name = name
#         self.product = product
#     def getInfo(self):
#         print(f"Then name of the programmer is {self.name} and the product is {self.product}")

# kush = Programmer("geetu", "Skype")
# alka = Programmer("Alka", "Github")
# kush.getInfo()
# alka.getInfo()

# ques-2
# class Calculator:
#     def __init__(self,num):
#         self.number = num
    
#     def square(self):
#         print(f"The value of {self.number} square is {self.number ** 2}")

#     def squareRoot(self):
#         print(f"The value of {self.number} square Root is {self.number ** 0.5}")

#     def cude(self):
#         print(f"The value of {self.number} cube is {self.number ** 3}")

# a = Calculator(4)
# a.square()
# a.squareRoot()
# a.cude()

# ques-3
# class Sample:
#     a = "Harry" #attribute of class
# obj = Sample()
# obj.a ="Vikky" # create instant attribute of object and not change class attribute
# data =obj.a
# Sample.a = "Vikky" # change class attribute
# print(data)

# Quest-4
# class Calculator:
#     def __init__(self,num):
#         self.number = num
    
#     def square(self):
#         print(f"The value of {self.number} square is {self.number ** 2}")

#     def squareRoot(self):
#         print(f"The value of {self.number} square Root is {self.number ** 0.5}")

#     def cude(self):
#         print(f"The value of {self.number} cube is {self.number ** 3}")

#     @staticmethod
#     def great():
#         print("********* Hello there welcome to the best calculator of the world*****")

# a = Calculator(4)
# a.square()
# a.squareRoot()
# a.cude()
# a.great()

# Question-5
# class Train:

#     def __init__(self, name, fare, seats):
#         self.name = name
#         self.fare = fare
#         self.seats = seats
#     def getStatus(self):
#         print(f"****************")
#         print(f"The name of the train is {self.name}")
#         print(f"The seats available of the train are {self.seats}")
#         print(f"****************")
    
#     def fareInfo(self):
#         print(f"The price of ticket is {self.fare}")
        
#     def bookTickt(self):
#         if(self.seats>0):

#            print(f"Your ticket hass been booked! Your seat number is {self.fare}")
#            self.seats = self.seats - 1
#         else:
#             print("sorry this train is fuyll kindly tri in tatkal")
    
#     # pending
#     def cancleTicket(self):
#            print(f"Your ticket has been Cancle! Your seat number is {self.fare}")
#            self.seats = self.seats + 1


# intercity = Train("intercity Express: 14015", 90, 2)
# intercity.getStatus()
# intercity.bookTickt()
# intercity.bookTickt()
# intercity.bookTickt()
# intercity.bookTickt()
# intercity.cancleTicket()
# intercity.fareInfo()


# ques-6
class Sample:
    def __init__(self,name):
        self.name =name
obj = Sample("geetu")

print(obj.name)
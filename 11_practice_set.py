# Ques-1
# class C2dVec:
#     def __init__(self, i, j):
#         self.icap = i
#         self.jcap = j
#     def __str__(self):
#         return f"{self.icap}i + {self.jcap}j"

# class C3dVec(C2dVec):
#     def __init__(self,i ,j, k):
#         super().__init__(i,j)
#         self.kcap = k

#     def __str__(self):
#         return f"{self.icap}i + {self.jcap}j + {self.kcap}k"
   

# v2d= C2dVec(1, 3)
# v3d= C3dVec(1, 5, 9)
# print(v2d)
# print(v3d)

# question-2
# multilevel inheritance
# class Animals:
#     animalsType = "Mammal"

# class pet:
#     color = "pink"

# class dog:
#     @staticmethod
#     def dark():
#         print("Bow bow!")


# d= dog()
# d.dark()


# questin-3
# class Employee:
#     salary =1000
#     increment = 2.5
#     @property
#     def salaryAfterIncrement(self):
#         return self.salary*self.increment
    
#     @salaryAfterIncrement.setter
#     def salaryAfterIncrement(self,reema):
#         self.increment = reema/self.salary

# e = Employee()
# print(e.salaryAfterIncrement)

# print(e.increment)

# e.salaryAfterIncrement=1000
# print(e.increment)

# question-4
# bug
# (a+bi)(c+di) = (ac-db) + (ab+bc)
# class Complex:
#     def __init__(self,r,i):
#         self.real = r
#         self.imaginary = i
    
#     def __add__(self,c):
#         return Complex(self.real + c.real, self.imaginary 
#         + c.imaginary)
    
#     def __mul__(self,c):
#         mulreal = self.real*c.real - self.imaginary*c.imaginary
#         mulImg = self.real*c.imaginary + self.imaginary*c.real
#         return Complex(mulreal,mulImg)
#     def __str__(self):
#         return f"{self.real} + {self.imaginary}i"
    
# c1 =  Complex(3, 2)
# c2 =  Complex(1, 7)
# print(c1 + c2)
# print(c1 + c2)

# Question-5
class Vector:
    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        str1 = ""
        index = 0
        for i in self.vec:
            str1 += f" {i}a{index} +"
            index +=1
        return str1[:-1]
    
    def __add__(self,vec2):
        newList = []
        for i in range (len(self.vec)):
            newList.append(self.vec[i] + vec2.vec[i])
        return Vector(newList)
    
    def __mul__(self,vec2):
        sum = 0
        for i in range (len(self.vec)):
            sum += self.vec[i] * vec2.vec[i]
        return sum

v1  = Vector([1,4,6])
v2  = Vector([1,4,6])
print(v1+v2)
print(v1*v2)


# Question-6

# class Vector:
#     def __init__(self, vec):
#         self.vec = vec

#     def __str__(self):
#         return f"{self.vec[0]}i + {self.vec[1]}j + {self.vec[2]}k"
    
    
# v1  = Vector([1,4,6])
# v2  = Vector([1,4,6])
# print(v1)

# question-7
class Vector:
    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        str1 = ""
        index = 0
        for i in self.vec:
            str1 += f" {i}a{index} +"
            index +=1
        return str1[:-1]
    
    def __add__(self,vec2):
        newList = []
        for i in range (len(self.vec)):
            newList.append(self.vec[i] + vec2.vec[i])
        return Vector(newList)
    
    def __mul__(self,vec2):
        sum = 0
        for i in range (len(self.vec)):
            sum += self.vec[i] * vec2.vec[i]
        return sum
    def __len__(self):
        return len(self.vec)

v1  = Vector([1,4,6,6,7])
v2  = Vector([1,4,6])
print(len(v1))
print(len(v2))

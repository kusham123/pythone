# Ques-1 print table
# num = int(input("Enter the name : "))
# i = 1
# for i in range(1,11):
    # multi = i*num
    # print(multi)
    # or
    # print(str(num) + " X " + str(i) + " = " + str(i*num))

# Ques-2  find find wich start with s
# l1 = ["Seema","nitu","riya","lokesh"]
# l1 = ['Seema','nitu','riya','lokesh']

# for name in l1:
#     if name.startswith("n"):
#         print("hello " + name)

# question-3
# num = int(input("Enter the name : "))
# i = 1

# while i<=10:
#     print(i * num)
#     i = i + 1

# ques-4 print prime num
# num = int(input("Enter the name : "))
# prime = True
# for i in range(2,num):
#     if(num%i == 0):
#         prime = False
#         break
# if prime:
#     print("This num is prime")
# else:
#     print("This number is not prime")


# ques-5
# pending

# ques-6
# 5! = 1 X 2 X 3 X 4 X 5
# num = int(input("Enter the number: "))
# factorial = 1
# for i in range(1,num+1):
#    factorial = factorial * i
# print(f"The factorial of {num} is {factorial}")


# ques-8 print 
# *
# **
# ***
# n = 4
# for i in range(4):
#     print("*" * (i+1))

# ques-7
#   *
#  ***
# *****
n = 3
for i in range(3):
    print(" " * (n-i-1),end="")
    print("*" * (2*i+1), end="")
    print(" " * (n-i-1))





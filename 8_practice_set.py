# ques-1
# def maximum(num1, num2, num3):
#     if(num1>num2):
#         if(num1>num3):
#             return num1
#         else:
#             return num3
#     else:
#         return num3
    
# m =maximum(3,5,8)
# print("The value of the maximum is " + str(m))

#Ques-2
# def farh(cel):
#     return (0*(9/5))+32
# c= 2
# f = farh(c)
# print("Fahraheit Temperature is : " + str(f))

# Ques-3
# print("Hello", end=" ")
# print("How", end=" ")
# print("are", end=" ")
# print("you", end=" ")

# ques-4
# sum(n) =sum(n-1)-n
# def sum_recursive(n):
#     if n == 1 or n == 0:
#         return 1
#     return sum_recursive(n-1)+n

# s= sum_recursive(3)
# print(s)

# ques-5
# n = 6
# for i in range(n):
#     print("*" * (n-i)) 

# ques-6
# pending

# ques-7
def remove_and_split(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()

this = "       Harry is a good     "
n = remove_and_split(this, "Harry")
print(n)

# 6:52

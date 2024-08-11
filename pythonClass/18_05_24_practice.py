# Define the two numbers
num1 = 10
num2 = 20


# Compare the two numbers using if and else
if num1 > num2:
    max_num = num1
else:
    max_num = num2

# Print the result
# print(f"The maximum of {num1} and {num2} is {max_num}")


# num1 = input("enter first name - ")
# num2 = input("enter first name - ")



# number = float(input("Enter a number: "))
# if number > 0:
#     print(f"The number {number} is positive.")
# elif number < 0:
#     print(f"The number {number} is negative.")
# else:
#     print(f"The number {number} is zero.")


#     number = int(input("Enter a number: "))
# if number / 5:
#     print(f"This {number} is divisible by 5.")
# elif number / 11:
#     print(f"This {number} is divisible by 11.")
# else:
#     print(f"This {number} is not divisible by 5 or 11.")



# char = input("Enter a character: ")

# if char.isalpha():
#     print(f"The character '{char}' is an alphabet letter.")
# else:
#     print(f"The character '{char}' is not an alphabet letter.")

# num1 = int(input("Enter the start of the range: "))
# num2 = int(input("Enter the end of the range: "))

# if((a>"A" and a<="Z") or (a>="a" and a<="z")):
#     print()

# print(f"Even numbers are:")
# for num in range(num1, num2):
#     if num % 2 == 0:
#         print(num, end=" ")

# num1 = int(input("Enter the start of the range: "))
# num2 = int(input("Enter the end of the range: "))

# print(f"Even numbers are:")
# for num in range(1, num2):
#     num +=num
#     print(num)

# or

# num = int(input("Enter the number: "))
# num2 = 1
# for i in range(1,num):
#    num2 = num2 + i
#    print(f"All number sum is {num2}")


#Quest-7 python program to check number is correct form or not

# num1 = input("Enter the number = ")
# print(type(num1))
# if type(int(num1)):
#     print(f"{num1} Number is intger type")
# else:
#     print(f"{num1} This is not intger type")

# python program to check number is correct form or not
num1 = input("Enter the number = ")
if isinstance(num1, int):
    print(f"{num1} is an integer")
else:
    print(f"{num1} is not an integer")

#  python program to check if given string(character should not contain special )
# string = input("Enter string = ")
# if all(char.isalnum() for char in string):
#     print(f"'{string}' contains only alphanumeric characters.")
# else:
#     print(f"'{string}' contains special characters.")

# python program to check  character and number is correct form or not

# value = input("Enter the value = ")
# if isinstance(value, int):
#     print(f"{value} is an integer")
# elif isinstance(value, str):
#     print(f"{value} is an string")
# else:
#     print(f"{value} is not an integer or string")

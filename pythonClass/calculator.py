first = int(input("enter the first number: "))
second = int(input("enter the second number: "))
operator = input("enter the operator you need to perforn(+,-,*,/)")

if operator == "+":
    print(first + second)
elif operator == "-":
    print(first - second)
elif operator == "*":
    print(first * second)
else:
    print("invalid operator")

# print(5//2)
# print(5/2)
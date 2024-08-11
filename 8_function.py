def percent(marks):
    return ((marks[0] + marks[1] + marks[2])/300)*100

marks = [45,34,23]
# percentage1 = (sum(marks)/300)*100
# percentage1 = ((marks[0] + marks[1] + marks[2])/300)*100
percentage1 = percent(marks)

marks2 = [43,36,53]
# percentage2 = (sum(marks2)/300)*100
# percentage2 = ((marks2[0] + marks2[1] + marks2[2])/300)*100
percentage2 = percent(marks2)
# print(percentage1,percentage2)


# def greet(name):
#     print("good morning" + name)
# a= greet(" preeti ")
# print(a)

# factorial funtion
def factorial(n):
    product = 1
    for i in range(n):
        product = product * (i+1)
    
    return product
# or

def factorial_recursive(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial_recursive(n-1)

# f= factorial(5)
f= factorial_recursive(0)
print(f)
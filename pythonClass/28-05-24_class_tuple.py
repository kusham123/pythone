# tuple = (1,2,3,4,1)
# print(tuple)
# print("Count of 1 in input is:", tuple.count(1))

# list1 = [(1,2,3),(2,3,6)]

# class1 = int(input("Enter no of studen = "))
# list1 =[]
# for i in range(class1):
#     firstName = input("Enter your first name = ")
#     lastName = input("Enter your last name = ")
    
#     tuple=(firstName,lastName)
# list1.append(tuple)
# print(list1)

# lst = [2]*3
# print(lst)

#num perfect or not
# num = int(input("Enter number"))
# for i in range(num):
#     val = num%i
#     print(val)

# you are given a number and intger k
# youare also given a array 

k = int(input("Enter value of k = "))
num = int(input("Enter your number = "))
arr = list(map(int,input().split()))
frequency = [0]*10

for i in range(num):
  frequency[arr[i]]+=1

res =[]

for i in range(10):
    if frequency[i]>=k:
     res.append(arr[i])
print(res)

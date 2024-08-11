# list =[]
# for i in range(5):
#     list.append(int(input("Enter a number:")))
# print("List:",list)



# list1 = [1,2,3,4,5]

# # method 1
# for i in list1:  #i is defined as value
#     print(i)

# for i in range

# question-1 you are given a number n, size of list and n element of list.you have to find the maximum number in list
# num=3
# num =int(input("Enter your number range = "))
# list1 =[]
# for i in range(0, num):
#     list1.append(int(input("your list = ")))
# max = list1[0]

# for i in range(1,num):
#     if list1[i] > max:
#         max =list1[i]
#         print(max)

# count = 0
# for i in range(num):
#     if list[i] == max:
#         count += 1
#         print("count in max no in  list is = ",count)


num1 = int(input("enter first number = "))
num2 = int(input("enter second number = "))
list2 =[]
list1 =[]
for i in range(num1):
    list1.append(int(input("your list 1 = ")))
    print(list1)


for j in range(num2):
    list2.append(int(input("your list 2 = ")))
    print(list2)
   
list3 = []
for i in range(len(list1)):
    count = 0
    for j in range(len(list2)):
        if list1[i]<list2[j]:
            count += 1
    list3.append(count)

print(list3)


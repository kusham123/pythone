# my_dic = {"name":"nitu",
#           "age":"23",
#           "city":"new yourk"}
# print(my_dic['age'])

# you are give an array of integers. you need to print all occurence of each number
# input give like array sie=6
# 1 2 1 3 2 4
# output =  1 : 2
# 2 : 2
# 3 : 1
# 4 : 1
# n = int(input("enter array size num = "))
# arr = list(map(int,input().split()))

# freq = {}
# for i in arr:
#     if i in freq:
#         freq[i] += 1
#     else:
#         freq[i] = 1

# for key, value in freq.items():
#     print(key,":", value)


# question-2 find size of dicnatory of lenth

#you are given array of string, you need print all the string size ahead of the string
# input : ['a', 'ab','adc','b', 'dd','abcd'
# output
# 1: a,b
# 2: ab,dd
# 3: abd
# 4: abcd
# n = int(input("enter array string = "))
# arr = list(map(str,input().split()))

# freq = {}
# for i in arr:
#     size = len(i)
#     freq[i] =size

# for key, value in freq.items():
#     print(value,":",key)
# print(i)

# or sir solution

# n = int(input("enter array string = "))
# arr = list(map(str,input().split()))

# # array define second method
# # arr = []
# # for i in range(n):
# #    arr.append(input())

# dict ={}
# for i in arr:
#     if len(i) in dict:
#       dict[len(i)].append(i)
#     else:
#        dict[len(i)] = [i]

# print(dict)



# Question -3 
# you are given an array of intgers arr[]
# now you are given a quey
# each query contain a numbeer x
# you need to print the count of number in array arr[]
# 1<=size of array<=10*5
# 1<=arr[i]<=10
# 1<=x<=10*9

# input : arr[] = [1,2,1,4,5,6,3,8,9,3]
# q = 6
# query = [1,2,3,4,5,15]
# output: [2,1,2,1,1,0] 

# arr = list(map(str,input().split()))
n = int(input("enter size of array = "))

arr = []
for i in range(n):
   arr.append(int(input()))
q = int(input("Enter number of queries: "))

query = []
for j in range(q):
   query.append(int(input("query numbers : ")))


dict = {}
for i in arr:
   if i in dict:
       dict[i] += 1
   else:
       dict[i] = 1
# print(dict)
# here output : {2: 1, 3: 1, 4: 1, 67: 1, 45: 1}

ans =[]
for i in query:
   if i in dict:
      ans.append(dict[i])
   else:
      ans.append(0)
print(ans)

# https://leetcode.com/problems/contains-duplicate/description/

# https://leetcode.com/problems/first-letter-to-appear-twice/description/
# https://leetcode.com/problems/remove-letter-to-equalize-frequency/description/
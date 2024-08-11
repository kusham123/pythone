# 1)you are given an array of size n find number of unique element in array
# 2)your are give an array n and integer k, find the count of subarray having unique element <=K
# input =[1,2,1,3], k=2
# output = 8

# n = int(input("Enter the size of array: "));
# lst = list(map(int,input().split()))

# s = set()
# for i in range(len(lst)):
#     s.add(lst[i])
# print(len(s))

# ques-2
n = int(input("Enter the size of array: "))
arr = list(map(int,input().split()))
k = int(input("Enter the  value of k: "))

res=0

for i in range(n):
    subarray = set()
    for j in range(i,n):
        subarray.add(arr[j])
        if len(subarray) <= k:
            res += 1
        else:
            break
print(res)

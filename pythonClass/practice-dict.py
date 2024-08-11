# Ques - 1 Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct. 

# n = int(input("enter size of array = "))
# arr = []
# for i in range(n):
#     arr.append(int(input()))

# dict = {}
# for i in arr:
#     if i in dict:
#        result = True
#        break
#     dict[i] = True
# else: 
#     result = False
# print(result)

# Given a string s consisting of lowercase English letters, return the first letter to appear twice.
n = str(input("enter size of array = "))
dict ={}
for i in n:
    if i in dict:
        print(i)
        break
    dict[i] = True
    
# def first_letter_to_appear_twice(s):
#     seen = {}
#     for char in s:
#         if char in seen:
#             return char
#         print(char)
#         seen[char] = True

# # Example usage:
# # s = "abcddcba"
# s = str(input("enter size of array = "))
# print(first_letter_to_appear_twice(s))  # Output: "d"    

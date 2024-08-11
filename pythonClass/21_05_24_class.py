
# num = int(input("Enter you number"))
# for i in range(1,num):
#     print(i)

# print a program for print this:- 
# 1
# 12
# 123
# 1234

num = int(input("Enter you number = "))
for i in range(num):
    for j in range(0,i+1):
        print(j+1,end="")
    print("")



#Ques-1 find greaterest of four numbers enter by user
# num1 = int(input("Enter number 1: "))
# num2 = int(input("Enter number 2: "))
# num3 = int(input("Enter number 3: "))
# num4 = int(input("Enter number 4: "))

# if(num1>num4):
#     f1 = num1
# else:
#     f1 = num4
    
# if(num2>num3):
#     f2 = num2
# else:
#     f2 = num3

# if(f1>f2):
#     print(str(f1) + "is greatest")
# else:
#     print(str(f2) + "is greatest")


# Quest-2 student pass/fail if it requird 40% and marks atlest 33%

# sub1 = int(input("Enter first Subj marks :"))
# sub2 = int(input("Enter second Subj marks :"))
# sub3 = int(input("Enter third Subj marks :"))

# if(sub1<33 or sub2<33 or sub3<33):
#     print("you are fail")
# elif((sub1+sub2+sub3)/3 <40):
#     print("You are fail due to total persantege less than 40")
# else:
#     print("Congratualation You are pass ")

# Question-3
# text = input("Enter the text :")
# spam = False

# if("make a lot of money" in text):
#     spam = True
# elif("buy now" in text):
#     spam = True
# elif("subscribe this" in text):
#     spam = True
# elif("click this" in text):
#     spam = True
# else:
#     spam =False

# if(spam):
#     print("This text is spam")
# else:
#     print("This text is not spam")


# Ques-4 
# name = input("Enter username :")

# if(len(name)<10):
#     print("correct username")
# else:
#     print("username sholud be less than 10 charcter")

# ques-5
# names =["harry", "ritu", "rohit","seema"]
# name = input("Enter name to check :")

# if name in names:
#     print("your name is present in the list")
# else:
#     print("your name is not present in the list")

# question-6
# marks = int(input("Enter your marks : "))

# if marks>=90:
#     grade = "Ex"
# elif marks>=80:
#     grade = "A"
# elif marks>=70:
#     grade = "B"
# elif marks>=60:
#     grade = "C"
# elif marks>=50:
#     grade = "D"
# else:
#     grade ="Fail"
    
# print("your grade is " + grade)

# Question-7
post = "are you geetu yadav. how study in sayta colleage from palwal"

word = input("Enter searching your word :")

if post.find("geetu"):
    print("Your finding word this : " + word)
else:
    print("Your word not found")

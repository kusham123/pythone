# ques-1 

mydict = {
    "Pankha" :"Fan",
    "Dabba" :"Box",
    "kurshi" :"chair"
}
# print("Option are ", mydict.keys())
# a = input("Enter the Hindi Word\n")
# print("The meaning of your word is:", mydict[a])

# Below line will not throw error if key is not present in the dictionary
# print("The meaning of your word is:", mydict.get(a))


# quest-2 
# write a progaram to input 8 number from user and dipaly all unique number

# num1 = int(input("Enter Number 1 :"))
# num2 = int(input("Enter Number 2 :"))
# num3 = int(input("Enter Number 3 :"))
# num4 = int(input("Enter Number 4 :"))
# num5 = int(input("Enter Number 5 :"))
# num6 = int(input("Enter Number 6 :"))
# num7 = int(input("Enter Number 7 :"))
# num8 = int(input("Enter Number 8 :"))

# s = {num1,num2,num3,num4,num5,num7,num8}
# print(s)

# ques-3
s = {18,"18",18.7}
print(s)


# ques-4
s = {18,"18",18.0}
s =set()
s.add(20)
s.add(20.0) 
s.add("20")
print(s)

# quest-5  what type of p= {}
p= {}
print(type(p)) #dictionary

# quest-6
FavLang ={}
a = input("Enter your favorite language Ankit\n") 
b = input("Enter your favorite language Geetu\n") 
c = input("Enter your favorite language Sonali\n") 
d = input("Enter your favorite language Harsita\n") 
FavLang['ankit'] = a
FavLang['geetu'] = b
FavLang['sonali'] = c
FavLang['Harshita'] = d
print(FavLang)
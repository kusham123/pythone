# Ques-1
# f = open('poem.txt')
# t = f.read()
# if 'Twinkle' in t:
#     print("Twinkle is present")
# else:
#     print("Twinkle is not present")
# f.close()

# ques-1
# def game():
#     return 89

# score = game()
# with open("hiscore.txt") as f:
#     hiScoreStr = f.read()

# if hiScoreStr=='':
#     with open("hiscore.txt","w") as f:
#         f.write(str(score))

# elif int(hiScoreStr)<score:
#     with open("hiscore.txt","w") as f:
#         f.write(str(score))


# question-3

    # for i in range(2,21):
    #     with open(f"table/multiplication_table_of_{i}.txt",'w') as f:
    #         for j in range(1,11):
    #             f.write(f"{i}X{j} = {i*j}\n")
    #     break

# # ques-4

# with open("sample.txt") as f:
#     content = f.read()

# content = content.replace("donkey","#8789234")
# with open("sample.txt","w") as f:
#     f.write(content)


# ques-5
# words =['donkey','mote','kaddu']
# with open("sample.txt") as f:
#     content = f.read()
# for word in words:
#     content = content.replace(word,"#8789234")
#     with open("sample.txt","w") as f:
#         f.write(content)

# # Ques-6 log file read
# with open("log.txt") as f:
#     content = f.read()
# if 'python' in content.lower():
#     print("yes ython is present")
# else:
#     print("NO python is present")


# Ques-7 log file read
# content = True
# i = 1
# with open("log.txt") as f:
#     while content:
#         content = f.readline()
            
#         if 'python' in content.lower():
#             print(content)
#             print(f"yes python is present {i}")
            
#         i+=1


# ques-8 copy this.txt content into copy.txt
# with open("this.txt") as f:
#     content = f.read()
# with open("copy.txt", 'w') as f:
#      f.write(content)


# ques-9 find identcal(same) file
# file1 = "copy.txt"
# file2 = "this.txt"

# with open(file1) as f:
#     f1 = f.read()

# with open(file2) as f:
#     f2 = f.read()
    
# if f1 == f2:
#     print("files are idential")
# else:
#     print("files are idential")


# ques-9
# filename = "sample.txt"
# with open(filename, "w") as f:
#     f.write("")

# Ques-10
import os
oldname = "sample2.txt"
newname = "renamed_by_python.txt"
with open(oldname) as f:
     content = f.read()
with open(newname,'w') as f:
     f.write(content)
     os.remove(oldname)
     
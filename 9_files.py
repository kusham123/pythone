f = open('sample.txt','w')
# data = f.read()
# data = f.read(5) #read first charcter of a file
# data = f.readline()
# print(data)
# data = f.readline()
# print(data)

# f.write("why are your study")
with open("sample.txt") as f :
    f.read()
f.close()

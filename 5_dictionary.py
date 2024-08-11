myDict ={
    "Fast" : "in a Quick manner",
    "Harry" : "A Coder",
    "Marks" : [1,2,6],
    "anotherDict" : {'meena': "singer"},
}
# print(myDict['Fast'])
# print(myDict['Marks'])
# print(myDict['anotherDict']['meena'])

# dictionary methods
# print(list(myDict.keys()))
# print(list(myDict.values()))
# print(list(myDict.items()))

updateDict = {
    "Lovish" : "Friend",
    "Divya" : "Friend",
    "Nitu" : "Friend"
}
myDict.update(updateDict)
# print(myDict)

print(myDict.get("herry")) #print value associated with key "herry"
print(myDict["herry"])   #print value associated with key "herry"

# the diffrence between .get and [] syntax in dictionaries ?
print(myDict.get("herry2"))  #return none as harry2 is not present in the disctionary
print(myDict.get["herry2"]) #throw an error as harry2 is not present in the disctionary
a = {1,2,3,5,1}
# print(type(a))
# print(a)

# important: This syntax will create an empty dictionary and not an empty set
a = {}
# print(type(a))

# an empty set can be created using the below syntax
b = set()
# print(type(b))

# methods of set
# add values to an empty set
b.add(3)
b.add(5)
b.add(3) # Adding a values repeatedly does not change a set

# list not add in set
# b.add([4,5,6])

# tuple add in sets
b.add((4,5,6))

# dictionary not add in sets
# b.add({4:5})

print(len(b)) # pritns length of this set

# Removal of an Item
# b.remove(3) # Removes 5 front set b
# b.remove(15) # throw an error while trying to remove 15 (which is not present in the set) 
print(b)

print(b.pop()) # remove element in set 
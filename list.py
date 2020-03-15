list = []


#Add item to end of the list
list.append('index0')

print(list)


list.append('index1')
list.append('index2')
list.append('index3')
list.append('index4')
list.append('index5')
list.append('index6')
print(list[1])


animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
#Take index of item
duck_index = animals.index("duck")

#Add item middle of list
animals.insert(duck_index, "cobra")

print (animals)

#Sort list

list.insert(3, 'index7')
print(list)
list.sort()
print(list)



#Count of list
count = len(list)


#Remove from list
list.remove('index7')
print(list)

# The first and second items (index zero and one)
first = list[0:2]

# Third and fourth items (index two and three)
middle = list[2:4]

# The last two items (index four and five)
last =  list[4:]

print(first)
print(middle)
print(last)



animals = "catdogfrog"

# The first three characters of animals
cat = animals[:3]

# The fourth through sixth characters
dog = animals[3:6]

# From the seventh character to the end
frog = animals[6:]


for animal in animals:
    print (animal)


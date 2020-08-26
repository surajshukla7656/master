sea_creatures = ['shark', 'cuttlefish', 'squid', 'mantis shrimp', 'anemone']
print(sea_creatures)

# concatenate string items in a list 
# with other strings using the + operator
print('Sammy is a ' + sea_creatures[0])

sea_creatures = ['shark', 'cuttlefish', 'squid', 'mantis shrimp', 'anemone']
print(sea_creatures)

sea_creatures[1] = 'octopus'
print(sea_creatures)

sea_creatures[-3] = 'blobfish'
print(sea_creatures)

sea_creatures = ['shark', 'cuttlefish', 'squid', 'mantis shrimp', 'anemone']
print(sea_creatures)



# When creating a slice, as in [1:4], 
# the first index number is where the slice starts (inclusive), 
# and the second index number is where the slice ends (exclusive), 
print(sea_creatures[1:4])

# If we want to include either end of the list,
#  we can omit one of the numbers in the list[x:y] syntax
print(sea_creatures[:3])
print(sea_creatures[2:])

# We can also use negative index numbers
#  when slicing lists, just like with positive index numbers:
print(sea_creatures[-4:-2])
print(sea_creatures[-3:])
#  is called stride, which refers to how many 
# items to move forward after the first item 
# is retrieved from the list.

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

print(numbers)
print(numbers[1:11:2])
print(numbers[::3])

sea_creatures = ['shark', 'octopus', 'blobfish', 'mantis shrimp', 'anemone']
oceans = ['Pacific', 'Atlantic', 'Indian', 'Southern', 'Arctic']

print(sea_creatures + oceans)
# it can be used to add an item (or several) 
# in list form to the end of another list.
#  Remember to place the item in square brackets:

sea_creatures = ['shark', 'octopus', 'blobfish', 'mantis shrimp', 'anemone']
sea_creatures = sea_creatures + ['yeti crab']
print (sea_creatures)

sea_creatures = ['shark', 'octopus', 'blobfish', 'mantis shrimp', 'anemone']
oceans = ['Pacific', 'Atlantic', 'Indian', 'Southern', 'Arctic']


# By using the * operator we can replicate 
# our lists by the number of times we specify.

# Let’s multiply the sea_creatures list by 2 
# and the oceans list by 3:

print(sea_creatures * 2)
print(oceans * 3)
sea_creatures = ['shark', 'octopus', 'blobfish', 'mantis shrimp', 'anemone']

# The += and *= compound operators can be used to 
# populate lists in a quick and automated way

for x in range(1,4):
    sea_creatures += ['fish']
    print(sea_creatures)

# The *= operator behaves in a similar way:
sharks = ['shark']

for x in range(1,4):
    sharks *= 2
    print(sharks)
# it can have elements of different data types

#  Create list
list1 = [14, 'March', 1879, 'Ulm', 'Germany']
print(list1)

sea_creatures =['shark', 'octopus', 'blobfish', 'mantis shrimp', 'anemone', 'yeti crab']

del sea_creatures[1]
print(sea_creatures)

sea_creatures =['shark', 'octopus', 'blobfish', 'mantis shrimp', 'anemone', 'yeti crab']

del sea_creatures[1:4]
print(sea_creatures)

sea_names = [['shark', 'octopus', 'squid', 'mantis shrimp'],['Sammy', 'Jesse', 'Drew', 'Jamie']]

print(sea_names[1][0])
print(sea_names[0][0])
print(sea_names[1][2])
#  list.append()

fish = ['barracuda','cod','devil ray','eel']
fish.append('flounder')
print(fish)
#  list.insert()
fish = ['barracuda','cod','devil ray','eel', 'flounder']

fish.insert(0,'anchovy')
print(fish)

fish.insert(3,'damselfish')
print(fish)
# list.extend()
fish = ['barracuda','cod','devil ray','eel', 'flounder']

more_fish = ['goby','herring','ide','kissing gourami']

fish.extend(more_fish)
print(fish)
I have been observing that they are not attending the chemistry classes too on regular basis.

Deepanshu
Supreet Singh
MD Sayeed Irfan
Sahzad Hussain
Kaushal Kumar
Aman (11)
Hemlata
Samrat 
Gaurav Sharma
Dipsikha 
Manish

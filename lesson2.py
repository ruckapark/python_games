# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 10:19:27 2020

@author: George
"""

#%% dictionaries

phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)

phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}

#not how it would make more sense to store phonenumbers as a string to have the 0 at the beginning
# phonebook.update({'George':01367842718,'Laura':01435928930})
phonebook.update({'George':1367842718,'Laura':1435928930})

print(phonebook)

# we could even store list and other dictionaries inside a dictionary
phonebook = {'England':{},'France':{}}
phonebook['England'].update({
        'George':'+44 1839 823 345',
        'Becky':'+44 8394 234 234',
        'Hatty':'+44 7329 434 234'
        })
phonebook['France'].update({
        'Patrice':'+33 7 34 23 15 34',
        'Benoit':'+33 6 12 32 15 24'
        })

#have a look on variable explorer at the phonebook
print(phonebook['France'])
print(phonebook['England']['George'])

#challenge ideas - look up good dictionary exercise (store a list in a dictionary and do some of the previous list manipulation)
#make the dictionaries obviously relevant to lesson 3 . i.e. the colours dictionary!!

#%% while loops - run according to a True or a False
x = 1
while x < 5:
    print('{} is less than 5'.format(x))
    x += 1
# maybe add here print('5 has been reached')
    
#typical game loop
running = True
score = 0
while running:
    #game functions
    score += 1
    if score >= 10:
        print('Well done, level 1 complete!')
        running = False
        
#%% for loops - maybe draw a little flow diagram / logigramme

for i in range(10):
    print(i)

names = ['George','Hatty','Adam','Henry','Rebecca','Loretta','Renato']
for i in range(4):
    print(names[i])
    
#to get all of them
for i in range(len(names)):
    print(names[i])
    
#or even better
for name in names:
    print(name)
    
#only print names beginning with h? - introduce lower
for name in names:
    if name[0].lower() == 'h': print(name)
    
#let's see if we can make the for loop above with a while loop
#illustrate it is possible but explain why in some cases it is largely preferable to use one of the other
names_len = len(names)
i = 0
while i < names_len:
    if names[i][0].lower() == 'h': print(names[i])
    i += 1
#while you can often make a for loop with a while loop
#while loops can't always be replicated by a for loop (we have to know the number of iterations in advance)

#%% nested loops andloop keywords to break out etc.
for country in phonebook:
    for contact in phonebook[country]:
        print('{} is from {}'.format(contact,country))
        print('Their phone number is: ',phonebook[country][contact])

running = True
enemies = 10 #imagine we have 10 space invaders on screen
while running:
    for i in range(enemies):
        if i == 8: running = False
    
#break and continue may need to be used
#by far the most common time to force break out of a loop is when a condition is met

for number in range(5):
    print(number)
    
for number in range(5):
    print(number)
    if number == 2: break

#let's see exactly the effect break will have if used in a nested loop
#here is a loop to check if a number is prime
i = 2
while(i < 100):
   j = 2
   while(j <= (i/j)):
      if not(i%j): break
      j += 1
   if (j > i/j) : print(i, 'is prime')
   i += 1
   
#clearly we can think of break like sending us backk to the previous tab indent
#it won't send us the whole way back to 0
   
#challenges look up some good exercises to do with for loops
#make a game loop that is a game of rock paper scissors

#%% functions - remember pass or ...
def add(x,y):
    addition = x + y
    return addition

def subtract(x,y):
    return x - y

def is_prime(x):
    """
    The function checks if the x input is prime
    """
    i = 2
    prime = 1
    while i <= x**0.5:
        if x%i == 0:
            prime = 0
            break
        i+=1
        # print(i)
    if prime: return True
    else: return False
    
# challenge look up function exercises and add to game

#%% list comprehensions - don't go into to much detail just explain that the more they use this the more obvious it will get
    #you never NEED a list comprehension
    #it makes the code more compact and sometime much easier to read
    #it also ensures higher code efficiency - as seen timing

numbers = []
numbers = [0,1,2,3,4,5,6,7,8,9]
numbers = []
for i in range(10):
    numbers.append(i)
numbers = []
numbers = [i for i in range(10)]

names = ['Hatty','George','Henry','Adam','Thomas']
names_h = [name for name in names if 'h' in name.lower()]

#challenge - use the time it module to differentiate between:
    #for i in range(100000000000): numbers.append(i)
    #numbers = [i for i in range(10000000000)]

#%% zip
# for any data structure that we can run a loop trhough we call it an iterable
# if we want to join to iterbales into the same iterable we can

keys = ['one','two','three']
x = [1,2,3]
y = [2,5,8]
zipped = zip(x,y)
zip_list = list(zipped)
zip_dic = dict(zipped)
keys_copy = zip_dic.keys()
x_copy = zip_dic.values()

#challenges - not necessary
for i,x in enumerate(x):
    print('i:', i, ', x:', x)
    
#%% enumerate
#not useful this is wrong! should be index, key
for key, value in enumerate(zip_dic):
    print(key,':',value)

for i, (key,value) in enumerate(zip_dic.items()):
    print(i,':',key)
    print(i,':',value)


#%% no longer in notbooke 
    #classes and objects - this concept is really important for games
    #each independant thing is an object!
    # a class can be thought of as a template
    
class ClassA:
    #a default speed for all objects of class A
    speed = 10
    player_type = 'enemy' #class A is for the enemies

    #self refers to the variables within the class itself
    def describe(self):
        print("This {} is moving at {} m/s".format(self.player_type,self.speed))
        
# we now have a variable that contains a python object of classA
enemy_1 = ClassA()
enemy_2 = ClassA()
enemy_3 = ClassA()
enemy_3.speed = 5      #make it a bit slower
print(enemy_1.speed)
enemy_3.describe()


#modules and packages (os, PIL, numpy, random, turtledraw)


#lambda functions? - challenge maybe
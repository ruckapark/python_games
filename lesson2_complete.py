# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 10:19:27 2020

@author: George
"""

#%% 
#range is called an iterator (runs through numbers). Let's see what it looks like as a list    
print(list(range(10)))

#it doesnt matter what the temporary variable is called, but it has to be consistent
for i in range(10):
    print(i)
for x in range(1,11):
    print(x)
for number in range(23,28):
    print(number)

#let's add some family members    
family = ['mum','dad','sister','brother']
for member in family:
    print(member)
    
#now lets add the ages
ages = [60,65,21,0]
for age in ages:
    print(age)
    
length = 4
length = len(ages) #could also be len(family)
for x in range(length):
    print(family[x],'is',ages[x],'years old!')
    
"""
Exercises:
    1.Take your list of game characters and make a for loop that prints their names
    2. Add a message to the for loop - print(char,'is a game character')
    3. Make a new list that has a speed variable for each character called speeds.
    Then work out the length of the lists using len() and make a for loop that prints
    a message for each character and their speed (like i did with my family and the ages)
"""

#%% while loops - run according to a True or a False (remember if statements)
x = 1
while x < 5:
    print(x,'is less than 5')
    x = x + 1
    
#typical game loop
running = True
score = 0
while running:
    #increase the score by 1
    score += 1
    if score >= 10:
        print('Well done, level 1 complete!')
        #stop the while loop!
        running = False
        
#heres anoher example
running = True
enemies = 10 #imagine we have 10 space invaders on screen
while running:
    for i in range(enemies):
        if i == 8: 
            running = False
            
"""
Exercises: Make a new if condition to stop the while loop instead of i == 8
           When you make running = False, print a message saying the game has finished
           
           If you finish this you can go on an keep trying to add more for loops and if
           statements into the while  loop!
"""
   
#make a game loop that is a game of rock paper scissors
import random
running = True
answers = ['rock','paper','scissors']
i = 0
while running:
    answer = input('Rock, Paper, Scissors?').lower()
    comp = answers[random.randint(0,2)]
    
    if answer == 'rock':
        if comp == 'scissors':
            score += 1
            print('nice')
        elif comp == 'paper':
            score -= 1
            print('oops')
        else:
            print('draw')
    elif answer == 'scissors':
        #try to fill these in yourself!
        pass
    else:
        #try to fill these in yourself!
        pass
    
    #best of three
    if i == 3:
        if score > 0:
            print('You win!')
        elif score == 0:
            print('Its a draw!')
        else:
            print('You lose...')
        running = False
    
    i+=1
#challenge is to fill in the elif and else parts yourself - Then play against the computer!
#%% functions - remember pass or ...
def add(x,y):
    addition = x + y
    return addition

sum1 = add(1,3)
sum2 = add(2,6)
print('1 + 3 is',sum1,'2 + 6 is',sum2)

def subtract(x,y):
    return x - y
print(subtract(10,25))

def my_name():
    print('my name is George')

def random_name():
    import random
    names = ['George','Max','Harry','Jess','Michael','John','Susan']
    index = random.randint(0,len(names))
    return names[index]
print(random_name())

def is_prime(x):
    """
    The function checks if the x input is prime
    """
    i = 2
    prime = 1
    while i <= x*0.5:
        if x%i == 0:
            prime = 0
            break
        i+=1
        # print(i)
    if prime: return True
    else: return False
is_prime(73) #should give true

"""
Exercises:
    1. Make a function that divides two number
    2. Make a function that takes a number, adds 5, then returns the new number (test it!)
    3. See if you can make a function that prints a random number from 1-10 (similar to random_name())
    4. Use a for loop to print only the prime numbers up to 100 - hint is below!
"""
for i in range(50):
    if is_prime(i):
        print(i,'is prime!')

#%% no longer in notbooke 
    #classes and objects - this concept is really important for games
    #each independant thing is an object!
    # a class can be thought of as a template
    
class EnemyClass:
    #a default speed for all objects of class A
    def __init__(self):
        self.speed = 10
        self.player_type = 'enemy' #class A is for the enemies

    #self refers to the variables within the class itself
    def describe(self):
        print("This {} is moving at {} m/s".format(self.player_type,self.speed))
        
# we now have a variable that contains a python object of classA
enemy_1 = EnemyClass()
enemy_2 = EnemyClass()
enemy_3 = EnemyClass()
enemy_3.speed = 5      #make it a bit slower
print(enemy_1.speed)

#use a function!
enemy_3.describe()

"""
To understand why a class is really useful we need to understand the init function

This function is built in and runs automatically when we make a class
The easiest way to understand this is with an example of using __init__  and self together

We always start classes with a capital letter to keep things consistent!
"""
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)
p2 = Person("George", 23)
p3 = Person("Tom",15)

people = [p1,p2,p3]

for person in people:
    print(person.name, ' is:',person.age)
    
"""
We don't have to use 'self' it just keeps things easy to read

Let's see if we can work out what is going on here:
    - clearly if we use self it looks a lot neater!
"""

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myname(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

#easier to read
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

#%% see if you can do these ones by yourselves

def max_of_three(a,b,c):
    """
    Write a Python function to find the Max of three numbers
    
    in reality we would just use the python inbuilt function!
    """
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b 
    else:
        return c
    
def unique_counts(list_):
    """
    Write a Python function that takes a list and returns a new list with unique elements of the first lis
    """
    new_list = []
    for element in list_:
        if element not in new_list: new_list.append(element)
    

#%%modules and packages (os, PIL, numpy, random, turtledraw, tinker maybe)
# from x import y
# import x as y
#numpy and scipy are the maths modules most widely used, we wont need them much but look at how easy it is compared with writing a function for a list ourself.
import numpy as np
x = np.array([1,2,3,4])
y = np.array([2,4,6,8])

print(x/y)
print(x*y)
print(np.mean([x,y]))
print(np.transpose(x))

#%%
import turtle

george = turtle.Turtle()
screen = turtle.Screen()
# set the speed to the highest setting
george.speed(1)
screen.clearscreen()
# draw a square
for i in range(4):
  george.forward(50)
  george.right(90)

# move the turtle without drawing
george.penup()
george.back(50)
george.right(90)
george.forward(55)
george.left(90)
george.pendown()

# draw a triangle
for i in range(3):
  george.forward(150)
  george.left(120)

# move the turtle
george.penup()
george.back(40)
george.right(90)
george.back(50)
george.pendown()

# draw a circle
for i in range(360):
  george.forward(2)
  george.left(1)
  
  
#%%
turtle.clearscreen()
turtle.reset()
  
colors = ['red','blue','green','yellow']
#here is how we fill a circle

george.color('green','yellow')
george.pensize(6)
george.width(6)
george.begin_fill()
george.circle(40)
george.end_fill()

def square(turtle_,length):
    for i in range(4):
        turtle_.forward(length)
        turtle_.right(90)
        
george.penup()
george.forward(100)
george.pendown()

#first color is outline, second is fill color
george.color('red','blue')
george.begin_fill()
square(george,75)
george.end_fill()

import random
turtle.Screen().exitonclick()
def circle(turtle_):
    
    colors = 'red blue green yellow black'.split()
    
    x = random.randint(-150,150)
    y = random.randint(-150,150)
    radius = random.randint(10,70)
    color_line = colors[random.randint(0,4)]
    color_fill = colors[random.randint(0,4)]
    thickness = random.randint(0,radius//2)
        
    
    turtle_.penup()
    turtle_.goto(x,y)
    turtle_.pendown()
    turtle_.width = thickness
    turtle_.color(color_line,color_fill)
    turtle_.begin_fill()
    turtle_.circle(radius)
    turtle_.end_fill()
        

for i in range(10):
    circle(george)
    
    
    
    
    
    
    
    
    
    
    
    
    
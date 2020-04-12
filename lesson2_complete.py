# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 10:19:27 2020

@author: George
"""

#%% while loops - run according to a True or a False
x = 1
while x < 5:
    print('{} is less than 5'.format(x))
    x += 1
    
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
    
#by far the most common time to force break out of a loop is when a condition is met
for number in range(5):
    print(number)
    
for number in range(5):
    print(number)
    if number == 2: 
        break
   
#make a game loop that is a game of rock paper scissors
#ROCK PAPER SCISSORS
import random
running = True
answers = ['rock','paper','scissors']
i = 0
while running:
    #best of three
    if i == 3:
        if score > 0:
            print('You win!')
        elif score == 0:
            print('Its a draw!')
        else:
            print('You lose...')
        running = False
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
    
    i+=1

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


#%% no longer in notbooke 
    #classes and objects - this concept is really important for games
    #each independant thing is an object!
    # a class can be thought of as a template
    
class ClassA:
    #a default speed for all objects of class A
    def __init__(self):
        self.speed = 10
        self.player_type = 'enemy' #class A is for the enemies

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

  def myfunc(abc):
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

# something that can be useful to know is what we call a recurring function!
def factorial_recursive(n):
    # Base case: 1! = 1
    if n == 1:
        return 1

    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial_recursive(n-1)
    
#now n = 3 so we want to run the same code as above until we get to n = 1 this is what will happen if we run:
factorial = factorial_recursive(4)
    

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

# set the speed to the highest setting
george.speed(1)

# draw a square
for i in range(4):
  george.forward(50)
  george.right(90)

# move the turtle
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
    
    
    
    
    
    
    
    
    
    
    
    
    
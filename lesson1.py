# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 09:03:35 2020

Lesson 1 code for techcamp

@author: George
"""

#%%
"""
Whilst explaining the print function explain that python has various primitive functions
Print just works along with some other functions that we will look at later
"""
print("Hello World!")
print('Hello World!')
#print('You died! You're Score was 29.') WONT WORK!
print("You died! You're Score was 29.") #an advantage of using  the double quotes

"""
What we are printing here is known as a string
What if we want to print something else? A number? That will work too
What if we want to print something more complicated with both? - We will work that out later
"""
print("20") #careful! is this a number?
print(20)   #What's the difference?
x = 20
print(x)

#%%
"""
So what is the difference between a string and a number?
Object orientated - no declaring variables. All variables are like objects.
Imagine a box and we put something in it. We label the box and we can then use whatever is in the box by calling the variable name
Like above x = 20. x is now a variable that we put things in, and it is 20.
These are the three primitive types of variable: string, int and float - explain the difference between int and float
"""
x_string = "20"
x_int = 20
x_float = 20.0

#label some more
y_string = "10"
y_int = 10
y_float = 10.0

"""
So what are the basic maths operations that we can do? Try some down below in the IDE command line!
Go through some sums using the variables and use the variable explorer to double check the results!
"""
sum_int = x_int + y_int
#2sum_int = 2*x_int
sum_string = x_string + y_string
#sum_string2 = x_string - y_string wont work
#sum_mix = x_string + x_int wont work
sum_mix = x_int + x_float

"""
How about some more complex operators? Can we spot the difference between these operators
When might the modulus example be useful for a game? Rotating a block in tetris for example?
"""
test_var1 = 15/10
test_var2 = 15%10.0
test_var3 = 15//10

#what about powers or square roots?
print(8**2)
print(8**0.5) #what if we want to just have a symbol for square root so we dont have to remember the powers? Functions! Modules!

"""
We can see that by default if the sum has a float in it that takes priority?
What if we don't want it to? Maths with floating points takes up more memory.
For simple programs we wont notice the speed but imagine we have 1000 lines of code.
If the computer has to store two numbers instead of one for each operation we could make the code twice as fast (or more!)

In this case we can declare variable types if we need to. This is another case of a function that just exists in python
It is part of the language. str,int,float
Examples to talk about (iterating through a range later - it couldnt be a floating point python doesnt know how to do this)
"""
print(int(5+6.0))
print(float(5+6))
print(str(5+6))
print(str(5)+str(6))
#print(int("5"+"6")) wont work! Why not?

"""
Do exercise on summing various strings and formatting them while printing
"""

#%%%
"""
So what about storing multiple variables in the same place?
What if we want a list of names? Or an array of variables?
School register for examples? - exercise of printing whether people are in the class
"""
my_list = [1,2,3,4]
#so what if we want to check what the first item in the list is?
print(my_list[1])

#why did it print the second one? See if anyone can guess why?
print(my_list[0])

#so what if we have a list of names? It works the same
register = ['Hatty','George','Adam','Jane']
#how would we call Jane?
print(register[3])
#what if we don't know the size of the list and we just want the list item?
print(register[-1])
print(register[-2])

#How about adding to the list? We can use one of those pre existing python functions that is just there
register.append('Percy')
print(register[-1])
#so it adds to the end - maybe make an exercise about using a module to add something at the index of their choice!

"""
Append is a really useful function. Especially in a game like snake: when we get a snack we have to append a block to the end of the snakes body!
If we have a huge register of names and we only want to take the first people how would we do it? (ex. by letter?)
Here comes another functions that we can use to find out how long our list is without counting it
We can use slices which we will be using a lot to make out games


Similarly if we have a list of numbers we can use conditions to only select the numbers below 10
"""

register.append(name for name in ['Charlotte','Isobel','Ellie','Ian'])
#What happens if we put those four in a list?
#exercise use pop to do the opposite of append
print(len(register))
reg_length = len(register)
print(register[:])      #what is the point it has just printed the whole thing?
print(register[2:3])    #but this didnt get us two names? Thats how indexing works!
print(register[2:4])    #that's better
#print(register[:reg_length/4]) Why doesn't that work? We need an integer divide. Explain why
print(register[:reg_length//4])

"""
While we're at it one more this for printing
How can we add one of these names into a printed string?
This is when formatting strings comes in handy

We can make todays exercise about making a leaderboard for the game!
i.e. a list of scores of random numbers
"""

#let's print the second name of the list - we can try to randomise selections later
print("Todays top score goes to {}".format(register[0]))

"""
There are other ways to do this but its my preference to do it this way
So are there any other commands that will cause errors in the quotation marks?
How about starting a new line? \n 
But what if we want to have a \n in the string without it breaking the line?
Sometimes we will want this for a path directory
If we all go into the directory we are in and create a file called 'new_file' and look at the directory name can we see a problem that might arise?
"""

print("Today's top score goes to {}. \nThe lowest score goes to {}, better luck next time mate!".format(register[0],register[2]))
#copy in the working directory
#print("The current workin directory is: C:\Users\George\new_file")
print(r"The current working directory is: C:\Users\George\new_file")
#or even better
cwd = r'C:\Users\George\new_file'
print('The cwd is: {}'.format(cwd))

"""
EXERCISES: print a string backwards
    
    
    
    
"""

#%%

"""
How can we use the lists with arithmetic?
Python doesn't see a plus and think ok two numbers it will try to add any two things if it can
We have already seen this with strings adding together
Python is quite a clever language and in general we don't have to tell it too much
We lose some speed but it makes it very readable and quicker to learn
"""
numbers1 = [1,2,3,4,5,6]
numbers2 = [2,4,1,3,6,5]
numbers_sum = numbers1 + numbers2

#it is still acting like a list and not a mathematical array. The computer sees a list of numbers and not an array
#import numpy in the challenges

#but what if we wanted to add all the individual components of the array?
print(dir(__builtin__)) #have a look at our python functions that are built
numbers_sums = [sum(x) for x in zip(numbers1,numbers2)]

#notice in the list the input function - that could be a way of talking to the computer and giving out answers to things

"""
Exercises:
    import numpy and do some maths with these functions
"""

#%%
"""
Two very important words in python are True and False
Lets learn what an if statement is to see why
"""
x = 10
#if x = 10: print('hello') wont work
if x == 10: print('hello')
if x != 10: print('hello') #what is another way of typing out not?
if x == 10:
    print('adding one to x!')
    x = x + 1 #challenge to see if they can shorten this line to += 1 in the challenges
    print('x is now: {}'.format(x))

#this is what the computer is seeing
if True:
    print('This will always run')
elif False:
    print('This will never run')
    
"""
EXERCISES:
    see if a certain letter is in the strings
    
"""
    
"""
here is a quick example of a while and for loop - which we will go into in more detail in the next session
While True - in stretch set a variable to True that will become false after breaking a threshold
"""
#challenge is to see whether this really needs marker or could we put an if statement in the while condition?
#second challenge is to try to remake this have the same functions but print 10,11,12,13,14 not just from 11 onwards!
#third challenge is to see if we can print the product of x and the previous x before it ends: 10*11,11*12,12*13,13*14
x = 10
marker = True
while marker == True:
    x += 1
    if x < 15:
        print(x)
    else:
        marker = False
    
#challenge play around with putting two numbers in range to figure out how it works
#feel free to look up python range function and try to understand how to use it!
#using something called a list comprehension why not try doing the same thing in one line without using the :
#try only printing the numbers divisible by 2 perhaps we could use the modulus function!
for x in range(10):
    print(x)
    
"""
Well done for now that's all the theory - there are some exercise and we'll need every function of python weve seen later on
For now lets try to locate some files in our computer with python
"""

#%%
"""
python is good at reading excel files. If you had a big list of numbers that you wanted to change you could do it all in python
without even opening the file!
Let's try having a look at some photos for now!
We're going to think about flappy bird for example and make some adjustments to photos we might use for the game
"""
import os #say we will focus more on libraries next session
base_directory = os.getcwd() #get current working directory
print(base_directory)
os.listdir()
os.mkdir('Game_pictures')
os.listdir()
games_pic_dir = base_directory + '\\Game_pictures' #remember its a folder!

#%%
import PIL #do we really need to import this whole module?
os.chdir(r'C:\\Users\\George\\Pictures\\Gaming')
#check photos
os.listdir()
thunder = PIL.Image.open('thunder.jpg')
thunder.show()
thunder_dims = thunder.size

thunder_resize = thunder.resize((1920,600))
thunder_resize.show()

"""
this looks warped so lets try cropping the image
The coordinate system starts from the top left
Having a look at it we might want to crop out the bottom half to size 1920,600
crop((left,top,right,bottom))
"""
thunder = thunder.crop((0,thunder_dims[1]-600,thunder_dims[0],thunder_dims[1]))
thunder.show()
os.chdir(games_pic_dir)
thunder.save('thunder_background.png')
#challenge try to save to this directory but without changing it manually
#hint if you include the path of where you would like to save it in the file name it will save in this location!


#%%
"""
But what if we want all our images to be the same size?
Let's make a list of all of our images in the exercise
And then cropping by calling the indexes from our list!
Remember a list can contain any object - even a PIL image object in this case!
"""
city = PIL.Image.open('city.jpg')
sea = PIL.Image.open('sea.jpg')
countryside = PIL.Image.open('countryside.jpg')
backgrounds = [thunder,city,sea,countryside]
"""
How could we split a directory about a certain character or word ? i.e. documents
How could we then use this to go directly to the pictures folder?
Another inbuilt function is known as split
"""

#%%
"""
For our final challenge how about we try playing around with the colours on our python icon.
In our games, as we're using python, we coould use the python log as our player character.
Lets try to change the colours so we can use a different python for every map!
"""

#load the python logo
os.chdir(r'C:\\Users\\George\\Pictures\\Gaming')
python = PIL.Image.open('python.png')
python_size = python.size
python_grey = python.convert('L') #L stands for greyscale

python_grey.show() #perhaps we could use this for a black and white map in a game?
#check the mode of the image - if rgba convert to rgb as we dont need transparency
python = python.convert("RGB") #not nothing will happen if we dont have the equals in there!
r,g,b = python.split()
new_python = PIL.Image.merge("RGB",(b,g,r))
new_python.show()

#give them a list of colour combos and see if they can get a certain 3 colour combos (tbd)

#%%
#for the player we will probably want it a bit smaller than the image
python_small = python.resize((64,64))
python_small.show()
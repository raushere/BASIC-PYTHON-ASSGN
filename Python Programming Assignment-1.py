#!/usr/bin/env python
# coding: utf-8

# # Python Programming Assignment-1

# In[1]:


#1.Write a Python program to print 'Hello Python' ?


print('Hello Python')


# In[5]:


# 2.Write a Python program to do arithmetic operations addition and division ?
num1 = 12
num2 = 4

# Add two numbers
sum = num1 + num2
# division two numbers
div = num1 / num2

# Display the sum
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))

# Display of division
print('The division of {0} by {1} is {2}'.format(num1, num2, div))


# In[6]:


#3.Write a Python program to find the area of a triangle ?

height = int(input('Enter height of triangle: '))
base = int(input('Enter base of triangle: '))

def areaOfTriangle(height, base):
    print('\nArea of triangle ->', 0.5*height*base)

areaOfTriangle(height,base)


# In[7]:


# 4.Write a Python program to swap two variables ?

num_1 = int(input("Enter First Number: "))
num_2 = int(input("Enter Second Number: "))

def swapNumbers(a,b):
    temp = a
    a = b
    b = temp
    return a,b

print('Before swapping -> ',num_1, num_2)
num_1, num_2 = swapNumbers(num_1, num_2)
print('After swapping -> ',num_1,num_2)


# In[9]:


# 5.Write a Python program to generate a random number ?

from random import randint

def generateRandomNumber(start=0, end=100):
    print('Random number -> ',randint(start,end))

# Generating random numbers without arguments    
generateRandomNumber()

# Generating random numbers with arguments    
generateRandomNumber(4,60)


# In[ ]:





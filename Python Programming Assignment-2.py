#!/usr/bin/env python
# coding: utf-8

# # Python Programming Assignment-2

# In[1]:


#1.Write a Python program to convert Kilometers to Miles ?


def km_to_Miles():
    kiloMeters = float(input("Enter no of kilometers : "))
    print("{} km is Equal to {} miles".format(kiloMeters,kiloMeters*0.621))

km_to_Miles()


# In[2]:


# 2.Write a Python program to convert Celsius to Farenheit ?

def cels_to_Farh():
    celsius = int(input("Enter temperature in celsius : "))
    Farenheit = (celsius*(9/5))+32
    print("{}° Celsius is Equal to {}° Farenheit".format(celsius,Farenheit))
    
cels_to_Farh()


# In[3]:


# 3.Write a Python program to display calender ?

import calendar

def displayCalender():
    year = int(input("Enter calender year: "))
    print(calendar.calendar(year))
    
displayCalender()


# In[8]:


# 4.Write a Python program to solve quadartic equation ?

import cmath

a = int(input('Enter a value: '))
b = int(input('Enter b value: '))
c = int(input('Enter c value: '))

# calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))


# In[10]:


# 5. Write a Python program to swap two variables without temp variable ?

x = input('Enter value of x: ')
y = input('Enter value of y: ')

# create a temporary variable and swap the values
temp = x
x = y
y = temp

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))


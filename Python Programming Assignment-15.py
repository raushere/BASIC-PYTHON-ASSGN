#!/usr/bin/env python
# coding: utf-8

# # Python Programming Assignment-15

# 1. Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console ?
# Example:
# If the following n is given as input to the program: 100
# Then, the output of the program should be: 0,35,70

# In[7]:


def showDivisible(in_num):
    for ele in range(0,in_num):
        if (ele%5 == 0) and (ele%7 == 0):
            yield ele
for ele in showDivisible(100):
    print(ele,end=' ')


# 2.Please write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console ?
# Example:
# If the following n is given as input to the program: 10
# Then, the output of the program should be: 0,2,4,6,8,10

# In[8]:


def genEvenNumbers(in_num):
    for ele in range(in_num+1):
        if ele%2 == 0:
            yield ele

for ele in genEvenNumbers(10):
    print(ele,end=' ')


# 3.The Fibonacci Sequence is computed based on the following formula below, Please write a program using list comprehension to print the Fibonacci Sequence in comma separated form with a given n input by console ?
# f(n)=0 if n=0 f(n)=1 if n=1 f(n)=f(n-1)+f(n-2) if n>1

# In[9]:


def genFibonaci(in_num):
    if in_num == 0:
        return 0
    elif in_num == 1:
        return 1
    else:
        return genFibonaci(in_num-1)+genFibonaci(in_num-2)
    
print([genFibonaci(x) for x in range(20)])


# 4.Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the user name of a given email address. Both user names and company names are composed of letters only ?
# Example:
# If the following email address is given as input to the program: john@google.com
# Then, the output of the program should be: john

# In[1]:


def getUsernames():
    in_string = input('Enter Email Address(es): ')
    out_string = in_string.split('@')
    print(f'Username of {in_string} is {out_string[0]}')

for i in range(2):
    getUsernames()


# 5.Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

# In[3]:


class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        return self.length*self.length

square = Square(35)
print(square.area())


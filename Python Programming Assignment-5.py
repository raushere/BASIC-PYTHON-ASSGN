#!/usr/bin/env python
# coding: utf-8

# # Python Programming Assignment-5

# In[26]:


# 1. Write a Python Program to find LCM ?

def findTheLcm(x_term,y_term):
    if x_term > y_term:
        greater = x_term
    else:
        greater = x_term
    while True:
        if((greater%x_term == 0) and (greater%y_term == 0)):
            lcm = greater
            break
        else:
            greater +=1
    print(f'The LCM of {x_term},{y_term} is {lcm}')

findTheLcm(12,4)
findTheLcm(9,7)
findTheLcm(18,24)


# In[27]:


# 2. Write a Python Program to find HCF ?

def findTheHcf(x_term,y_term):
    if x_term>y_term:
        smaller = y_term
    else:
        smaller = x_term
    for ele in range(1,smaller+1):
        if((x_term%ele == 0) and (y_term%ele == 0)):
            hcf = ele
    print(f'The HCF of {x_term},{y_term} is {hcf}')

findTheHcf(16,78)
findTheHcf(10,40)
findTheHcf(23,12)


# In[28]:


# 3. Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal ?

def DecimalToOther():
    num = int(input('Enter a Number: '))
    print(f'Binary Number -> {bin(num)}')
    print(f'Octal Number -> {oct(num)}')    
    print(f'Hexadecimal Number -> {hex(num)}')    

DecimalToOther()


# In[30]:


# 4. Write a Python Program to Find the ASCII value of a Character ?

def charToAscii():
    char = input('Enter a Character: ')
    if len(char) > 1:
        print('Please Enter a Single Character')
    else:
        print(f'Ascii Character of {char} is {ord(char)}')

charToAscii()


# In[33]:


# 5. Write a Python Program to Make a Simple Calculator with 4 Basic Mathematical operations ?

import operator

ops = { "+": operator.add, "-": operator.sub, "*":operator.mul, "/":operator.truediv } 

print('Select a Arithmetic Operation:         \n1.Addition(+)        \n2.Division(-)        \n2.Multiplication(*)        \n4.Division(/)        \n3.Stop(0)\n')
   

while True:
    operator = input('Enter a arithmetic operation -> ')
    if operator == '0':
        print("Program Stopped successfully")
        break
    elif operator not in ['+','-','*','/']:
        print("Please enter a valid operator")
    else:
        num_1 = int(input('\nEnter 1st Number: '))
        num_2 = int(input('Enter 2nd Number: '))
        print(f'{num_1}{operator}{num_2}={ops[operator](num_1,num_2)}\n')


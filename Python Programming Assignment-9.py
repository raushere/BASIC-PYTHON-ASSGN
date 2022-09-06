#!/usr/bin/env python
# coding: utf-8

# # Python Programming Assignment-9

# In[69]:


# 1.Write a Python Program to check if the given number is a Disarium Number ?

def checkDisariumNumber():
    in_num = input('Enter a Number: ')
    sum = 0
    for item in range(len(in_num)):
        sum = sum + int(in_num[item])**(item+1)
    if sum == int(in_num):
        print(f'{in_num} is a Disarium Number')
    else:
        print(f'{in_num} is a Not Disarium Number') 

checkDisariumNumber()


# In[70]:


# 2.Write a Python Program to print all Disarium numbers between 1 to 100 ?

def printDisariumNumbers(start=0,end=100):
    output_num = []
    for number in range(start,end+1):
        sum = 0
        for item in range(len(str(number))):
            sum = sum + int(str(number)[item])**(item+1)
        if sum == number:
            output_num.append(number)
    return output_num
            
        
printDisariumNumbers(1,100)


# In[72]:


# 3.Write a Python Program to check if the given number is Happy Number ?

def checkHappyNumber():
    in_num = input('Enter a Number: ')
    in_num_duplicate = in_num
    trackNumber = set()   
    while True:
        if in_num != '1' and str(in_num) not in trackNumber:
            trackNumber.add(in_num)
            sum = 0
            for ele in range(len((in_num))):
                sum = sum + int(in_num[ele])**2
            in_num = str(sum)
        elif str(in_num) in trackNumber:
            print(f'{in_num_duplicate} is not a Happy Number')
            break
        else:
            print(f'{in_num_duplicate} is a Happy Number')
            break

checkHappyNumber()


# In[73]:


# 4.Write a Python Program to print all Happy numbers between 1 and 100 ?

def checkHappyNumber(start=0,end=100):
    happyNumbersList = []
    for in_num in range(start,end+1):
        in_num = str(in_num)
        inum_holder = in_num
        trackNumber = set()   
        while True:
            if in_num != '1' and str(in_num) not in trackNumber:
                trackNumber.add(in_num)
                sum = 0
                for ele in range(len((in_num))):
                    sum = sum + int(in_num[ele])**2
                in_num = str(sum)
            elif str(in_num) in trackNumber:
                break
            else:
                happyNumbersList.append(int(inum_holder))
                break
    print(f'The Happy Numbers between {start} and {end} are {happyNumbersList}')
    
checkHappyNumber(0,100)


# In[74]:


# 5.Write a Python Program to determine whether the given number is a Harshad Number ?

def checkHarshadNumber():
    in_num = input('Enter a Number: ')
    sum = 0
    for item in range(len(in_num)):
        sum = sum + int(in_num[item])
    if int(in_num)%sum == 0:
        print(f'{in_num} is a Harshad Number')
    else:
        print(f'{in_num} is a Not Harshad Number')
        
checkHarshadNumber()


# In[ ]:





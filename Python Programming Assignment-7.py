#!/usr/bin/env python
# coding: utf-8

# # Python Programming Assignment-7

# In[50]:


# 1. Write a Python Program to find sum of Array ?

def sumOfArray():
    in_arr = eval(input("Enter the Array: "))
    print(f'The sum of {in_arr} is {sum(in_arr)}')

sumOfArray()


# In[51]:


# 2. Write a Python Program to find Largest element in an Array ?

def largestElement():
    in_arr = eval(input("Enter the Array: "))
    print(f"The Largest Element in {in_arr} is {sorted(in_arr, reverse=True)[0]}")
    
largestElement()


# In[52]:


# 3. Write a Python Program for array rotation ?

def reverseOfArray():
    in_arr = eval(input("Enter the Array: "))
    print(f"The Reverse of Array {in_arr} is {in_arr[::-1]}")
    
reverseOfArray()


# In[53]:


# 4. Write a Python Program to Split the array and add the first part to the end ?

def sumOfSplits():
    in_arr = eval(input("Enter the Array: "))
    print(f"The Sum of First and Last Elements of Array {in_arr} is {in_arr[0]+in_arr[-1]}")
    
sumOfSplits()


# In[55]:


# 5. Write a Python Program to check if given array is Monotonic ?

def checkMonotonic():
    in_arr = eval(input("Enter the Array: "))
    if(all(in_arr[i]<=in_arr[i+1] for i in range(len(in_arr)-1)) or all(in_arr[i]>=in_arr[i+1] for i in range(len(in_arr)-1))):
        print(f'Array {in_arr} is Monotonic')
    else:
        print(f'Array {in_arr} is Not Monotonic')

checkMonotonic()
checkMonotonic()


# In[ ]:





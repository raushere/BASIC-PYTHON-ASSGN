#!/usr/bin/env python
# coding: utf-8

# # Python Programming Assignment-10

# In[1]:


# 1.Write a Python Program to find sum of elements in a list ?
def sumofList():
    in_ele = int(input('Enter the No of Entries in a List: '))
    in_list = []
    for itr in range(in_ele):
        in_list.append(int(input('Enter a element: ')))
    print(f'Sum of Elements: {sum(in_list)}')

sumofList()


# In[2]:


# 2.Write a Python Program to multiply all numbers in the list ?
def mulofList():
    in_ele = int(input('Enter the No of Entries in a List: '))
    in_list = []
    mul = 1
    for itr in range(in_ele):
        in_list.append(int(input('Enter a element: ')))
    for ele in in_list:
        mul = mul * ele
    print(mul)

mulofList()


# In[3]:


# 3.Write a Python Program to find smallest number in the list ?
def smallEleInList():
    in_ele = int(input('Enter the No of elements in a list: '))
    in_list = []
    for ele in range(in_ele):
        in_list.append(int(input('Enter a Element: ')))
    print(f'The Smallest Element in {in_list} is {sorted(in_list)[0]}')
smallEleInList()


# In[4]:


# 4.Write a Python Program to find largest number in the list ?
def largestEleInList():
    in_ele = int(input('Enter the No of elements in a list: '))
    in_list = []
    for ele in range(in_ele):
        in_list.append(int(input('Enter a Element: ')))
    print(f'The Largest Element in {in_list} is {sorted(in_list, reverse=True)[0]}')

largestEleInList()


# In[5]:


# 5.Write a Python Program to find second largest number in the list ?
def secondLargestEleInList():
    in_ele = int(input('Enter the No of elements in a list: '))
    in_list = []
    for ele in range(in_ele):
        in_list.append(int(input('Enter a Element: ')))
    print(f'The Second Largest Element in {in_list} is {sorted(in_list, reverse=True)[1]}')

secondLargestEleInList()


# In[7]:


# 6.Write a Python Program to find N largest elements in the list ?
def nLargestEleInList(k):
    in_ele = int(input('Enter the No of elements in a list: '))
    in_list = []
    for ele in range(in_ele):
        in_list.append(int(input('Enter a Element: ')))
    print(f'The {k} Largest Element in {in_list} is {sorted(in_list, reverse=True)[0:k]}')

nLargestEleInList(4)


# In[8]:


# 7.Write a Python Program to find even numbers in the list ?
def evenNoInList():
    in_ele = int(input('Enter the No of elements in a list: '))
    in_list = []
    even_list = []
    for ele in range(in_ele):
        in_list.append(int(input('Enter a Element: ')))
    for ele in in_list:
        if ele%2 == 0:
            even_list.append(ele)
    print(f'The Even Elements in {in_list} are {even_list}')

evenNoInList()


# In[9]:


# 8.Write a Python Program to find odd numbers in the list ?
def oddNoInList():
    in_ele = int(input('Enter the No of elements in a list: '))
    in_list = []
    odd_list = []
    for ele in range(in_ele):
        in_list.append(int(input('Enter a Element: ')))
    for ele in in_list:
        if ele%2 != 0:
            odd_list.append(ele)
    print(f'The Even Elements in {in_list} are {odd_list}')

oddNoInList()


# In[12]:


# 9.Write a Python Program to remove empty list from list ?
def checkEmptyList():
    in_list = eval(input('Enter all elements of the list: '))
    if [] in in_list:
        print(f'There is an Empty list in {in_list} at Position {in_list.index([])}')
        in_list.remove([])
        print(f'The List after removing [] is {in_list}')
    else:
        print(f'There is no [] List in the list {in_list}')
        
checkEmptyList()


# In[14]:


# 10.Write a Python Program to Cloning or Copying a list ?
import copy

def cloneList():
    in_list = eval(input('Enter a list'))
    print(in_list, id(in_list))
    cloned_list = in_list.copy()
    print(cloned_list, id(cloned_list))

cloneList()


# In[15]:


# 11.Write a Python Program to count occurences of an element in a list ?
def checkOccurence():
    in_list = eval(input('Enter the elements of the list: '))
    in_num = eval(input('Enter the element to find: '))
    count = 0
    if in_num in in_list:
        for ele in in_list:
            if ele == in_num:
                count = count+1
    print(f'There are {count} occurences of {in_num} in {in_list}')
    
checkOccurence()


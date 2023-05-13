#!/usr/bin/env python
# coding: utf-8

# # Python Programming Assignment-11

# In[18]:


# 1. Write a Python program to find words which are greater than given length k ?

def checkLengthOfString():
    in_string = input("Enter the string: ")
    in_length = int(input('Enter the length of the string: '))
    out_string = []
    for string in in_string.split(" "):
        if len(string) > in_length:
            out_string.append(string)
    print(','.join(out_string))

checkLengthOfString()


# In[19]:


# 2. Write a Python program for removing i-th character from a string ?
def removeCharacter():
    in_string = input("Enter the String: ")
    in_char_num = int(input("Enter the ith Character: "))
    out_string = ''
    for ele in range(len(in_string)):
        if ele != in_char_num:
            out_string = out_string + in_string[ele]
    print(out_string)
    
removeCharacter()


# In[21]:


# 3. Write a Python program to split and join a string ?

def splitJoinString():
    in_string = input('Enter the string: ')
    print(f"Split String: {in_string.split(' ')}")
    print(f"Join String: {' '.join(in_string.split(' '))}")

splitJoinString()


# In[23]:


# 4. Write a Python to check if a given string is binary string or not ?

def checkBinary():
    in_string = input('Enter the string: ')
    stun = 0
    for ele in in_string:
        if ele in ['0','1']:
            stun = 1
            continue
        else:
            stun = 0
            break
    statement = 'is a binary string' if stun == 1 else 'is not a binart string' 
    print(f'{in_string} {statement}')

checkBinary()
checkBinary()


# In[24]:


# 5. Write a Python program to find uncommon words from two Strings ?

def unCommonWords():
    in_string_1 = set(input("Enter the String 1: ").split(' '))
    in_string_2 = set(input("Enter the String 2: ").split(' '))
    out_string = (in_string_1.union(in_string_2)).difference(in_string_1.intersection(in_string_2))
    print(out_string)

unCommonWords()


# In[26]:


# 6. Write a Python to find all duplicate characters in string ?

def duplicateChars():
    in_string = input('Enter the string: ')
    non_duplicate_list = []
    duplicate_list = []
    for ele in in_string:
        if ele not in non_duplicate_list:
            non_duplicate_list.append(ele)
        else:
            duplicate_list.append(ele)
    print(f'Duplicate characters are: {list(set(duplicate_list))}')
        
duplicateChars()


# In[27]:


# 7. Write a Python Program to check if a string contains any special character?

def checkSpecialChar():
    spl_chars = '[@_!#$%^&*()<>?/\|}{~:]'
    in_num = input('Enter the string: ')
    count = 0
    char_list = []
    for ele in in_num:
        if ele in spl_chars:
            char_list.append(ele)
            count = count+1
    print(f'There are {count} Speical Characters in {in_num} which are {char_list}')
            
        
checkSpecialChar()
checkSpecialChar()


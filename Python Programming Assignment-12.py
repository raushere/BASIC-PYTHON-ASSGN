#!/usr/bin/env python
# coding: utf-8

# # Python Programming Assignment-12

# In[29]:


# 1.Write a Python program to Extract Unique values dictionary values?

in_dict = {1:'saurabh',2:'masoori',3:'ganga',4:'magic',5:'kashmir',6:'love',7:'famous', 8:'somnath'}
print(in_dict.values())
print(f'Unique Values: {list(set(in_dict.values()))}')


# In[30]:


# 2.Write a Python program to find the sum of all items in a dictionary?

in_dict = {'Apple':12,'papaya':5,'orange':50,'blacberry':61,'coconut':35}
print('Sum of All items: ',sum(in_dict.values()))


# In[31]:


# 3.Write a Python program to Merging two Dictionaries?

course_details = {
    'cousre_name':'FDS'
}
instructors = {
    'course_instructors':['sunny','Krish']
}
course_details.update(instructors)
print(course_details)


# In[35]:


# 4.Write a Python program to convert key-values list to flat dictionary?

in_list = [('A',40),('B',30),('C',10),('D',55),('E',10),('F',100),('G',80),('H',70),('I',25),('J',85)]

# Method #1
dict(in_list)


# In[37]:


# 5.Write a Python program to insertion at the beginning in OrderedDict?

from collections import OrderedDict
dict_one = OrderedDict({'Apple':'Iphone','Microsoft':'Windows','Google':'chrome'})
print('dict_one',dict_one)
dict_two = {'Tesla':'SpaceX'}
dict_one.update(dict_two)
print('dict_one',dict_one)
dict_one.move_to_end('Tesla',last=False)
print('dict_one',dict_one)


# In[38]:


# 6.Write a Python program to check order of character in string using OrderedDict()?

from collections import OrderedDict

initial_list = {'a': 1000, 'f': 200, 'd': 300, 'c': 400, 'b': 500, 'e': 600}
print(initial_list)

final_list = OrderedDict(dict(sorted(initial_list.items())))
print(final_list)


# In[39]:


# 7.Write a Python program to sort Python Dictionaries by Key or Value?

d_items = {'Orange':10,'Mango':60,'Blackberry':50,'Grape':25}

def sort_dict(in_dict,sort_type):
    if sort_type == 'key':
        print(dict(sorted(in_dict.items(), key=lambda x:x[0], reverse=False)))
    else:
        print(dict(sorted(in_dict.items(), key=lambda x:x[1], reverse=False)))
        
sort_dict(d_items,'key')        
sort_dict(d_items,'value')


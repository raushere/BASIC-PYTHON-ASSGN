#!/usr/bin/env python
# coding: utf-8

# # Basic Python Assignment-5

# In[ ]:


# 1. What does an empty dictionary&#39;s code look like?
To create an empty dictionary, the dictionary should be set to {}. This is shown in the code below. So, with this code above, we create a dictionary called items which is set equal to {}. 
So this dictionary named items is empty.

# 2. What is the value of a dictionary value with the key foo and the value 42?

dict_values([42])

# 3. What is the most significant distinction between a dictionary and a list?

A list is an ordered sequence of objects, whereas dictionaries are unordered sets. However, the main difference is that
items in dictionaries are accessed via keys and not via their position.

# 4. What happens if you try to access spam[foo] if spam is {bar: 100}?

KeyError: 'foo'

# 5. If a dictionary is stored in spam, what is the difference between the expressions cat in spam and
cat in spam.keys()?

There is no difference. The in operator checks whether a value exists as a key in the dictionary. 'cat' in spam checks whether
there is a 'cat' key in the dictionary, while 'cat' in spam. keys() checks whether there is a key 'cat' for one of the 
keys in spam .

# 6. If a dictionary is stored in spam, what is the difference between the expressions cat in spam and cat in spam.values()?

The in operator checks whether a value exists as a key in the dictionary. 'cat' in spam checks whether there is a 'cat' key 
in the dictionary, while 'cat' in spam. values() checks whether there is a value 'cat' for one of the keys in spam .

# 7. What is a shortcut for the following code?
if color not in spam:
    spam['color'] = 'black'
    
spam = {}
spam['color']='black' if 'color' not in spam else Pass
## short hand if esle statement....

# 8. How do you pretty print dictionary values using which module and function?

Use pprint() to Pretty Print a Dictionary in Python
Within the pprint module there is a function with the same name pprint() , which is the function used to pretty-print the
given string or object. First, declare an array of dictionaries. Afterward, pretty print it using the function pprint.


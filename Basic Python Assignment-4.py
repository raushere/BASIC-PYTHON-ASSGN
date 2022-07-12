#!/usr/bin/env python
# coding: utf-8

# # Basic Python Assignment-4

# In[ ]:


# 1. What exactly is []?

It indiactes empty list. we provide some value inside this to achive our goal.

# 2. In a list of values stored in a variable called spam, how would you assign the value hello as the third value?
(Assume [2, 4, 6, 8, 10] are in spam.)

spam[2] = 'hello'

Lets pretend the spam includes the list ['a','b','c','d'] for the next three queries.

# 3. What is the value of spam[int(int('3'* 2) / 11)]?

spam[3] is d

# 4. What is the value of spam[-1]?

spam[-1] is d

# 5. What is the value of spam[:2]?

spam[:2] is ['a', 'b']

Lets pretend bacon has the list [3.14,cat,11,cat, True] for the next three questions.

# 6. What is the value of bacon.index(cat)?

bacon.index('cat') is 1

# 7. How does bacon.append(99) change the look of the list value in bacon?

[3.14, 'cat', 11, 'cat', True, 99]

# 8. How does bacon.remove(cat) change the look of the list in bacon?

[3.14, 11, 'cat', True, 99]

# 9. What are the list concatenation and list replication operators?

The operator for list concatenation is +, while the operator for replication is *. (This is the same as for strings.)

# 10. What is difference between the list methods append() and insert()?

The only difference between append() and insert() is that insert function allows us to add a specific element at a specified 
index of the list unlike append() where we can add the element only at end of the list.

# 11. What are the two methods for removing items from a list?

The methods are remove(), pop() and clear(). It helps to remove the very first given element matching from the list. 
The pop() method removes an element from the list based on the index given. The clear() method will remove all the elements
present in the list.

# 12. Describe how list values and string values are identical.

The similarity between Lists and Strings in Python is that both are sequences. The differences between them are that firstly,
Lists are mutable but Strings are immutable. Secondly, elements of a list can be of different types whereas a String only
contains characters that are all of String type.

# 13. What's the difference between tuples and lists?

The key difference between the tuples and lists is that while the tuples are immutable objects the lists are mutable.
This means that tuples cannot be changed while the lists can be modified. Tuples are more memory efficient than the lists.

# 14. How do you type a tuple value that only contains the integer 42?

(42,) (The trailing comma is mandatory.)

# 15. How do you get a list value's tuple form? How do you get a tuple value's list form?

Use the list comprehension statement [list(x) for x in tuples] to convert each tuple in tuples to a list. 
This also works for a list of tuples with a varying number of elements.

# 16. Variables that contain list values are not necessarily lists themselves. Instead, what do they contain?

Variables will contain references to list values rather than list values themselves. But for strings and integer values, 
variables simply contain the string or integer value.

# 17. How do you distinguish between copy.copy() and copy.deepcopy()?

copy() create reference to original object. If you change copied object - you change the original object. 
deepcopy() creates new object and does real copying of original object to new one. Changing new deepcopied object 
does not affect original object.


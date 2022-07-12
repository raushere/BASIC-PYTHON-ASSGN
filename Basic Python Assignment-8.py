#!/usr/bin/env python
# coding: utf-8

# # Basic Python Assignment-8

# In[ ]:


# 1. Is the Python Standard Library included with PyInputPlus?

No. PyInputPlus is a third-party module and doesn’t come with the Python Standard Library.

# 2. Why is PyInputPlus commonly imported with import pyinputplus as pypi?

This optionally makes your code shorter to type: you can type pyip.inputStr() instead of pyinputplus.inputStr().

# 3. How do you distinguish between inputInt() and inputFloat()?

The inputInt() function returns an int value, whereas the inputFloat() function returns a float value. This is the difference between returning 5 and 5.0.

# 4. Using PyInputPlus, how do you ensure that the user enters a whole number between 0 and 99?

Call pyip.inputint(min=0, max=99).

# 5. What is transferred to the keyword arguments allowRegexes and blockRegexes?

A list of regex strings that are either explicitly allowed or denied

# 6. If a blank input is entered three times, what does inputStr(limit=3) do?

A list of regex strings that are either explicitly allowed or denied

#7. If blank input is entered three times, what does inputStr(limit=3, default='hello') do?

The function returns the value 'hello'.


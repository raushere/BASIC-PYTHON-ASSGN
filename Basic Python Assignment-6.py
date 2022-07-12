#!/usr/bin/env python
# coding: utf-8

# # Assignment_6

# In[ ]:


# 1. What are escape characters, and how do you use them?

In Python strings, the backslash "\" is a special character, also called the "escape" character. It is used in representing 
certain whitespace characters: "\t" is a tab, "\n" is a newline, and "\r" is a carriage return. Conversely, prefixing a
special character with "\" turns it into an ordinary character.

# 2. What do the escape characters n and t stand for?

In Python strings, the backslash "\" is a special character, also called the "escape" character. It is used in representing 
certain whitespace characters: "\t" is a tab, "\n" is a newline, and "\r" is a carriage return.

# 3. What is the way to include backslash characters in a string?
Use the syntax "\\" within the string literal to represent a single backslash.

# 4. The string &quot;Howl's Moving Castle&quot; is a correct value. Why isn't the single quote character in the
get_ipython().set_next_input('word Howl is not escaped a problem');get_ipython().run_line_magic('pinfo', 'problem')

The single quote in Howl's is fine because you've used double quotes to mark the beginning and end of the string.

# 5. How do you write a string of newlines if you don't want to use the n character?

Just use \n ; Python automatically translates that to the proper newline character.

# 6. What are the values of the given expressions?

'Hello, world'[1] -- 'e'
'Hello, world'[0:5] -- 'Hello'
'Hello, world'[:5] -- 'Hello'
'Hello, world'[3:] -- 'lo, world'

# 7. What are the values of the following expressions?

'Hello'.upper() -- 'HELLO'
'Hello'.upper().isupper() -- True
'Hello'.upper().lower() -- 'hello'

# 8. What are the values of the following expressions?

'Remember, remember, the fifth of July.'.split()

['Remember,', 'remember,', 'the', 'fifth', 'of', 'July.']

'-'.join('There can only one.'.split())

'There-can-only-one.'

# 9. What are the methods for right-justifying, left-justifying, and centering a string? 

Python String contains two built-in methods to provide the left and right justification.
Python String ljust() function. Python String ljust() function accepts the character for padding it to the input string.
Python String rjust() function.

# 10. What is the best way to remove whitespace characters from the start or end?

String. Trim() removes all whitespace from the beginning and end of a string.


#!/usr/bin/env python
# coding: utf-8

# # Basic Python Assignment-3

# In[ ]:


# 1. Why are functions advantageous to have in your programs?

There used to be some part of code that is been used number of time so instead of writing the same code multiple times 
we can create a function of it and use it when ever necessary so that we can avoid the repeation of code which makes program more compact.

# 2.When does the code in a function run: when it specified or when it is called?
    
when the function is called by passing the parameters.

# 3. What statement creates a function?

def make(n):

Here make is function name and n is parameter.

# 4. What is the difference between a function and a function call?

function is lines of code that execute upon calling.
function call is the way the programmer make utilse of the function by calling it in the main program.

# 5. How many global scopes are there in a Python program? How many local scopes?

Ther is only one global scople and local scope is a nested function within a enclosed function and number of local scope 
can be formed.

# 6. What happens to variables in a local scope when the function call returns?

When the execution of the function call returns, the local variables are destroyed.

# 7. What is the concept of a return value? Is it possible to have a return value in an expression?

After the execution of a function it return a value(end result after the execution).

Yes it is possible to return a expression as a return value.

# 8. If a function does not have a return statement, what is the return value of a call to that function?

A function without an explicit return statement returns None.

# 9. How do you make a function variable refer to the global variable?

If you want to refer to a global variable in a function, you can use the global keyword to declare which variables are global.

#10. What is the data type of None?

The None keyword is used to define a null value, or no value at all. None is not the same as 0, False, or an empty string. 
None is a data type of its own (NoneType) and only None can be None.

# 11. What does the sentence import areallyourpetsnamederic do?

That import statement imports a module named areallyourpetsnamederic. it gives error for not having this python module.

# 12. If you had a bacon() feature in a spam module, what would you call it after importing spam?
                                                                       
This function can be called with spam. bacon().

# 13. What can you do to save a programme from crashing if it encounters an error?

When it encounters an error, the control is passed to the except block, skipping the code in between. 
As seen in the above code, we have moved our code inside a try and except statement. Try running the program and 
it should throw an error message instead of crashing the program.

# 14. What is the purpose of the try clause? What is the purpose of the except clause?

The try block is used to check some code for errors i.e the code inside the try block will execute when there is no error 
in the program. Whereas the code inside the except block will execute whenever the program encounters some error in 
the preceding try block and prevent from crashing the program.


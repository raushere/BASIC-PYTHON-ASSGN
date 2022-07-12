#!/usr/bin/env python
# coding: utf-8

# # Basic Python Assignment-24
# 1. What is the relationship between def statements and lambda expressions ?

Ans: def statement is used to create a normal function. where as lamba expressions are used to create Anonymous functions. which can be assigned to a variable and can be called using the variable later in function.

Lambda's body is a single expression and not a block of statements like def statement. The lambda expression's body is similar to what we'd put in a def body's return statement. We simply type the result as an expression instead of explicitly returning it. Because it is limited to an expression, a lambda is less general than a def statement.# 2. What is the benefit of lambda?

Ans: The following are some of the benefits of lambda expressions:

(a)Can be used to create Nameless/Anonymous functions inside some complex functions if we are planning to use it only once.

(b)Moderate to small functions can be created in a single line.

(c)Fuctions created using lambda expressions can be assigned to a variable and can be used by simply calling the variable.# 3. Compare and contrast map, filter, and reduce.

Ans: The differences between map, filter and reduce are:

(a)map(): The map() function is a type of higher-order. This function takes another function as a parameter along with a sequence of iterables and returns an output after applying the function to each iterable present in the sequence.

(b)filter(): The filter() function is used to create an output list consisting of values for which the function returns true.

(c)reduce(): The reduce() function, as the name describes, applies a given function to the iterables and returns a single value# 4. What are function annotations, and how are they used?

Ans: Function annotations provide a way of associating various parts of a function with arbitrary python expressions at compile time.
Annotations of simple parameters def func(x: expression, y: expression = 20):
Whereas the annotations for excess parameters are as − def func (**args: expression, **kwargs: expression):# 5. What are recursive functions, and how are they used?

Ans: A recursive function is a function that calls itself during its execution. The process may repeat several times, outputting the result and the end of each iteration.# 6. What are some general design guidelines for coding functions?

Ans: Some of the general design guidelines for coding functions are:

(a)Always use a docstring to explain the functionality of the function.
(b)Avoid using or limited use of global variables.
(c)Proper Identation to increase the code readability.
(d)Try to follow a naming convention for function names and stick with the same convention throughout the application.
(e)Avoid using digits while choosing a variable name.
(f)Try to use a name for the function which conveys the purpose of the function.# 7. Name three or more ways that functions can communicate results to a caller.

Ans: Some of the ways in which a function can communicate with the calling function is:

(a)Print
(b)Return
(c)Yield
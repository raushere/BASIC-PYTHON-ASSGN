#!/usr/bin/env python
# coding: utf-8

# # Basic Python Assignment-2

# In[ ]:


#1.What are the two values of the Boolean data type? How do you write them?

It has two possible values: True and False 
    
#2. What are the three different types of Boolean operators?
    
AND, OR, NOT 

#3. Make a list of each Boolean operator's truth tables (i.e. every possible combination of Boolean values for 
#the operator and what it evaluate ).

TRUTH TABLE :
AND             
A   B   Q    
0   0   0   
0   1   0    
1   0   0    
1   1   1

OR 
0   0   0   
0   1   1    
1   0   1    
1   1   1
NOT
A   B
0   1      
1   0       

'''
4.What are the values of the following expressions?
a. (5 > 4) and (3 == 5)
b. not (5 > 4)
c.  (5 > 4) or (3 == 5)
d. not ((5 > 4) or (3 == 5))
e. (True and True) and (True == False)
f. (not False) or (not True)
'''
a. False
b. False
c. True
d. False
e. False
f. True

#5. What are the six comparison operators?

1 ==
2 >=
3 <=
4 >
5 <
6 !=

#6. How do you tell the difference between the equal to and assignment operators?Describe a condition and 
#when you would use one.

1. with single equal sign right side value is assigned to the left side variable

EX :- Y = 20 .here 20 is assigned to Y .

2. with double == sign the values on the either side are compared for equality

5==9

Here we get False.

#7. Identify the three blocks in this code:

spam = 0
if spam == 10: -- first block
print('eggs')
if spam > 5:  -- second block
print('bacon')
else:         -- third block
print('ham')
print('spam')
print('spam')

#8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! 
#if anything else is stored in spam.

inp = int(input("Enter the number: "))

if inp == 1:
    print("HELLO")
elif: inp == 2:
        print("Howdy")
else:
    print("Greetings!")

#9.If your programme is stuck in an endless loop, what keys you’ll press?

You can stop an infinite loop with CTRL + C

#10. How can you tell the difference between break and continue?

break : for break the loop is skiped permanently
continue : for continue the remaining part of code is skipped and the exection start from next iteration

#11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?

range(10) : Here the iteration start from 0 as default and end at 9
range(0,10): Here the starting iteration 0 is intentionally mentioned though it start from 0.
range(0,10,1):Here everthing is same but step change is 1 though as default it is already 1 by default

On whole there is no differnce in the output

#12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program 
that prints the numbers 1 to 10 using a while loop.

for i in range(1,11):
    print(i)

i = 1 
while i<=10:
    print(i)
    i += 1

#13. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?

import spam
spam.bacon()

example:
import math
math.sqrt()


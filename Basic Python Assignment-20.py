#!/usr/bin/env python
# coding: utf-8

# # Basic Python Assignment-20

# In[1]:


#1. Set the variable test1 to the string 'This is a test of the emergency text system,' and save test1 to a file named test.txt.
test1 = 'This is a test of the emergency text system,'
print(test1)
with open('test.txt','w') as file:
    file.write(test1)
    file.close()


# In[2]:


get_ipython().system(' type test.txt ')


# In[3]:


#2. Read the contents of the file test.txt into the variable test2. Is there a difference between test 1 and test 2?
with open('test.txt','r') as file:
    test2 = file.read()
    
print(test2)   
print(test1 == test2)


# In[4]:


''' 3. Create a CSV file called books.csv by using these lines:
title,author,year
The Weirdstone of Brisingamen,Alan Garner,1960
Perdido Street Station,China Miéville,2000
Thud!,Terry Pratchett,2005
The Spellman Files,Lisa Lutz,2007
Small Gods,Terry Pratchett,1992 '''

data = '''title,author,year
The Weirdstone of Brisingamen,Alan Garner,1960
Perdido Street Station,China Miéville,2000
Thud!,Terry Pratchett,2005
The Spellman Files,Lisa Lutz,2007
Small Gods,Terry Pratchett,1992'''

with open('books.csv','w') as file:
    file.write(data)


# In[5]:


#4. Use the sqlite3 module to create a SQLite database called books.db, and a table called books with these fields: title (text), author (text), and year (integer).
import sqlite3
db = sqlite3.connect('books.db')
cursor = db.cursor()
cursor.execute("CREATE TABLE books (title text, author text, year int)")
db.commit()
db.close()


# In[6]:


# 5. Read books.csv and insert its data into the books table.
import sqlite3
import csv
conn = sqlite3.connect("books.db")
cursor = conn.cursor()
with open("books.csv","r") as file:
    books = csv.DictReader(file)
    for book in books:
        cursor.execute("INSERT INTO books VALUES (?,?,?)",(book['title'],book['author'],book['year']))
conn.commit()
conn.close()


# In[7]:


# 6. Select and print the title column from the books table in alphabetical order.
import sqlite3
conn = sqlite3.connect('books.db')
cursor = conn.cursor()
output = cursor.execute("SELECT title FROM books ORDER BY title ASC")
for ele in output:
    print(ele[0])
conn.commit()
conn.close()


# In[25]:


# 7. From the books table, select and print all columns in the order of publication.
import sqlite3
conn = sqlite3.connect('books.db')
cursor = conn.cursor()
ouput = cursor.execute("SELECT * FROM books ORDER BY year")
for record in ouput:
    print(record)


# In[26]:


# 8. Use the sqlalchemy module to connect to the sqlite3 database books.db that you just made in exercise 6.
import sqlalchemy
conn = sqlalchemy.create_engine('sqlite:///books.db')
conn


# In[22]:


# 9. Install the Redis server and the Python redis library (pip install redis) on your computer. Create a Redis hash called test with the fields count (1) and name ('Fester Bestertester'). Print all the fields for test.
get_ipython().system(' pip install redis3')


# In[40]:


import redis
conn = redis.Redis()
conn.hset('test',{'count':1,'name':'Fester Bestertester'})
conn.hgetall("test")

#unable to get output always showing error


# In[37]:


#10. Increment the count field of test and print it.
conn.hincrby('test', 'count', 1)
conn.hget('test', 'count')

#unable to get output always showing error


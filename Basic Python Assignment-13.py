#!/usr/bin/env python
# coding: utf-8

# # Basic Python Assignment-13

# In[ ]:



get_ipython().set_next_input('1. What advantages do Excel spreadsheets have over CSV spreadsheets');get_ipython().run_line_magic('pinfo', 'spreadsheets')

Ans: The Advantages of Excel over CSV are:

    Excel (XLS and XLSX) file formats are better for storing and analysing complex data.
    An Excel not only stores data but can also do operations on the data using macros, formulas etc
    CSV files are plain-text files, Does not contain formatting, formulas, macros, etc. It is also known as flat files

get_ipython().set_next_input('2.What do you pass to csv.reader() and csv.writer() to create reader and writer objects');get_ipython().run_line_magic('pinfo', 'objects')

import csv
with open('text.csv','r') as file:
    csv_file = csv.reader(file,delimiter=',')
    for ele in csv_file:
        print(ele)

['name,department,birthday month']
['John Smith,Accounting,November']
['Erica Meyers,IT,March']

get_ipython().set_next_input('3. What modes do File objects for reader and writer objects need to be opened in');get_ipython().run_line_magic('pinfo', 'in')

Ans: For csv.reader(iterable_file_object), the file objects needed to be opened in read mode mode='r' Whereas for csv.writer(iterable_file_object) the file objects needed to be opened in write mode mode='w'
get_ipython().set_next_input('4. What method takes a list argument and writes it to a CSV file');get_ipython().run_line_magic('pinfo', 'file')

Ans: csv.writer class provides two methods for writing to CSV. They are writerow() and writerows(). writerow() method writes a single row at a time. Whereas writerows() method is used to write multiple rows at a time.

# Example Program
import csv      
fields = ['Name', 'Branch', 'Year', 'CGPA'] #column names 
rows = [ 
            ['Nikhil', 'COE', '2', '9.0'],  # data rows of csv file 
            ['Sanchit', 'COE', '2', '9.1'], 
            ['Ravi', 'IT', '2', '9.3']
       ] 
with open("university_records.csv", 'w') as csvfile: 
    csvwriter = csv.writer(csvfile) # creating a csv writer object 
    csvwriter.writerow(fields) # writing the fields 
    csvwriter.writerows(rows) # writing the data rows 

get_ipython().set_next_input('5. What do the keyword arguments delimiter and line terminator do');get_ipython().run_line_magic('pinfo', 'do')

Ans: Lets take the example of a csv file:
First Name, Last Name, Age
Mano, Vishnu, 24
Vishnu, Vardhan, 21
Here ',' is Delimiter. We can use any Character as per our needs if required. Similarly Line Terminator comes at end of line by default it is newline and can be changed accourding to Requirement.
get_ipython().set_next_input('6. What function takes a string of JSON data and returns a Python data structure');get_ipython().run_line_magic('pinfo', 'structure')

Ans: loads() method takes a string of JSON data and returns a Python data structure

# Example of json.loads() method
import json
my_details_json ='''{
    "Name": "Mano Vishnu",
    "Qualification": "Bachelor of Technology",
    "Stream": "Computer Science and Engineering"
}'''
print(my_details_json)
print(f'Type of my_details_json is {type(my_details_json)}')
my_details = json.loads(my_details_json)
print(my_details)
print(f'Type of my_details is {type(my_details)}')

{
    "Name": "Mano Vishnu",
    "Qualification": "Bachelor of Technology",
    "Stream": "Computer Science and Engineering"
}
Type of my_details_json is <class 'str'>
{'Name': 'Mano Vishnu', 'Qualification': 'Bachelor of Technology', 'Stream': 'Computer Science and Engineering'}
Type of my_details is <class 'dict'>

get_ipython().set_next_input('7. What function takes a Python data structure and returns a string of JSON data');get_ipython().run_line_magic('pinfo', 'data')

Ans: dumps() method takes a python data structure and returns a string of JSON data

# Example of json.dumps() method
import json
my_details = {
    'Name':'Mano Vishnu',
    'Stream':'Computer Science and Engineering',
    'Qualification':'Bachelor of Technology'
}
print(my_details)
print(f'Type of my_details is {type(my_details)}')
my_details_json = json.dumps(my_details, indent=4, sort_keys=True)
print(my_details_json)
print(f'Type of my_details_json is {type(my_details_json)}')

{'Name': 'Mano Vishnu', 'Stream': 'Computer Science and Engineering', 'Qualification': 'Bachelor of Technology'}
Type of my_details is <class 'dict'>
{
    "Name": "Mano Vishnu",
    "Qualification": "Bachelor of Technology",
    "Stream": "Computer Science and Engineering"
}
Type of my_details_json is <class 'str'>


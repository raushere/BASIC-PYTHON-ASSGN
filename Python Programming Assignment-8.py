#!/usr/bin/env python
# coding: utf-8

# # Python Programming Assignment-8

# In[58]:


# 1. Write a Python Program to Add two Matrices ?

def addMatrices(a,b):
    print(f'Inputs: {a},{b}')
    if len(a) == len(b):
        out_matrix = []
        for ele in range(len(a)):
            if len(a[ele]) == len(b[ele]):
                out_matrix.append([])
                for sub_ele in range(len(a[ele])):
                    out_matrix[ele].append(a[ele][sub_ele]+b[ele][sub_ele])
            else:
                print('Both Matrices must contains same no of rows and columns') 
    else:
        print('Both Matrices must contains same no of rows and columns')
    print(f'Output: {out_matrix}')

addMatrices([[1,2,3],[2,5,6],[7,1,9]],[[9,3,7],[6,5,4],[3,2,1]])


# In[60]:


# 2. Write a Python Program to Multiply two Matrices ?

a = [[2,2,5],[4,8,1],[3,2,7]]
b = [[2,7,6],[4,9,1],[3,1,8]]

def multiply_matrice(a,b):
    output = []
    if len(a[0]) == len(b):
        for ele in range(len(a[0])):
            output.append([0 for ele in range(len(b[0]))])
        for i in range(len(a)):
            for j in range(len(b[0])):
                for k in range(len(b)):
                    output[i][j] += a[i][k]*b[k][j]
        print(output)     
    else:
        print('Matrix Multiplication is Not Possible')
        
multiply_matrice(a,b)


# In[63]:


# 3. Write a Python Program to transpose a Matrix ?

a = [[1,2,1],[4,5,6],[7,8,9]]
b = [[1,2],[4,4],[7,8]]
c = [[1,2,3],[7,5,6]]

def generate_transpose(in_matrix):
    out_matrix = []
    for ele in range(len(in_matrix[0])):
        out_matrix.append([0 for i in range(len(in_matrix))])
    for i in range(len(in_matrix)):
        for j in range(len(in_matrix[i])):
            out_matrix[j][i] = in_matrix[i][j]
    print(f'{in_matrix} ---> {out_matrix}')
        
generate_transpose(a)
generate_transpose(b)
generate_transpose(c)


# In[66]:


# 4. Write a Python Program to sort Words in an Alphabatical Order ?

def sortString():
    in_string = input("Enter a String: ").title()
    sorted_list = sorted(in_string.split(' '))
    print(' '.join(sorted_list))

sortString()


# In[68]:


# 5. Write a Python Program to remove Punctuations From a String ?

def removePunctuatuions():
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    in_string = input('Enter a String: ')
    out_string = ''
    for ele in in_string:
        if ele not in punctuations:
            out_string += ele
    print(out_string)
    
removePunctuatuions()


# In[ ]:





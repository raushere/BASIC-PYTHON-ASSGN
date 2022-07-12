#!/usr/bin/env python
# coding: utf-8

# # Basic Python Assignment-19

# In[9]:


#1. Make a class called Thing with no contents and print it. Then, create an object called example from this class and also print it. Are the printed values the same or different?
class Thing:
    pass

print(Thing)

example = Thing()
print(example)


# In[10]:


#2. Create a new class called Thing2 and add the value 'abc' to the letters class attribute. Letters should be printed.
class Thing2:
    letters = 'abc'
    
print(Thing2.letters)


# In[12]:


#3. Make yet another class called, of course, Thing3. This time, assign the value 'xyz' to an instance (object) attribute called letters. Print letters. Do you need to make an object from the class to do this?
class Thing3:    
    def __init__(self):
        self.letters = 'xyz'
        
try:        
    print(Thing3.letters) # Will raise a syntax Error
except:
    newthing = Thing3()
    print(newthing.letters)


# In[13]:


#4. Create an Element class with the instance attributes name, symbol, and number. Create a class object with the values 'Hydrogen,' 'H,' and 1.
class Element:   
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

my_elements = Element('Hydrogen','H',1)


# In[14]:


#5. Make a dictionary with these keys and values: 'name': 'Hydrogen', 'symbol': 'H', 'number': 1. Then, create an object called hydrogen from class Element using this dictionary.
custom_dict = {'name':'Hydrogen','symbol':'H','number':1}
print(custom_dict)

# Method 1
hydrogen = Element(*custom_dict.values())
print('Using Method #1 ->',hydrogen.name,hydrogen.symbol,hydrogen.number, sep='\t')

# Method 2
hydrogen = Element(**custom_dict)
print('Using Method #2 ->',hydrogen.name,hydrogen.symbol,hydrogen.number, sep='\t')


# In[15]:


#6. For the Element class, define a method called dump() that prints the values of the object’s attributes (name, symbol, and number). Create the hydrogen object from this new definition and use dump() to print its attributes.
class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number      
    def dump(self):
        print(self.name, self.symbol, self.number)
        
hydrogen = Element('Hydrogen','H',1)
hydrogen.dump()


# In[16]:


#7. Call print(hydrogen). In the definition of Element, change the name of method dump to __str__, create a new hydrogen object, and call print(hydrogen) again.
print(hydrogen)

class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number      
    def __str__(self):
        return f'{self.name} {self.symbol} {self.number}'
        
Hydrogen = Element('Hydrogen','H',1)
print(Hydrogen)


# In[17]:


#8. Modify Element to make the attributes name, symbol, and number private. Define a getter property for each to return its value.
class Element:
    def __init__(self,name,symbol,number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number
    
    @property
    def get_name(self):
        return self.__name
    
    @property
    def get_symbol(self):
        return self.__symbol
    
    @property
    def get_number(self):
        return self.__number
    
hydrogen = Element('Hydrogen','H',1)
print(hydrogen.get_name)
print(hydrogen.get_symbol)
print(hydrogen.get_number)


# In[18]:


#9. Define three classes: Bear, Rabbit, and Octothorpe. For each, define only one method: eats(). This should return 'berries' (Bear), 'clover' (Rabbit), or 'campers' (Octothorpe). Create one object from each and print what it eats.
class Bear:
    def eats(self):
        print('berries')
class Rabbit:
    def eats(self):
        print('clover')
class Octothorpe:
    def eats(self):
        print('campers')
        
bear = Bear()
rabbit = Rabbit()
octothrope = Octothorpe()

bear.eats()
rabbit.eats()
octothrope.eats()


# In[19]:


#10. Define these classes: Laser, Claw, and SmartPhone. Each has only one method: does(). This returns 'disintegrate' (Laser), 'crush' (Claw), or 'ring' (SmartPhone). Then, define the class Robot that has one instance (object) of each of these. Define a does() method for the Robot that prints what its component objects do.
class Laser:
    def does(self):
        return 'disintegrate'
class Claw:
    def does(self):
        return 'crush'
class Smartphone:
    def does(self):
        return 'ring'
class Robot:
    def __init__(self):
        self.laser = Laser()
        self.claw = Claw()
        self.smartphone = Smartphone()
    def does(self):
        print(self.laser.does(),self.claw.does(),self.smartphone.does())
        
r2d2 = Robot()
r2d2.does()


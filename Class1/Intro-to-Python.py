#!/usr/bin/env python
# coding: utf-8

# # Introduction to Python
# 
# ## Python Basics
#  Reference for further reading: https://automatetheboringstuff.com/chapter1/

# ### Expressions

# In[11]:


3 + 5


# In[17]:


3 + 'a'


# In[18]:


str(3) + 'a'


# In[19]:


f"3a"


# In[20]:


3 * 'a'


# ### Variable Assignment

# In[35]:


grade = 89.3


# In[30]:


grade


# In[36]:


grade += 5


# In[37]:


grade


# ## Control Flow
# - NOTE: Booleans in Python are True and False, not TRUE and FALSE (as in R)
# - NOTE: Indentation, not {} indicate groups of lines in Python
# - Reference for further reading: https://automatetheboringstuff.com/chapter2/

# ### If-else Logic

# In[39]:


if 90 <= grade:
    print('A')
elif 80 <= grade < 90:
    print('B')
elif 70 <= grade < 80:
    print('C')
else:
    print('F')


# ### While Loop

# In[43]:


number_students_enrolled = 0

while number_students_enrolled < 30:
    number_students_enrolled += 1
else:
    # Prints after the while-loop finishes:
    print(number_students_enrolled)


# In[47]:


number_students_enrolled = 0

while True:
    number_students_enrolled += 1
    if number_students_enrolled == 30:
        break
else:
    print(number_students_enrolled)


# Why does the `print()` statement not get executed?

# ### For Loop

# In[53]:


for i in range(5):
    print(i * '*')
else:
    print("For-loop finished.")


# Note: `range()` includes lower bound, but *not* upper bound.

# In[54]:


for j in range(-5, 3, 2):
    print(j)


# ## Functions
# Reference for further reading: https://automatetheboringstuff.com/chapter3/

# ### Defining Functions

# In[61]:


def my_awesome_function():
    print("Hi!")
    print("How are you?")


# In[63]:


my_awesome_function()
my_awesome_function()


# In[68]:


def my_awesome_function(x):
    """Example of function with parameters."""
    print(f"Initial value: {x}")
    print(f"Previous value: {x - 1}")
    print(f"Next value: {x + 1}")


# In[67]:


my_awesome_function(3)


# In[69]:


def my_awesome_function(x):
    """Example of function with parameters and return statement."""
    return x + 2


# In[70]:


my_awesome_function(7)


# ### Local and Global Scope

# Global scope cannot access local variables:

# In[77]:


def my_awesome_function(x):
    """Example of function where y is in local scope."""
    y = x + 2
    return y


# In[75]:


my_awesome_function(7)


# In[78]:


y


# Variables in different scopes can have same name:

# In[81]:


# y is in global and local scopes:
y = 3
print(my_awesome_function(7))
y


# Additional caveats about scoping:
# - A function's local scope *can* access variables defined in global scope. But it's not good practice to do so, because it's harder to debug.
# - A function's local scope *cannot* access variables defined in another function's local scope. 
# 

# ### Exception Handling

# In[84]:


def my_awesome_function(x):
    """Example of error handling."""
    try:
        y = x + 2
    except TypeError:
        print("Error: Invalid argument for x -- numeric input expected.")


# In[85]:


my_awesome_function('a')


# 10 minute break

# ## Python Types
# Reference for further reading: https://automatetheboringstuff.com/chapter4/ and https://data-flair.training/blogs/python-data-structures-tutorial/

# In[88]:


print(type(3))
print(type(3.0))


# ### Lists

# In[90]:


[1, 3, 'abc', True, [2, 3]]


# ![Slice notation explained](slice_notation_explained.jpg)
# 
# [Reference](https://stackoverflow.com/questions/509211/understanding-pythons-slice-notation)
# 
# Note: range includes lower bound, but not upper bound.
# 
# `Name = ['F', 'u', 'd', 'g', 'e']`

# In[147]:


Name = ['F', 'u', 'd', 'g', 'e']


# In[148]:


len(Name)


# In[149]:


Name[0] = 'Sm'
Name


# In[150]:


[Name[0]] + ['i'] + Name[2:5]


# In[151]:


# Recall: Name = ['Sm', 'u', 'd', 'g', 'e']
del Name[2]
Name


# In[152]:


for i in range(len(Name)):
    print(Name[i])


# In[153]:


for letter in Name:
    print(letter)


# In[154]:


'F' in Name


# In[155]:


'F' not in Name


# In[156]:


x1, x2, x3 = [1, 2, 3]
print(f"{x1} {x2} {x3}")


# In[157]:


# Recall: Name = ['Sm', 'u', 'g', 'e']
Name.index('g')


# In[158]:


Name.append('d')
Name


# In[159]:


Name.insert(2, 'd')
Name


# In[160]:


# Caution: only first value is removed, if duplicates are present:
Name.remove('d')
Name


# In[162]:


Name.sort()
Name


# In[163]:


Name.sort(key=str.lower)
Name


# **Caution:** `sort()` method sorts in-place, which means that the function returns `None`. A common bug is assigning output of `sort()` to another variable that you then operate on -- but it's value is now `None` (!).

# ### Strings

# In[165]:


Name_string = 'Fudge'


# In[168]:


Name_string[2:-1]


# In[169]:


"F" in Name_string


# In[170]:


for letter in Name_string:
    print(letter)


# Note: strings are **not mutable**, i.e. you can't update a string, but you can create a new one:

# In[171]:


Name_string[0] = "Sm"


# In[175]:


Name_string[0] + 'i' + Name_string[2:5] + 't'


# ### Tuples
# Tip: Use tuples to signal to someone reading your code that this variable will not change in the code base.

# In[176]:


Name_tuple = ('F', 'u', 'd', 'g', 'e')


# Note: tuples are also **not mutable**, i.e. you can't update a string, but you can create a new one:

# In[177]:


Name_tuple[0] = "Sm"


# In[180]:


print(type(('abc',)))


# In[184]:


tuple([1, 2, 3])


# In[182]:


# Recall: Name_string = 'Fudge'
tuple(Name_string)


# In[183]:


list(Name_tuple)


# In[210]:


y1, y2, y3 = tuple([4, 5, 6])
print(f"{y1} {y2} {y3}")


# ### Sets
# Sets are **mutable** tuples with unique entries that allow set operations.

# In[203]:


set([2, 1, 'abc', '4a', 2])


# In[221]:


Name_set = set(Name)
Name_set


# In[222]:


Name_set - set(list('Fudge'))


# In[223]:


Name_set.intersection(set(list('Fudge')))


# In[224]:


Name_set.union(set(list('Fudge')))


# In[225]:


# Drop the first element of set:
Name_set.pop()


# ### Dictionaries
# Dictionaries are:
# - Made of key-value pairs
# - Unordered, i.e. there's no "first" dictionary element
# - It's O(1) operation for accessing items in list, vs. O(n) for a list.
# 
# Reference for further reading: https://automatetheboringstuff.com/chapter5/

# In[231]:


dictionary1 = {'key1': 'value1',
               'key2': 'value2'
              }
dictionary2 = {'key2': 'value2',
               'key1': 'value1'
              }
dictionary1 == dictionary2


# In[233]:


course_information = {'name': 'Statistical Computing and Programming',
                      'number': 404,
                      'instructor': 'Irina Kukuyeva',
                      'TA': 'Hao Wang'
                     }


# In[234]:


course_information['name']


# In[236]:


course_information['Room'] = 'PAB 1749'


# In[240]:


f"Welcome to Stats {course_information['number']}: {course_information['name']}"


# In[241]:


course_information.keys()


# In[242]:


course_information.values()


# In[243]:


course_information.items()


# In[245]:


'names' in course_information.keys()


# In[238]:


course_information.get('names', 'Missing Name')


# 10 minute break

# ## Passing by Reference (Python) vs Passing by Value (R)
# **Note**: Common cause of bugs in code.
# 
# Reference: https://automatetheboringstuff.com/chapter4/
# 

# ### Lists

# In[226]:


variable1 = [1, 3, [2,4]]
# Only reference is copied, not value:
variable2 = variable1
print(f"Variable 1: {variable1} and Variable 2: {variable2}")
variable2[0] = 10
print(f"Variable 1: {variable1} and Variable 2: {variable2}")


# In[227]:


import copy
variable1 = [1, 3, [2, 4]]
# Make (shallow) copy of variable:
variable2 = copy.copy(variable1)
print(f"Variable 1: {variable1} and Variable 2: {variable2}")
variable2[0] = 10
print(f"Variable 1: {variable1} and Variable 2: {variable2}")
variable2[2] = [-1]
print(f"Variable 1: {variable1} and Variable 2: {variable2}")


# In[228]:


variable1 = [1, 3, [[2], 4]]
# Make deep copy of variable:
variable2 = copy.deepcopy(variable1)
print(f"Variable 1: {variable1} and Variable 2: {variable2}")
variable2[0] = 10
print(f"Variable 1: {variable1} and Variable 2: {variable2}")
variable2[2][0] = [-1]
print(f"Variable 1: {variable1} and Variable 2: {variable2}")


# ### Dictionaries

# In[247]:


dictionary1 = {'key1': 'value1',
               'key2': 'value2'
              }
dictionary2 = dictionary1
print(f"Dictionary 1: {dictionary1} and Dictionary 2: {dictionary2}")
dictionary2['key2'] = '2'
print(f"Dictionary 1: {dictionary1} and Dictionary 2: {dictionary2}")


# In[248]:


dictionary1 = {'key1': 'value1',
               'key2': 'value2'
              }
dictionary2 = copy.deepcopy(dictionary1)
print(f"Dictionary 1: {dictionary1} and Dictionary 2: {dictionary2}")
dictionary2['key2'] = '2'
print(f"Dictionary 1: {dictionary1} and Dictionary 2: {dictionary2}")


# ## List Comprehension
# List comprehension is an alternative to a for-loop that's a few lines long.

# In[251]:


[(values, keys) for (keys, values) in course_information.items()]


# # In-Class Lab -- Due at end of class:

# Coding Tic-Tac-Toe, per: https://automatetheboringstuff.com/chapter5/
# 
# - Set-up a Tic-Tac-Toe board as a dictionary: 
# ```
# theBoard = {'top-L': ' ',
#             'top-M': ' ',
#             'top-R': ' ',
#             'mid-L': ' ',
#             'mid-M': ' ',
#             'mid-R': ' ',
#             'low-L': ' ',
#             'low-M': ' ',
#             'low-R': ' '
#            }
# ```
# - Use the [random module](https://docs.python.org/3/library/random.html) to randomly choose (available) locations for (alternating) placing of Xs and Os
# - Declare winner or tie

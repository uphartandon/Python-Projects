#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""Some dictionary Operations for practice, this code will help to understand how to convert dictinory element to list,
tuple and assining new values to keys and then extracting keys and values from it"""

user_input = input("Please provide the paragraph from google""\n")
#Taking paragraph as an input from user from google"


par_list = user_input.split() # Creating list from the paragrapg

print("Converting para into list","\n",par_list,"\n")

rem_dup = set(par_list) #Removing duplicates from the paragraph using sets

print("After deleting the duplicates:", rem_dup,"\n")
new_lis = list(rem_dup) #converting set to list

dict_obj={} # Creating an empty list to assign values

#Running for loop to assign dictionary keys (Extracted from para) a value as "Uphar"

for i in new_lis:
    dict_obj[i]="uphar"
print("Assigning values to the the keys", dict_obj,"\n")

#Converting dictinary values to tuple (as it was desired)
lis_tuple = tuple(dict_obj.values())
print("tuple of all dict values are:", lis_tuple,"\n")

#Converting keys to list

lis_keys = list(dict_obj.keys())
print("List of all dict keys are" "\n",lis_keys)

"""Samples paragraph : input = The Moon is Earth's only natural satellite and is quarter the size of the Earth

Expected output:

Converting para into list 
 ['The', 'Moon', 'is', "Earth's", 'only', 'natural', 'satellite', 'and', 'is', 'quarter', 'the', 'size', 'of', 'the', 'Earth'] 

After deleting the duplicates: {'is', 'the', 'The', 'natural', 'quarter', "Earth's", 'only', 'satellite', 'size', 'of', 'Moon', 'and', 'Earth'} 

Assigning values to the the keys {'is': 'uphar', 'the': 'uphar', 'The': 'uphar', 'natural': 'uphar', 'quarter': 'uphar', "Earth's": 'uphar', 'only': 'uphar', 'satellite': 'uphar', 'size': 'uphar', 'of': 'uphar', 'Moon': 'uphar', 'and': 'uphar', 'Earth': 'uphar'} 

tuple of all dict values are: ('uphar', 'uphar', 'uphar', 'uphar', 'uphar', 'uphar', 'uphar', 'uphar', 'uphar', 'uphar', 'uphar', 'uphar', 'uphar') 

List of all dict keys are
 ['is', 'the', 'The', 'natural', 'quarter', "Earth's", 'only', 'satellite', 'size', 'of', 'Moon', 'and', 'Earth']"""


# In[ ]:





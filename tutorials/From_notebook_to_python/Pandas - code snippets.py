#!/usr/bin/env python
# coding: utf-8

# # Pandas - code snippets

# # Loading Some Example Data

# In[2]:


import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/rasbt/python_reference/master/Data/some_soccer_data.csv')
df


# # If-tests

# I was recently asked how to do an if-test in pandas, that is, how to create an array of 1s and 0s depending on a condition, e.g., if `val` less than 0.5 -> 0, else -> 1. Using the boolean mask, that's pretty simple since `True` and `False` are integers after all.

# In[1]:


int(True)


# In[2]:


import pandas as pd

a = [[2., .3, 4., 5.], [.8, .03, 0.02, 5.]]
df = pd.DataFrame(a)
df


# In[3]:


df = df <= 0.05
df


# In[4]:


df.astype(int)


# # References
# - https://nbviewer.org/github/rasbt/python_reference/blob/master/tutorials/things_in_pandas.ipynb

# In[ ]:





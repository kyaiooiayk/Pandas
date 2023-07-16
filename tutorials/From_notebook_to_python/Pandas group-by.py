#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Imports" data-toc-modified-id="Imports-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Imports</a></span></li><li><span><a href="#Pandas-groupby" data-toc-modified-id="Pandas-groupby-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Pandas groupby</a></span></li><li><span><a href="#Example-#1" data-toc-modified-id="Example-#1-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Example #1</a></span></li><li><span><a href="#Example-#2" data-toc-modified-id="Example-#2-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Example #2</a></span></li><li><span><a href="#Example-#3" data-toc-modified-id="Example-#3-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Example #3</a></span></li><li><span><a href="#Example-#4" data-toc-modified-id="Example-#4-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Example #4</a></span></li><li><span><a href="#Example-#5" data-toc-modified-id="Example-#5-8"><span class="toc-item-num">8&nbsp;&nbsp;</span>Example #5</a></span></li><li><span><a href="#References" data-toc-modified-id="References-9"><span class="toc-item-num">9&nbsp;&nbsp;</span>References</a></span></li><li><span><a href="#Requirements" data-toc-modified-id="Requirements-10"><span class="toc-item-num">10&nbsp;&nbsp;</span>Requirements</a></span></li></ul></div>

# # Introduction
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# **What?** Pandas group-by
# 
# </font>
# </div>

# # Imports
# <hr style="border:2px solid black"> </hr>

# In[42]:


import numpy as np
import pandas as pd
import seaborn as sns


# # Pandas groupby
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - A groupby operation involves some combination of splitting the object, applying a function, and combining the results. 
# - This can be used to group large amounts of data and compute operations on these groups.
# - The point of all of this is to use the data in a more efficent manner.
# 
# </font>
# </div>

# # Example #1
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - Get the mean `Max Speed` of the all the entries under Animal.
# - What `gropby` does is to group all the entries corresponsing to a single instance under the `Animal` column and then compute the mean.
# 
# </font>
# </div>

# In[2]:


df = pd.DataFrame({'Animal': ['Falcon', 'Falcon',
                              'Parrot', 'Parrot'],
                   'Max Speed': [380., 370., 24., 26.]})


# In[3]:


df


# In[4]:


df.groupby(['Animal'])


# In[5]:


df.groupby(['Animal']).mean()


# # Example #2
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - We can groupby different levels of a hierarchical index using the level parameter.
# 
# </font>
# </div>

# In[6]:


arrays = [['Falcon', 'Falcon', 'Parrot', 'Parrot'],
          ['Captive', 'Wild', 'Captive', 'Wild']]

index = pd.MultiIndex.from_arrays(arrays, names=('Animal', 'Type'))

df = pd.DataFrame({'Max Speed': [390., 350., 30., 20.]}, index=index)


# In[7]:


df


# In[8]:


df.groupby(level=0).mean()        


# In[9]:


df.groupby(level="Type").mean()


# # Example #3
# <hr style="border:2px solid black"> </hr>

# In[10]:


l = [[1, 2, 3], [1, None, 4], [2, 1, 3], [1, 2, 2]]
df = pd.DataFrame(l, columns=["a", "b", "c"])
df


# <div class="alert alert-info">
# <font color=black>
# 
# - When using the parameter `by` all entries under the provided column assigned an index.
# - This means that for instance under column `a` we have `2` at level `b=1` because we sum 2 (and not more in this case) which is the value under column `a` where there is a corresponding `b=1`.
# 
# </font>
# </div>

# In[11]:


df.groupby(by=["b"]).sum()


# In[12]:


df.groupby(by=["b"], dropna=False).sum()


# # Example #4
# <hr style="border:2px solid black"> </hr>

# In[13]:


df = pd.read_csv("./nba.csv")
df


# In[14]:


df["Team"].unique()


# In[15]:


# applying groupby() function to group the data by Team value
gk = df.groupby('Team')
gk.first()


# In[16]:


# Finding the values contained in the "Boston Celtics" group
gk.get_group('Boston Celtics')


# In[17]:


# Use groupby() function to form groups based on more than one category (i.e. Use more than one column to perform the splitting).


# In[18]:


gkk = df.groupby(['Team', 'Position'])


# In[19]:


# Print the first value in each group
gkk.first()


# # Example #5
# <hr style="border:2px solid black"> </hr>

# In[22]:


df.head()


# In[41]:


merged = pd.merge(
df.groupby("Team")["Name"].count().reset_index(name="No team member"),
df.groupby("Team")["Weight"].sum().reset_index(name="Sum Weight")
)
merged["average_weight"] = merged["Sum Weight"]/merged["No team member"]
merged


# # References
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# - [Pandas groupby vs. SQL groupby](https://realpython.com/pandas-groupby/)
# - https://www.geeksforgeeks.org/python-pandas-dataframe-groupby/
# - https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html
# 
# </font>
# </div>

# # Requirements
# <hr style="border:2px solid black"> </hr>

# In[20]:


get_ipython().run_line_magic('load_ext', 'watermark')
get_ipython().run_line_magic('watermark', '-v -iv')


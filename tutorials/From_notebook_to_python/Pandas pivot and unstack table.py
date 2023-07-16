#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Imports" data-toc-modified-id="Imports-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Imports</a></span></li><li><span><a href="#Read-in-the-dataset" data-toc-modified-id="Read-in-the-dataset-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Read-in the dataset</a></span></li><li><span><a href="#Pivot-the-Data" data-toc-modified-id="Pivot-the-Data-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Pivot the Data</a></span></li><li><span><a href="#Unstack-table" data-toc-modified-id="Unstack-table-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Unstack table</a></span></li><li><span><a href="#Pivot-vs.-Stack-vs.-Usntack" data-toc-modified-id="Pivot-vs.-Stack-vs.-Usntack-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Pivot vs. Stack vs. Usntack</a></span></li><li><span><a href="#References" data-toc-modified-id="References-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# **What?** Pandas pivot and unstack table
# 
# </font>
# </div>

# # Imports
# <hr style="border:2px solid black"> </hr>

# In[2]:


import numpy as np
import pandas as pd


# # Read-in the dataset
# <hr style="border:2px solid black"> </hr>

# In[3]:


df = pd.read_excel('./sales-funnel.xlsx')
df.head()


# In[4]:


df.shape


# # Pivot the Data
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - Most people likely have experience with pivot tables in **Excel**. Pandas provides a similar function.
# - The simplest pivot table must have a dataframe and an `index`, which stands for the column that the data will be aggregated upon and `values`, which are the aggregated value.
# - In **simple terms**, it aggregates value and present them in a way that is easy to read.
# 
# </font>
# </div>

# In[4]:


df.pivot_table(index = ['Manager', 'Rep'], values = ['Price'])


# <div class="alert alert-info">
# <font color=black>
# 
# - By default, the values will be averaged, but we can do a count or a sum by providing the aggfun parameter.
# 
# </font>
# </div>

# In[5]:


# you can provide multiple arguments to almost every argument of the pivot_table function
df.pivot_table(index = ['Manager', 'Rep'], values = ['Price'], aggfunc = [np.mean, len])


# <div class="alert alert-info">
# <font color=black>
# 
# - If we want to see sales broken down by the products, the columns variable allows us to define one or more columns. 
# - Note: The confusing points with the pivot_table is the use of columns and values. 
# - Columns are optional - they provide an additional way to segment the actual values you care about. 
# - The aggregation functions are applied to the values you've listed. 
# 
# </font>
# </div>

# In[6]:


df.pivot_table(index = ['Manager','Rep'], values = ['Price'],
               columns = ['Product'], aggfunc = [np.sum])


# The NaNs are a bit distracting. If we want to remove them, we could use `fill_value` to set them to 0.

# In[7]:


df.pivot_table(index = ['Manager', 'Rep'], values = ['Price', 'Quantity'],
               columns = ['Product'], aggfunc = [np.sum], fill_value = 0)


# <div class="alert alert-info">
# <font color=black>
# 
# - You can move items to the index to get a different visual representation. 
# - The following code chunk removes Product from the columns and add it to the index and also uses the margins = True parameter to add totals to the pivot table. 
# 
# </font>
# </div>

# In[8]:


df.pivot_table(index = ['Manager', 'Rep', 'Product'],
               values = ['Price', 'Quantity'], aggfunc = [np.sum], margins = True)


# <div class="alert alert-info">
# <font color=black>
# 
# - We can define the status column as a category and set the order we want in the pivot table. 
# 
# </font>
# </div>

# In[9]:


df['Status'] = df['Status'].astype('category')
df['Status'] = df['Status'].cat.set_categories(['won', 'pending', 'presented', 'declined'])
df.pivot_table(index = ['Manager', 'Status'], values = ['Price'],
               aggfunc = [np.sum], fill_value = 0, margins = True)


# <div class="alert alert-info">
# <font color=black>
# 
# - A really handy feature is the ability to pass a dictionary to the aggfunc so you can perform different functions on each of the values you select. 
# - This has a side-effect of making the labels a little cleaner.
# 
# </font>
# </div>

# In[10]:


table = df.pivot_table(index = ['Manager','Status'], 
                       columns = ['Product'], 
                       values = ['Quantity','Price'],
                       aggfunc = {'Quantity': len, 'Price': [np.sum, np.mean]}, 
                       fill_value = 0)
table


# <div class="alert alert-info">
# <font color=black>
# 
# - Once you have generated your data, it is in a DataFrame so you can filter on it using your standard DataFrame functions. e.g. We can look at all of our pending and won deals.
# 
# </font>
# </div>

# In[11]:


# .query uses strings for boolean indexing and we don't have to 
# specify the dataframe that the Status is comming from
table.query("Status == ['pending','won']")


# # Unstack table
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - Pivot a level of the (necessarily hierarchical) index labels.
# 
# </font>
# </div>

# In[3]:


index = pd.MultiIndex.from_tuples([('one', 'a'), ('one', 'b'),

                                   ('two', 'a'), ('two', 'b')])


# In[4]:


s = pd.Series(np.arange(1.0, 5.0), index=index)


# In[5]:


s


# In[6]:


s.unstack(level=-1)


# In[7]:


s.unstack(level=0)


# In[9]:


df = s.unstack(level=0)
df.unstack()


# In[10]:


# Inverse operation
df.stack()


# # Pivot vs. Stack vs. Usntack
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - `DataFrame.pivot`   = Pivot a table based on column values.
# - `DataFrame.stack`   = Pivot a level of the column labels (inverse operation from unstack).
# - `DataFrame.unstack` = Pivot a level of the (necessarily hierarchical) index labels.
# 
# </font>
# </div>

# # References
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# - [This notebook](https://github.com/ethen8181/machine-learning/blob/master/python/pivot_table/pivot_table.ipynb)
# - [Blog: Pandas pivot table explained](http://pbpython.com/pandas-pivot-table-explained.html)
# - https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.unstack.html
#     
# </font>
# </div>

# In[ ]:





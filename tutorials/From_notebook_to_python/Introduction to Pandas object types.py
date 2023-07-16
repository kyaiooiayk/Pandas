#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Pandas-Object-Types" data-toc-modified-id="Pandas-Object-Types-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Pandas Object Types</a></span></li><li><span><a href="#Imports" data-toc-modified-id="Imports-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Imports</a></span></li><li><span><a href="#DataFrame-Class" data-toc-modified-id="DataFrame-Class-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>DataFrame Class</a></span></li><li><span><a href="#Basic-Analytics" data-toc-modified-id="Basic-Analytics-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Basic Analytics</a></span></li><li><span><a href="#Series-Class" data-toc-modified-id="Series-Class-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Series Class</a></span></li><li><span><a href="#Conclusions" data-toc-modified-id="Conclusions-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Conclusions</a></span></li><li><span><a href="#References" data-toc-modified-id="References-8"><span class="toc-item-num">8&nbsp;&nbsp;</span>References</a></span></li><li><span><a href="#Requirements" data-toc-modified-id="Requirements-9"><span class="toc-item-num">9&nbsp;&nbsp;</span>Requirements</a></span></li></ul></div>

# # Introduction
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# **What?** Introduction to Pandas object types
# 
# </font>
# </div>

# # Pandas Object Types
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - `DataFrame` is a class designed to efficiently handle data in tabular form, i.e., data characterized by a columnar organiza‐ tion. To this end, the DataFrame class provides, for instance, column labeling as well as flexible indexing capabilities for the rows (records) of the data set, similar to a table in a relational database or an Excel spreadsheet
# 
# - `Series` class of pandas, which in a sense rep‐ resents a special case of the `DataFrame` class with a single column of data only. A Series object is obtained when a single column is selected from a multicolumn `DataFrame` object.
# 
# </font>
# </div>

# ![image.png](attachment:image.png)

# # Imports
# <hr style = "border:2px solid black" ></hr>

# In[1]:


import pandas as pd  


# # DataFrame Class
# <hr style = "border:2px solid black" ></hr>

# In[2]:


df = pd.DataFrame([10, 20, 30, 40],  
                  columns=['numbers'],  
                  index=['a', 'b', 'c', 'd'])  


# In[3]:


df  


# In[4]:


df.index  


# In[5]:


df.columns  


# In[6]:


df.loc['c']  


# In[7]:


df.loc[['a', 'd']]  


# In[8]:


df.iloc[1:3]  


# In[9]:


df.sum()  


# In[10]:


df.apply(lambda x: x ** 2)  


# In[11]:


df ** 2  


# In[12]:


df['floats'] = (1.5, 2.5, 3.5, 4.5)  


# In[13]:


df


# In[14]:


df['floats']  


# In[15]:


df['names'] = pd.DataFrame(['Yves', 'Sandra', 'Lilli', 'Henry'],
                           index=['d', 'a', 'b', 'c'])  


# In[16]:


df


# In[17]:


df.append({'numbers': 100, 'floats': 5.75, 'names': 'Jil'},
               ignore_index=True)  


# In[18]:


df = df.append(pd.DataFrame({'numbers': 100, 'floats': 5.75,
                             'names': 'Jil'}, index=['y',]))  


# In[19]:


df


# In[20]:


df = df.append(pd.DataFrame({'names': 'Liz'}, index=['z',]), sort=False)  


# In[21]:


df


# In[22]:


df.dtypes  


# In[23]:


df[['numbers', 'floats']].mean()  


# In[24]:


df[['numbers', 'floats']].std()  


# # Basic Analytics

# In[25]:


import numpy as np


# In[26]:


np.random.seed(100)


# In[27]:


a = np.random.standard_normal((9, 4))


# In[28]:


a


# In[29]:


a = np.random.standard_normal((9, 4))
df = pd.DataFrame(a)  


# In[30]:


df


# In[31]:


df.columns = ['No1', 'No2', 'No3', 'No4']  


# In[32]:


df


# In[33]:


df['No2'].mean()  


# In[34]:


dates = pd.date_range('2019-1-1', periods=9, freq='M')  


# In[35]:


dates


# In[36]:


df.index = dates


# In[37]:


df


# In[38]:


df.values


# In[39]:


np.array(df)


# In[40]:


df.info()  


# In[41]:


df.describe()  


# In[42]:


df.sum()  


# In[43]:


df.mean()  


# In[44]:


df.mean(axis=0)  


# In[45]:


df.mean(axis=1)  


# In[46]:


df.cumsum()  


# In[47]:


np.mean(df)  


# In[48]:


# raises warning
np.log(df)  


# In[49]:


np.sqrt(abs(df))  


# In[50]:


np.sqrt(abs(df)).sum()  


# In[51]:


100 * df + 100  


# # Series Class
# <hr style = "border:2px solid black" ></hr>

# In[52]:


type(df)


# In[53]:


S = pd.Series(np.linspace(0, 15, 7), name='series')


# In[54]:


S


# In[55]:


type(S)


# In[56]:


s = df['No1']


# In[57]:


s


# In[58]:


type(s)


# In[59]:


s.mean()


# In[60]:


s.plot(lw=2.0, figsize=(10, 6));
# plt.savefig('../../images/ch05/pd_plot_03.png')


# # Conclusions
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-danger">
# <font color=black>
# 
# - `DataFrame` class is particularly suited to working with tabular data of any kind. 
# - Most operations on such objects are vectorized, leading not only—as in the `NumPy` case—to concise code but also to high performance in general.
# - In addition, pandas makes working with incomplete data sets convenient (which is not the case with `NumPy`, for instance).
# 
# </font>
# </div>

# # References
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# - https://github.com/yhilpisch/py4fi2nd/blob/master/code/ch05/05_pandas.ipynb
# 
# </font>
# </div>

# # Requirements
# <hr style = "border:2px solid black" ></hr>

# In[61]:


get_ipython().run_line_magic('load_ext', 'watermark')
get_ipython().run_line_magic('watermark', '-v -iv')


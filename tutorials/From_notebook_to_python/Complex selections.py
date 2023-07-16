#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Imports" data-toc-modified-id="Imports-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Imports</a></span></li><li><span><a href="#Complex-Selection" data-toc-modified-id="Complex-Selection-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Complex Selection</a></span></li><li><span><a href="#References" data-toc-modified-id="References-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>References</a></span></li><li><span><a href="#Requirements" data-toc-modified-id="Requirements-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Requirements</a></span></li></ul></div>

# # Introduction
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# **What?** Complex selections
# 
# </font>
# </div>

# # Imports
# <hr style = "border:2px solid black" ></hr>

# In[1]:


import numpy as np
import pandas as pd  


# # Complex Selection
# <hr style = "border:2px solid black" ></hr>

# In[2]:


data = np.random.standard_normal((10, 2))  


# In[3]:


df = pd.DataFrame(data, columns=['x', 'y'])  


# In[4]:


df.info()  


# In[5]:


df.head()  


# In[6]:


df.tail()  


# In[7]:


df['x'] > 0.5  


# In[8]:


(df['x'] > 0) & (df['y'] < 0)  


# In[9]:


(df['x'] > 0) | (df['y'] < 0)  


# In[10]:


df[df['x'] > 0]  


# In[11]:


df.query('x > 0')  


# In[12]:


df[(df['x'] > 0) & (df['y'] < 0)]  


# In[13]:


df.query('x > 0 & y < 0')  


# In[14]:


df[(df.x > 0) | (df.y < 0)]  


# In[15]:


df > 0  


# In[16]:


df[df > 0]  


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

# In[17]:


get_ipython().run_line_magic('load_ext', 'watermark')
get_ipython().run_line_magic('watermark', '-v -iv')


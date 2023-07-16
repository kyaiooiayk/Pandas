#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Imports" data-toc-modified-id="Imports-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Imports</a></span></li><li><span><a href="#Performance-aspects" data-toc-modified-id="Performance-aspects-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Performance aspects</a></span></li><li><span><a href="#References" data-toc-modified-id="References-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>References</a></span></li><li><span><a href="#Requirements" data-toc-modified-id="Requirements-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Requirements</a></span></li></ul></div>

# # Introduction
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# **What?** Performance aspects
# 
# </font>
# </div>

# # Imports
# <hr style = "border:2px solid black" ></hr>

# In[1]:


import numpy as np
import pandas as pd  


# # Performance aspects
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - There are often multiple options to achieve the same goal with pandas. 
# - This section compares such options for adding up two columns element-wise.
# 
# </font>
# </div>

# In[2]:


data = np.random.standard_normal((1000000, 2))  


# In[3]:


data.nbytes  


# In[4]:


df = pd.DataFrame(data, columns=['x', 'y'])  


# In[5]:


df.info()  


# In[6]:


get_ipython().run_line_magic('time', "res = df['x'] + df['y']")


# In[7]:


res[:3]


# In[8]:


get_ipython().run_line_magic('time', 'res = df.sum(axis=1)')


# In[9]:


res[:3]


# In[10]:


get_ipython().run_line_magic('time', 'res = df.values.sum(axis=1)')


# In[11]:


res[:3]


# In[12]:


get_ipython().run_line_magic('time', 'res = np.sum(df, axis=1)')


# In[13]:


res[:3]


# In[14]:


get_ipython().run_line_magic('time', 'res = np.sum(df.values, axis=1)')


# In[15]:


res[:3]


# In[16]:


get_ipython().run_line_magic('time', "res = df.eval('x + y')")


# In[17]:


res[:3]


# In[18]:


get_ipython().run_line_magic('time', "res = df.apply(lambda row: row['x'] + row['y'], axis=1)")


# In[19]:


res[:3]


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

# In[20]:


get_ipython().run_line_magic('load_ext', 'watermark')
get_ipython().run_line_magic('watermark', '-v -iv')


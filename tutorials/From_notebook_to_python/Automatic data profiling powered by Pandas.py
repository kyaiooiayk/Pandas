#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Imports" data-toc-modified-id="Imports-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Imports</a></span></li><li><span><a href="#Load-dataset" data-toc-modified-id="Load-dataset-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Load dataset</a></span></li><li><span><a href="#Firing-automatic-data-profiling" data-toc-modified-id="Firing-automatic-data-profiling-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Firing automatic data profiling</a></span></li><li><span><a href="#Reference" data-toc-modified-id="Reference-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Reference</a></span></li></ul></div>

# # Introduction

# <div class="alert alert-block alert-warning">
# <font color=black>
# 
# **What?** Automatic Pandas profiling
# 
# </font>
# </div>

# # Imports

# In[1]:


import pandas as pd
from pandas_profiling import ProfileReport


# # Load dataset

# <div class="alert alert-block alert-info">
# <font color=black>
# 
# - This dataset includes the location, mass, composition, and fall year for over 45,000 meteorites that have struck our planet.
# - NASA Meteorites Landings dataset
# 
# </font>
# </div>

# In[ ]:


data = pd.read_csv('./Meteorite_Landings.csv')


# In[ ]:


data.head(5)


# In[ ]:


data.shape


# # Firing automatic data profiling

# <div class="alert alert-block alert-info">
# <font color=black>
# 
# - This will NOT do everything.
# - It just kick start the project.
# - You still need futher manual cleaning if needed.
# 
# </font>
# </div>

# In[ ]:


ProfileReport(data)


# <div class="alert alert-block alert-info">
# <font color=black>
# 
# - Something similar to **Overview** can be obtained with **pd.describe()** 
# 
# </font>
# </div>

# # Reference

# <div class="alert alert-warning">
# <font color=black>
# 
# - [Link to dataset](https://data.nasa.gov/api/views/gh4g-9sfh/rows.csv?accessType=DOWNLOAD)
# - https://towardsdatascience.com/pandas-profiling-for-quicker-data-understanding-83bb9fc6719f
# - [Pandas profiler at its best](https://github.com/timmajani/Efficient-Python-for-Data-Scientists/blob/main/Data%20Exploration%20Becomes%20Easier%20%26%20Better%20With%20Pandas%20Profiling.md)
#     
# </font>
# </div>

# In[ ]:





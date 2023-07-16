#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Imports" data-toc-modified-id="Imports-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Imports</a></span></li><li><span><a href="#Example-#1" data-toc-modified-id="Example-#1-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Example #1</a></span></li><li><span><a href="#Example-#2" data-toc-modified-id="Example-#2-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Example #2</a></span></li><li><span><a href="#References" data-toc-modified-id="References-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>References</a></span></li><li><span><a href="#Requirements" data-toc-modified-id="Requirements-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Requirements</a></span></li></ul></div>

# # Introduction
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-warning">
# <font color=black>
# 
# **What?** How to use Pandas for plotting
# 
# </font>
# </div>

# # Imports
# <hr style = "border:2px solid black" ></hr>

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt


# # Example #1
# <hr style = "border:2px solid black" ></hr>

# In[2]:


# weather data from London, UK, for 2008.
weather = pd.read_csv("https://raw.githubusercontent.com/alanjones2/dataviz/master/london2018.csv")
print(weather[:2])


# In[3]:


# Make a dictionary and pass is it as an argument
plot_kwargs={ "figsize" :(8,5), "color" :'Red', "title" :"Maximum temperatures", "grid" :True, 
             "label" :"Max Temp", "fontsize" : 18 }
    
weather.plot(x="Month", y="Tmax", **plot_kwargs)
plt.show()


# # Example #2
# <hr style = "border:2px solid black" ></hr>

# In[4]:


a = np.random.standard_normal((9, 4))
df = pd.DataFrame(a) 


# In[5]:


from pylab import plt, mpl  
plt.style.use('seaborn')  
mpl.rcParams['font.family'] = 'serif'  
get_ipython().run_line_magic('config', "InlineBackend.figure_format = 'svg'")


# In[6]:


df.cumsum().plot(lw=2.0, figsize=(10, 6));  


# In[7]:


df.plot.bar(figsize=(10, 6), rot=30);  


# # References
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# - https://towardsdatascience.com/5-easy-ways-of-customizing-pandas-plots-and-charts-7aefa73ff18b
# 
# </font>
# </div>

# # Requirements
# <hr style = "border:2px solid black" ></hr>

# In[8]:


get_ipython().run_line_magic('load_ext', 'watermark')
get_ipython().run_line_magic('watermark', '-v -iv')


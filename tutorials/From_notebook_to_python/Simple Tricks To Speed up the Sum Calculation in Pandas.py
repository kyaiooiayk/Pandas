#!/usr/bin/env python
# coding: utf-8

# # 4 Simple Tricks To Speed up the Sum Calculation in Pandas

# I wanted to improve the performance of some passages in my code a little bit and found that some simple tweaks can speed up the  `pandas` section significantly. I thought that it might be one useful thing to share -- and no Cython or just-in-time compilation is required! 

# In my case, I had a large dataframe where I wanted to calculate the sum of specific columns for different combinations of rows (approx. 100,000,000 of them, that's why I was looking for ways to speed it up). Anyway, below is a simple toy DataFrame to explore the `.sum()` method a little bit.

# In[2]:


import pandas as pd
import numpy as np

df = pd.DataFrame()

for col in ('a', 'b', 'c', 'd'):
    df[col] = pd.Series(range(1000), index=range(1000))


# In[3]:


df.tail()


# Let's assume we are interested in calculating the sum of column `a`, `c`, and `d`, which would look like this:

# In[4]:


df.loc[:, ['a', 'c', 'd']].sum(axis=0)


# Now, the `.loc` method is probably the most "costliest" one for this kind of operation. Since we are only intersted in the resulting numbers (i.e., the column sums), there is no need to make a copy of the array. Anyway, let's use the method above as a reference for comparison:

# In[5]:


# 1
get_ipython().run_line_magic('timeit', "-n 1000 -r 5 df.loc[:, ['a', 'c', 'd']].sum(axis=0)")


# Although this is a rather small DataFrame (1000 x 4), let's see by how much we can speed it up using a different slicing method:

# In[6]:


# 2
get_ipython().run_line_magic('timeit', "-n 1000 -r 5 df[['a', 'c', 'd']].sum(axis=0)")


# Next, let us use the Numpy representation of  the `NDFrame` via the `.values` attribue:

# In[7]:


# 3
get_ipython().run_line_magic('timeit', "-n 1000 -r 5 df[['a', 'c', 'd']].values.sum(axis=0)")


# While the speed improvements in #2 and #3 were not really a surprise, the next "trick" surprised me a little bit. Here, we are calculating the sum of each column separately rather than slicing the array.

# In[8]:


[df[col].values.sum(axis=0) for col in ('a', 'c', 'd')]


# In[9]:


# 4
get_ipython().run_line_magic('timeit', "-n 1000 -r 5 [df[col].values.sum(axis=0) for col in ('a', 'c', 'd')]")


# In this case, this is an almost 10x improvement!

# One more thing: Let's try the Einstein summation convention [`einsum`](http://docs.scipy.org/doc/numpy/reference/generated/numpy.einsum.html).

# In[10]:


from numpy import einsum
[einsum('i->', df[col].values) for col in ('a', 'c', 'd')]


# In[11]:


# 5
get_ipython().run_line_magic('timeit', "-n 1000 -r 5 [einsum('i->', df[col].values) for col in ('a', 'c', 'd')]")


# ### Conclusion:

# Using some simple tricks, the column sum calculation improved from 1370 to 57.7 µs per loop (approx. 25x faster!)

# ### What about larger DataFrames?

# So, what does this trend look like for larger DataFrames?

# In[23]:


import timeit
import random
from numpy import einsum
import pandas as pd

def run_loc_sum(df):
    return df.loc[:, ['a', 'c', 'd']].sum(axis=0)

def run_einsum(df):
    return [einsum('i->', df[col].values) for col in ('a', 'c', 'd')]

orders = [10**i for i in range(4, 8)]
loc_res = []
einsum_res = []

for n in orders:

    df = pd.DataFrame()
    for col in ('a', 'b', 'c', 'd'):
        df[col] = pd.Series(range(n), index=range(n))
    
    print('n=%s (%s of %s)' %(n, orders.index(n)+1, len(orders)))

    loc_res.append(min(timeit.Timer('run_loc_sum(df)' , 
            'from __main__ import run_loc_sum, df').repeat(repeat=5, number=1)))

    einsum_res.append(min(timeit.Timer('run_einsum(df)' , 
            'from __main__ import run_einsum, df').repeat(repeat=5, number=1)))

print('finished')


# In[24]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[26]:


from matplotlib import pyplot as plt

def plot_1():
    
    fig = plt.figure(figsize=(12,6))
    
    plt.plot(orders, loc_res, 
             label="df.loc[:, ['a', 'c', 'd']].sum(axis=0)", 
             lw=2, alpha=0.6)
    plt.plot(orders,einsum_res, 
             label="[einsum('i->', df[col].values) for col in ('a', 'c', 'd')]", 
             lw=2, alpha=0.6)

    plt.title('Pandas Column Sums', fontsize=20)
    plt.xlim([min(orders), max(orders)])
    plt.grid()

    #plt.xscale('log')
    plt.ticklabel_format(style='plain', axis='x')
    plt.legend(loc='upper left', fontsize=14)
    plt.xlabel('Number of rows', fontsize=16)
    plt.ylabel('time in seconds', fontsize=16)
    
    plt.tight_layout()
    plt.show()
    
plot_1()


# It looks like that the benefit of calculating the sums separately for each column becomes even larger the more rows the DataFrame has.

# Another question to ask: How does this scale if we have a growing number of columns?

# In[35]:


import timeit
import random
from numpy import einsum
import pandas as pd

def run_loc_sum(df, n):
    return df.loc[:, 0:n-1].sum(axis=0)

def run_einsum(df, n):
    return [einsum('i->', df[col].values) for col in range(0,n-1)]

orders = [10**i for i in range(2, 5)]
loc_res = []
einsum_res = []

for n in orders:

    df = pd.DataFrame()
    for col in range(n):
        df[col] = pd.Series(range(1000), index=range(1000))
    
    print('n=%s (%s of %s)' %(n, orders.index(n)+1, len(orders)))

    loc_res.append(min(timeit.Timer('run_loc_sum(df, n)' , 
            'from __main__ import run_loc_sum, df, n').repeat(repeat=5, number=1)))

    einsum_res.append(min(timeit.Timer('run_einsum(df, n)' , 
            'from __main__ import run_einsum, df, n').repeat(repeat=5, number=1)))

print('finished')


# In[37]:


from matplotlib import pyplot as plt

def plot_2():
    
    fig = plt.figure(figsize=(12,6))
    
    plt.plot(orders, loc_res, 
             label="df.loc[:, 0:n-1].sum(axis=0)", 
             lw=2, alpha=0.6)
    plt.plot(orders,einsum_res, 
             label="[einsum('i->', df[col].values) for col in range(0,n-1)]", 
             lw=2, alpha=0.6)

    plt.title('Pandas Column Sums', fontsize=20)
    plt.xlim([min(orders), max(orders)])
    plt.grid()

    #plt.xscale('log')
    plt.ticklabel_format(style='plain', axis='x')
    plt.legend(loc='upper left', fontsize=14)
    plt.xlabel('Number of columns', fontsize=16)
    plt.ylabel('time in seconds', fontsize=16)
    
    plt.tight_layout()
    plt.show()
    
plot_2()


# # References
# - https://nbviewer.org/github/rasbt/python_reference/blob/master/benchmarks/pandas_sum_tricks.ipynb

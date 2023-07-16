#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Imports" data-toc-modified-id="Imports-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Imports</a></span></li><li><span><a href="#Motivation" data-toc-modified-id="Motivation-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Motivation</a></span></li><li><span><a href="#Load-the-dataset" data-toc-modified-id="Load-the-dataset-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Load the dataset</a></span></li><li><span><a href="#Optimising-Numeric-Columns" data-toc-modified-id="Optimising-Numeric-Columns-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Optimising Numeric Columns</a></span></li><li><span><a href="#Optimising-object-types" data-toc-modified-id="Optimising-object-types-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Optimising object types</a></span></li><li><span><a href="#Selecting-types-while-reading-the-Data-in" data-toc-modified-id="Selecting-types-while-reading-the-Data-in-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Selecting types while reading the Data in</a></span></li><li><span><a href="#Function-to-automatically-perform-downcasting" data-toc-modified-id="Function-to-automatically-perform-downcasting-8"><span class="toc-item-num">8&nbsp;&nbsp;</span>Function to automatically perform downcasting</a></span></li><li><span><a href="#Conclusions" data-toc-modified-id="Conclusions-9"><span class="toc-item-num">9&nbsp;&nbsp;</span>Conclusions</a></span></li><li><span><a href="#References" data-toc-modified-id="References-10"><span class="toc-item-num">10&nbsp;&nbsp;</span>References</a></span></li><li><span><a href="#Requirements" data-toc-modified-id="Requirements-11"><span class="toc-item-num">11&nbsp;&nbsp;</span>Requirements</a></span></li></ul></div>

# # Introduction
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-warning">
# <font color=black>
# 
# **What?** Optimising Pandas - reduce memory footprint
# 
# </font>
# </div>

# # Imports
# <hr style = "border:2px solid black" ></hr>

# In[2]:


import numpy as np
import pandas as pd


# # Motivation
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-info">
# <font color=black>
# 
# - Less than 100 MB Pandas is OK
# - More than >100 Mb to xx GBs Pandas starts to suffer
# - In this second case people start contemplating Spark which can handle several GBs or even TBs.
# - However, Spark lack a rich feature sets for high quality data cleaning, exploration, and analysis.
# - **Bottom line?** For For medium-sized data, we're better off trying to get more out of pandas, rather than switching to a different tool.
# - Here, we'll show how by selecting the right data tyoes in the column can reduce the meomory footprint.
# 
# </font>
# </div>

# # Load the dataset
# <hr style = "border:2px solid black" ></hr>

# In[3]:


drinks = pd.read_csv('http://bit.ly/drinksbycountry')
drinks.head()


# <div class="alert alert-block alert-info">
# <font color=black>
# 
# - We'll first look at the memory usage of each column, because we're interested in accuracy
# - We'll set the argument deep to True to get an accurate number.
#   
# </font>
# </div>

# In[4]:


drinks.memory_usage(deep = True)


# In[5]:


# This is another option
drinks.info(memory_usage = 'deep')


# <div class="alert alert-block alert-info">
# <font color=black>
# 
# - Pandas groups the columns into blocks of values of the same type, because each data type is stored separately.
# - We’re going to examine the memory usage by each data type.
# - Immediately we can see that **most of the memory** is used by our object columns. 
# 
# </font>
# </div>

# In[6]:


for dtype in ('float', 'int', 'object'):
    selected_dtype = drinks.select_dtypes(include = [dtype])
    mean_usage_b = selected_dtype.memory_usage(deep=True).mean()
    # we can do / 1024 ** 2 to convert bytes to megabytes
    print("Average memory usage for {} columns: {:03.2f} B".format(dtype, mean_usage_b))


# # Optimising Numeric Columns
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-info">
# <font color=black>
# 
# - For blocks representing numeric values like integers and floats, pandas combines the columns and stores them as a NumPy ndarray. The NumPy ndarray is built around a C array, and the values are stored in a contiguous block of memory. This storage model consumes less space and allows us to access the values themselves quickly.
# - Many types in pandas have multiple subtypes that **can use fewer bytes** to represent each value and that is something we can used to save the memory footprint.
# - An int8 value uses 1 byte (or 8 bits) to store a value, and can represent 256 values (2^8) in binary. This means that we can use this subtype to represent values ranging from -128 to 127 (including 0). And uint8, which is unsigned int, means we can only have positive values for this type, thus we can represent 256 values ranging from 0 to 255.
# - To be able to use it we just need the min/max of our data via **numpy.iinfo** <br>
# 
# |memory usage|	float|	int	|uint	|datetime  |bool  |
# |------------|-------|------|-------|----------|------|
# |1 bytes	 | 	     | int8 |uint8  |	 	   |bool  |
# |2 bytes	 |float16| int16|uint16 |	 	   |      |
# |4 bytes	 |float32| int32|uint32 |	 	   |      |
# |8 bytes	 |float64| int64|uint64 |datetime64|	  |
# 
# </font>
# </div>

# In[7]:


int_types = ['uint8', 'int8', 'int16']
for int_type in int_types:
    print(np.iinfo(int_type))


# <div class="alert alert-block alert-info">
# <font color=black>
# 
# - We’ll use `DataFrame.select_dtypes` to select only the integer columns.
# - We'll use `pd.to_numeric()` to downcast our numeric types. 
# - Then we’ll optimize the types and compare the memory usage.
# 
# </font>
# </div>

# In[10]:


def mem_usage(pandas_obj):
    """memory usage of a pandas DataFrame or Series"""
    # we assume if not a DataFrame it's a Series
    if isinstance(pandas_obj, pd.DataFrame):
        usage_b = pandas_obj.memory_usage(deep=True).sum()
    else:
        usage_b = pandas_obj.memory_usage(deep=True)

    return '{:03.2f} B'.format(usage_b)


# In[11]:


drinks_int = drinks.select_dtypes(include=['int'])
converted_int = drinks_int.apply(pd.to_numeric, downcast='unsigned')

print(mem_usage(drinks_int))
print(mem_usage(converted_int))


# In[12]:


# Lets do the same thing with our float columns.
drinks_float = drinks.select_dtypes(include=['float'])
converted_float = drinks_float.apply(pd.to_numeric, downcast='float')

print(mem_usage(drinks_float))
print(mem_usage(converted_float))


# # Optimising object types
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-info">
# <font color=black>
# 
# - The object type represents values using Python string objects, partly due to the lack of support for missing string values in NumPy. Because Python is a high-level, interpreted language, it doesn't have fine grained-control over how values in memory are stored.
# - To overcome this problem, Pandas introduced Categoricals in version 0.15.
# - Since the country and continent columns are strings, they are represented as object types in pandas. 
# - We want to store the continent column as integers to reduce the memory required to store them by converting it to categorical type. 
# - To apply this conversion, we simply have to convert the column type to category using the .astype method.
# - The comparison shows that by converting the continent column to integers we're being more space-efficient. Apart from that it can actually speed up laters operations, e.g. sorting, groupby as we're storing the strings as compactly as integers. 
# 
# </font>
# </div>

# In[13]:


# convert and print the memory usage
continent_col = 'continent'
continent = drinks[continent_col]
continent_cat = drinks[continent_col].astype('category')
print(continent.head())
print(continent_cat.head())
# drinks.memory_usage(deep = True)


# In[14]:


# Lastly, let’s look at the memory usage for this column before and after converting to the category type.
print('original: ', mem_usage(continent))
print('categorical: ', mem_usage(continent_cat))


# <div class="alert alert-block alert-info">
# <font color=black>
# 
# - Let's apply this notion again to the country column.
# - This time, the memory usage for the country column is now larger.
# - The **reason** is that the country column's value is unique.
# - So **do not use** of the cardinality (distinguished values) is high.
# 
# </font>
# </div>

# In[16]:


country_col = 'country'
country = drinks[country_col]
country_cat = drinks[country_col].astype('category')
print('original: ', mem_usage(country))
print('categorical: ', mem_usage(country_cat))


# # Selecting types while reading the Data in
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-info">
# <font color=black>
# 
# - **How can we apply this if we can't even create the dataframe in the first place?**
# - Fortunately, we can specify the optimal column types **when reading** the data. 
# 
# </font>
# </div>

# In[15]:


col_types = {'beer_servings': 'uint32',
             'continent': 'category',
             'country': 'object',
             'spirit_servings': 'uint32',
             'total_litres_of_pure_alcohol': 'float32',
             'wine_servings': 'uint32'}

df_drinks = pd.read_csv('http://bit.ly/drinksbycountry', dtype=col_types)
df_drinks.memory_usage(deep=True)


# Or instead of manually specifying the type, we can leverage a function to automatically perform the memory reduction for us.

# # Function to automatically perform downcasting
# <hr style = "border:2px solid black" ></hr>

# In[17]:


def reduce_mem_usage(df, blacklist_cols=None):
    """
    Iterate through all the columns of the dataframe and downcast the
    data type to reduce memory usage.

    The logic is numeric type will be downcast to the smallest possible
    numeric type. e.g. if an int column's value ranges from 1 - 8, then it
    fits into an int8 type, and will be downcast to int8.
    And object type will be converted to categorical type.

    Parameters
    ----------
    df : pd.DataFrame
        Dataframe prior the memory reduction.

    blacklist_cols : collection[str], e.g. list[str], set[str]
        A collection of column names that won't go through the memory
        reduction process.

    Returns
    -------
    df : pd.DataFrame
        Dataframe post memory reduction.

    References
    ----------
    https://www.kaggle.com/gemartin/load-data-reduce-memory-usage
    """
    start_mem = compute_df_total_mem(df)
    print('Memory usage of dataframe is {:.2f} MB'.format(start_mem))

    blacklist_cols = blacklist_cols if blacklist_cols else set()
    for col in df.columns:
        if col in blacklist_cols:
            continue

        col_type = df[col].dtype

        if col_type != object:
            c_min = df[col].min()
            c_max = df[col].max()
            if str(col_type)[:3] == 'int':
                if c_min > np.iinfo(np.int8).min and c_max < np.iinfo(np.int8).max:
                    df[col] = df[col].astype(np.int8)
                elif c_min > np.iinfo(np.int16).min and c_max < np.iinfo(np.int16).max:
                    df[col] = df[col].astype(np.int16)
                elif c_min > np.iinfo(np.int32).min and c_max < np.iinfo(np.int32).max:
                    df[col] = df[col].astype(np.int32)
                else:
                    df[col] = df[col].astype(np.int64)
            else:
                if c_min > np.finfo(np.float16).min and c_max < np.finfo(np.float16).max:
                    df[col] = df[col].astype(np.float16)
                elif c_min > np.finfo(np.float32).min and c_max < np.finfo(np.float32).max:
                    df[col] = df[col].astype(np.float32)
                else:
                    df[col] = df[col].astype(np.float64)
        else:
            df[col] = df[col].astype('category')

    end_mem = compute_df_total_mem(df)
    print('Memory usage after optimization is: {:.2f} MB'.format(end_mem))
    print('Decreased by {:.1f}%'.format(
        100 * (start_mem - end_mem) / start_mem))
    return df


def compute_df_total_mem(df):
    """Returns a dataframe's total memory usage in MB."""
    return df.memory_usage(deep=True).sum() / 1024 ** 2


# In[18]:


df_drinks = pd.read_csv('http://bit.ly/drinksbycountry')
df_drinks = reduce_mem_usage(df_drinks, blacklist_cols=['country'])
df_drinks.memory_usage(deep=True)


# # Conclusions
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-danger">
# <font color=black>
# 
# - Less than 100 MB Pandas is OK
# - More than >100 Mb to xx GBs Pandas starts to suffer
# - In this second case people start contemplating Spark which can handle several GBs or even TBs.
# - However, Spark lack a rich feature sets for high quality data cleaning, exploration, and analysis.
# - **Bottom line?** For For medium-sized data, we're better off trying to get more out of pandas, rather than switching to a different tool.
# 
# </font>
# </div>

# # References
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# - [This notebook](http://nbviewer.jupyter.org/github/ethen8181/machine-learning/blob/master/python/pandas/pandas.ipynb)
# - [Code to automatically reduced the memory footprint](https://www.kaggle.com/gemartin/load-data-reduce-memory-usage)
# - [Blog: Pandas Categoricals](https://www.continuum.io/content/pandas-categoricals)
# - [Blog: Using pandas with large data](https://www.dataquest.io/blog/pandas-big-data/)
# - [Youtube: How do I make my pandas DataFrame smaller and faster?](https://www.youtube.com/watch?v=wDYDYGyN_cw)
# - [How did I convert the 33 GB Dataset into a 3 GB file Using Pandas?](https://medium.com/aatomz-research/how-did-i-convert-the-33-gb-dataset-into-a-3-gb-file-using-pandas-b21d8da205c0)
# 
# </font>
# </div>

# # Requirements
# <hr style = "border:2px solid black" ></hr>

# In[ ]:


get_ipython().run_line_magic('load_ext', 'watermark')
get_ipython().run_line_magic('watermark', '-v -iv')


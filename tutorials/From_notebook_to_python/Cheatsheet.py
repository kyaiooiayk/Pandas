#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span><ul class="toc-item"><li><span><a href="#How-to-reshuffle-dataset" data-toc-modified-id="How-to-reshuffle-dataset-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>How to reshuffle dataset</a></span></li><li><span><a href="#General-global-options" data-toc-modified-id="General-global-options-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>General global options</a></span></li><li><span><a href="#Creating-a-pandas-dataset-from-scratch" data-toc-modified-id="Creating-a-pandas-dataset-from-scratch-1.3"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Creating a pandas dataset from scratch</a></span></li><li><span><a href="#Adding-a-row" data-toc-modified-id="Adding-a-row-1.4"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>Adding a row</a></span></li><li><span><a href="#Adding-a-new-columns" data-toc-modified-id="Adding-a-new-columns-1.5"><span class="toc-item-num">1.5&nbsp;&nbsp;</span>Adding a new columns</a></span></li><li><span><a href="#Getting-a-specific-row" data-toc-modified-id="Getting-a-specific-row-1.6"><span class="toc-item-num">1.6&nbsp;&nbsp;</span>Getting a specific row</a></span></li><li><span><a href="#Selecting-column/columns" data-toc-modified-id="Selecting-column/columns-1.7"><span class="toc-item-num">1.7&nbsp;&nbsp;</span>Selecting column/columns</a></span></li><li><span><a href="#Selecting-row/rows" data-toc-modified-id="Selecting-row/rows-1.8"><span class="toc-item-num">1.8&nbsp;&nbsp;</span>Selecting row/rows</a></span></li><li><span><a href="#Get-the-value-under-a-specific-column" data-toc-modified-id="Get-the-value-under-a-specific-column-1.9"><span class="toc-item-num">1.9&nbsp;&nbsp;</span>Get the value under a specific column</a></span></li><li><span><a href="#Get-the-row-indeces" data-toc-modified-id="Get-the-row-indeces-1.10"><span class="toc-item-num">1.10&nbsp;&nbsp;</span>Get the row indeces</a></span></li><li><span><a href="#Profiling" data-toc-modified-id="Profiling-1.11"><span class="toc-item-num">1.11&nbsp;&nbsp;</span>Profiling</a></span></li><li><span><a href="#meta-dataframe" data-toc-modified-id="meta-dataframe-1.12"><span class="toc-item-num">1.12&nbsp;&nbsp;</span>meta dataframe</a></span></li><li><span><a href="#Hihghligh-and-bold-an-entry" data-toc-modified-id="Hihghligh-and-bold-an-entry-1.13"><span class="toc-item-num">1.13&nbsp;&nbsp;</span>Hihghligh and bold an entry</a></span></li><li><span><a href="#Sorting-by-column" data-toc-modified-id="Sorting-by-column-1.14"><span class="toc-item-num">1.14&nbsp;&nbsp;</span>Sorting by column</a></span></li><li><span><a href="#Changing-the-type-of-entries" data-toc-modified-id="Changing-the-type-of-entries-1.15"><span class="toc-item-num">1.15&nbsp;&nbsp;</span>Changing the type of entries</a></span></li><li><span><a href="#Changing-values-in-a-column" data-toc-modified-id="Changing-values-in-a-column-1.16"><span class="toc-item-num">1.16&nbsp;&nbsp;</span>Changing values in a column</a></span></li><li><span><a href="#Get-the-row-values-for-a-particular-number" data-toc-modified-id="Get-the-row-values-for-a-particular-number-1.17"><span class="toc-item-num">1.17&nbsp;&nbsp;</span>Get the row values for a particular number</a></span></li><li><span><a href="#Swap-columns-with-raws" data-toc-modified-id="Swap-columns-with-raws-1.18"><span class="toc-item-num">1.18&nbsp;&nbsp;</span>Swap columns with raws</a></span></li><li><span><a href="#Dropping-a-column" data-toc-modified-id="Dropping-a-column-1.19"><span class="toc-item-num">1.19&nbsp;&nbsp;</span>Dropping a column</a></span></li><li><span><a href="#Dropping-a-column-that-contatins-a-string" data-toc-modified-id="Dropping-a-column-that-contatins-a-string-1.20"><span class="toc-item-num">1.20&nbsp;&nbsp;</span>Dropping a column that contatins a string</a></span></li><li><span><a href="#List-column-that-start-with-a-string" data-toc-modified-id="List-column-that-start-with-a-string-1.21"><span class="toc-item-num">1.21&nbsp;&nbsp;</span>List column that start with a string</a></span></li><li><span><a href="#Dropping-a-column-that-contains-?" data-toc-modified-id="Dropping-a-column-that-contains-?-1.22"><span class="toc-item-num">1.22&nbsp;&nbsp;</span>Dropping a column that contains <code>?</code></a></span></li><li><span><a href="#Getting-rid-of-the-row-that-have-a-null-value" data-toc-modified-id="Getting-rid-of-the-row-that-have-a-null-value-1.23"><span class="toc-item-num">1.23&nbsp;&nbsp;</span>Getting rid of the row that have a null value</a></span></li><li><span><a href="#Percentage-of-null-value-per-column" data-toc-modified-id="Percentage-of-null-value-per-column-1.24"><span class="toc-item-num">1.24&nbsp;&nbsp;</span>Percentage of null value per column</a></span></li><li><span><a href="#Updating-iteratively-the-value-of-a-columns" data-toc-modified-id="Updating-iteratively-the-value-of-a-columns-1.25"><span class="toc-item-num">1.25&nbsp;&nbsp;</span>Updating iteratively the value of a columns</a></span></li><li><span><a href="#Iterating-through-a-column-in-pandas" data-toc-modified-id="Iterating-through-a-column-in-pandas-1.26"><span class="toc-item-num">1.26&nbsp;&nbsp;</span>Iterating through a column in pandas</a></span></li><li><span><a href="#From-xls-to-pandas-dataframe" data-toc-modified-id="From-xls-to-pandas-dataframe-1.27"><span class="toc-item-num">1.27&nbsp;&nbsp;</span>From xls to pandas dataframe</a></span></li><li><span><a href="#When-the-excel-file-has-more-than-one-page" data-toc-modified-id="When-the-excel-file-has-more-than-one-page-1.28"><span class="toc-item-num">1.28&nbsp;&nbsp;</span>When the excel file has more than one page</a></span></li><li><span><a href="#Filtering-categorical-features" data-toc-modified-id="Filtering-categorical-features-1.29"><span class="toc-item-num">1.29&nbsp;&nbsp;</span>Filtering categorical features</a></span></li><li><span><a href="#Display-full-contents-of-a-dataframe" data-toc-modified-id="Display-full-contents-of-a-dataframe-1.30"><span class="toc-item-num">1.30&nbsp;&nbsp;</span>Display full contents of a dataframe</a></span></li><li><span><a href="#Save-locally-the-pandas-table" data-toc-modified-id="Save-locally-the-pandas-table-1.31"><span class="toc-item-num">1.31&nbsp;&nbsp;</span>Save locally the pandas table</a></span></li><li><span><a href="#From-object-to-float64-conversion" data-toc-modified-id="From-object-to-float64-conversion-1.32"><span class="toc-item-num">1.32&nbsp;&nbsp;</span>From object to float64 conversion</a></span></li><li><span><a href="#Changing-columns-name" data-toc-modified-id="Changing-columns-name-1.33"><span class="toc-item-num">1.33&nbsp;&nbsp;</span>Changing columns name</a></span></li><li><span><a href="#Renaming-a-particulat-column" data-toc-modified-id="Renaming-a-particulat-column-1.34"><span class="toc-item-num">1.34&nbsp;&nbsp;</span>Renaming a particulat column</a></span></li><li><span><a href="#Get-quick-statistics" data-toc-modified-id="Get-quick-statistics-1.35"><span class="toc-item-num">1.35&nbsp;&nbsp;</span>Get quick statistics</a></span></li><li><span><a href="#Applying-changes-to-multiple-columns" data-toc-modified-id="Applying-changes-to-multiple-columns-1.36"><span class="toc-item-num">1.36&nbsp;&nbsp;</span>Applying changes to multiple columns</a></span></li><li><span><a href="#Tilde-~-operator" data-toc-modified-id="Tilde-~-operator-1.37"><span class="toc-item-num">1.37&nbsp;&nbsp;</span>Tilde <code>~</code> operator</a></span></li><li><span><a href="#Missing-values" data-toc-modified-id="Missing-values-1.38"><span class="toc-item-num">1.38&nbsp;&nbsp;</span>Missing values</a></span></li><li><span><a href="#Filling-NaN-values" data-toc-modified-id="Filling-NaN-values-1.39"><span class="toc-item-num">1.39&nbsp;&nbsp;</span>Filling NaN values</a></span></li><li><span><a href="#Updating-index" data-toc-modified-id="Updating-index-1.40"><span class="toc-item-num">1.40&nbsp;&nbsp;</span>Updating index</a></span></li><li><span><a href="#if-test" data-toc-modified-id="if-test-1.41"><span class="toc-item-num">1.41&nbsp;&nbsp;</span>if-test</a></span></li><li><span><a href="#tqdm" data-toc-modified-id="tqdm-1.42"><span class="toc-item-num">1.42&nbsp;&nbsp;</span>tqdm</a></span></li><li><span><a href="#SQL-like-commands" data-toc-modified-id="SQL-like-commands-1.43"><span class="toc-item-num">1.43&nbsp;&nbsp;</span>SQL-like commands</a></span></li></ul></li><li><span><a href="#References" data-toc-modified-id="References-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>References</a></span></li><li><span><a href="#Requirements" data-toc-modified-id="Requirements-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Requirements</a></span></li></ul></div>

# # Introduction

# <div class="alert alert-block alert-warning">
# <font color=black>
#  
# **What?** Pandas cheatsheet
# 
# </font>
# </div>

# ## How to reshuffle dataset

# - It allows you to randomly select rows from a DataFrame. The function takes several parameters that allow you to control the sampling process, such as the number of rows to return, and whether or not to sample with replacement and seed for reproducibility.
# - Parameter `frac` as 1, it determines what fraction of total instances need to be returned.

# In[ ]:


df = df.sample(frac=1)


#  ## General global options

# In[ ]:


# Control number of displayed columns
pd.set_option("display.max_columns", 50)
# Control number of displayed rows
pd.set_option("display.max_rows", 50)
# Suppress scientific notation
pd.set_option('display.float_format', lambda x: '%.5f' % x)


# ## Creating a pandas dataset from scratch

# In[ ]:


lst = [[1,2,3], [4,5,6]]
df = pd.DataFrame(lst, columns = ["DV0", "DV1", "DV2"])


# In[2]:


import pandas as pd
# create a simple dataset of people
data = {'Name': ["John", "Anna", "Peter", "Linda"],
            'Location' : ["New York", "Paris", "Berlin", "London"],
            'Age' : [24, 13, 53, 33]
}
data_pandas = pd.DataFrame(data)
# IPython.display allows "pretty printing" of dataframes # in the Jupyter notebook
display(data_pandas)


# ## Adding a row

# In[36]:


df = pd.DataFrame([[1, 2], [3, 4]], columns=list('AB'))


# In[37]:


df


# In[43]:


df2 = pd.DataFrame([[5, 6], [7, 8]], columns=list('AB'))
df.append(df2)


# ## Adding a new columns

# In[26]:


import pandas as pd

df = pd.read_csv(
    'https://raw.githubusercontent.com/rasbt/python_reference/master/Data/some_soccer_data.csv')
df


# In[27]:


df['team'] = pd.Series('', index=df.index)
df


# In[28]:


df.insert(loc=8, column='position', value='') 
df


# ## Getting a specific row

# In[1]:


# imports
import pandas as pd
  
# creating a DataFrame
data = {'1' : ['g', 'e', 'e'], 
        '2' : ['k', 's', 'f'], 
        '3' : ['o', 'r', 'g'], 
        '4' : ['e', 'e', 'k']}
df = pd.DataFrame(data)
print("Original DataFrame")
display(df)
  
print("Value of row 1")

df.iloc[1]


# ## Selecting column/columns

# In[ ]:


pandasDataFrame["columName"]


# In[ ]:


pandasDataFrame[["columName#1", "columName#2"]]


# In[ ]:


# Get the index of columns
pandasDataFrame.columns.get_loc("columName")


# ## Selecting row/rows

# In[ ]:


# selection by row index
pandasDataFrame.iloc[1]


# In[ ]:


# selection by row value
pandasDataFrame.iloc[<value of the row>]


# In[ ]:


# .iat and is much faster than .iloc for selecting a single element from a DataFrame
pandasDataFrame.iat[1]


# In[ ]:


# .at and is much faster than .loc for selecting a single element from a DataFrame
pandasDataFrame.at[<value of the row>]


# ## Get the value under a specific column

# In[ ]:


# return a numpy array
pandasDataFrame["columName"].values


# ## Get the row indeces

# In[ ]:


pandasDataFrame.index.values


# ## Profiling

# In[ ]:


# pip install pandas-profiling
import pandas_profiling
pandas_profiling.ProfileReport(df)

pfr = pandas_profiling.ProfileReport(df)
pfr.to_file("./example.html")


# ## meta dataframe

# In[ ]:


# assuming the index.name is not null
l_order = [df.index.name] + df.columns.tolist()
# is a DF with MetaData
df_meta = pfr.description_set['variables'].loc[l_order]

print df_meta.shape
df_meta.head(4)

# E.g, pfr.description_set['variables']['type'] is the columns type:
# Numeric
# Categorical
# Boolean
# Date
#Text (Unique)
# Rejected
# Unsupported


# ## Hihghligh and bold an entry

# In[2]:


# importing the module
import pandas as pd

# Functions


def highlight_min(x):
    x_min = x.min()
    return ['background: yellow' if v == x_min else '' for v in x]


def bold_min(x):
    x_min = x.min()
    return ['font-weight: bold' if v == x_min else '' for v in x]


# creating a dummy DataFrame
data = {'a': [1, 2, 3],
        'b': [50, 21, 23],
        'd': [3, 2, 1]}
df = pd.DataFrame(data)

# Visualise the highlighted df
df.style.apply(highlight_min).apply(bold_min)


# ## Sorting by column

# In[5]:


import pandas as pd
a = pd.DataFrame()
a["value"] = [1, 4, -6, 15]
a["letter"] = ["a", "b", "c", "d"]
a.sort_values(by=['value'], inplace=True, ascending=True)


# In[6]:


a


# ## Changing the type of entries

# In[ ]:


# Converting column type
df = df.astype("float")


# ## Changing values in a column

# In[21]:


import pandas as pd

df = pd.read_csv(
    'https://raw.githubusercontent.com/rasbt/python_reference/master/Data/some_soccer_data.csv')
df


# In[25]:


# Processing `salary` column
df['SALARY'] = df['SALARY'].apply(lambda x: x.strip('$m'))
df


# ## Get the row values for a particular number

# In[ ]:


df.iloc[170]


# ## Swap columns with raws

# In[ ]:


q=pd.DataFrame()
q.T


# ## Dropping a column

# In[ ]:


import copy
# Just make copy to keep the two dataset separate
dfnew = copy.deepcopy(df)
dfnew.drop(columns = ["ColumnName#1", "ColumnName2", ""], inplace = True)


# ## Dropping a column that contatins a string

# In[ ]:


dft = df[df.columns.drop(list(df.filter(regex='string_to_search_*')))]


# ## List column that start with a string

# In[ ]:


df.filter(regex=r'^string')


# ## Dropping a column that contains `?`

# In[ ]:


df = pd.read_csv("../dataset.csv")
df = df.replace("?", np.NaN)
df = df.dropna(how = 'any', axis = 0) 


# In[ ]:


# if you have -inf
df = df.replace(-np.inf, np.NaN)
df = df.dropna(how = 'any', axis = 0) 


# ## Getting rid of the row that have a null value

# In[ ]:


df = df.dropna(how = 'any', axis = 0) 


# ## Percentage of null value per column

# In[ ]:


# This one will give you the percentage of data missing
df.isnull().mean()*100


# ## Updating iteratively the value of a columns

# In[ ]:


for index, row in allScrapedDataClean.iterrows():    
    if "apartment" in row["type"].split():        
        allScrapedDataClean.at[index, "type"] = "apartment"
    else:        
        allScrapedDataClean.at[index, "type"] = "house"


# ## Iterating through a column in pandas

# In[ ]:


for index, row in df.iterrows():    
    print(row["ColumnName"])


# ## From xls to pandas dataframe

# In[ ]:


df = pd.read_excel("../DATASETS/Concrete_Data.xls")


# ## When the excel file has more than one page

# In[ ]:


# read the excel file
Excel_file = pd.ExcelFile("../DATASETS/COE.xls")
# How many sheets are there? Just one.
print(Excel_file.sheet_names)
# Selecting only one page
spreadsheet = Excel_file.parse("COE data")


# ## Filtering categorical features

# In[ ]:


# List of categorical columns
categoricalcolumns = df.select_dtypes(include=["object"]).columns.tolist()
print("Names of categorical columns : ", categoricalcolumns)
# Get location of categorical columns
cat_features = [df.columns.get_loc(col) for col in categoricalcolumns]
print("Location of categorical columns : ", cat_features)


# ## Display full contents of a dataframe

# [Reference](https://thispointer.com/python-pandas-how-to-display-full-dataframe-i-e-print-all-rows-columns-without-truncation/)

# In[ ]:


pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)


# ## Save locally the pandas table

# In[ ]:


df.to_latex('./summary_table.txt')


# ## From object to float64 conversion

# In[ ]:


#https://stackoverflow.com/questions/28277137/how-to-convert-datatypeobject-to-float64-in-python
import pandas as pd
dfc = dfc.apply(lambda col:pd.to_numeric(col, errors='coerce'))
dfc.info()


# ## Changing columns name

# In[1]:


import pandas as pd
df = pd.read_csv(
    'https://raw.githubusercontent.com/rasbt/python_reference/master/Data/some_soccer_data.csv')
df


# In[2]:


# Option #1 - Converting column names to lowercase
df.columns = [c.lower() for c in df.columns]
df


# In[3]:


# Option #2 - Converting column names to lowercase
df.rename(columns=lambda x : x.lower())


# ## Renaming a particulat column

# In[4]:


import pandas as pd
df = pd.read_csv(
    'https://raw.githubusercontent.com/rasbt/python_reference/master/Data/some_soccer_data.csv')
df


# In[6]:


df = df.rename(columns={'p': 'points', 
                        'gp': 'games',
                        'sot': 'shots_on_target',
                        'g': 'goals',
                        'ppg': 'points_per_game',
                        'a': 'assists',})

df


# ## Get quick statistics

# In[7]:


import pandas as pd
df = pd.read_csv(
    'https://raw.githubusercontent.com/rasbt/python_reference/master/Data/some_soccer_data.csv')
df


# In[20]:


stats = df.isna().mean().reset_index(name="miss_per").sort_values("miss_per", ascending=False)
stats = stats.merge(df.dtypes.reset_index(name="datatype"))
stats = stats.merge(df.apply(lambda col : col.unique()).reset_index(name="unique_values"))
stats["miss_per"] = stats["miss_per"]*100
#stats["miss_per"] = stats[stats["miss_per"]>0]
stats


# ## Applying changes to multiple columns

# In[29]:


import pandas as pd
df = pd.read_csv(
    'https://raw.githubusercontent.com/rasbt/python_reference/master/Data/some_soccer_data.csv')
df


# In[33]:


cols = ['GP', 'G']
df[cols] = df[cols].applymap(lambda x: x+1)
df


# ## Tilde `~` operator

# In[49]:


import pandas as pd

# Creating a dictionary
d = {
    'Actor': ['Amit', 'Nawaz', 'Manoj'],
    'Web-Series': ['Avrodh', 'Sacred Games', 'The Family Man'],
    'Platform': ['Sony liv', 'Netflix', 'Prime']
}

# Creating a DataFrame
df = pd.DataFrame(d)
df


# In[52]:


# Select those that contain Netflix
df[df['Platform'].str.contains('Netflix')]


# In[53]:


# Select those that do not contain Netflix
df[~df['Platform'].str.contains('Netflix')]


# ## Missing values

# In[1]:


import pandas as pd

df = pd.read_csv(
    'https://raw.githubusercontent.com/rasbt/python_reference/master/Data/some_soccer_data.csv')
df


# In[3]:


df[df['A'].isnull()]


# In[8]:


df[df['A'].notnull()]


# In[9]:


# Using the tilde operator
df[~df['A'].isnull()]


# In[6]:


Check if there are any missing values
df.isnull().sum().any()


# ## Filling NaN values

# In[15]:


import pandas as pd

df = pd.read_csv(
    'https://raw.githubusercontent.com/rasbt/python_reference/master/Data/some_soccer_data.csv')
df


# In[16]:


df[df['A'].isnull()]


# In[17]:


df.fillna(value="Imputed", inplace=True)


# In[18]:


df


# ## Updating index

# In[53]:


import pandas as pd

df = pd.read_csv(
    'https://raw.githubusercontent.com/rasbt/python_reference/master/Data/some_soccer_data.csv')
df


# In[54]:


df.set_index('PLAYER', inplace=True)
df


# In[55]:


# Reset the indices
df.reset_index(inplace=True, drop=True)
df


# ## if-test

# In[59]:


import pandas as pd

a = [[2., .3, 4., 5.], [.8, .03, 0.02, 5.]]
df = pd.DataFrame(a)
df


# In[60]:


df <0.05


# In[61]:


df = df<0.5
df.astype(int)


# ## tqdm

# In[ ]:


import pandas as pd
import numpy as np
from tqdm import tqdm


# In[14]:


df = pd.DataFrame(np.random.randint(0, 100, (100, 100)))

# print first 10 rows and first 5 columns
df.head(10).iloc[:, :5]


# In[15]:


tqdm.pandas(desc='pandas tqdm integration demo')

df = df.progress_apply(lambda number: number + 5)  # add 5 to each number
print(df.head(10).iloc[:, :5])


# ## SQL-like commands

# - It allows you to filter a DataFrame based on a Boolean expression.
# - It allows you to select rows from a DataFrame using a query string similar to SQL.
# - The function returns a new DataFrame containing only the rows that satisfy the Boolean expression.

# In[2]:


import pandas as pd

df = pd.read_csv(
    'https://raw.githubusercontent.com/rasbt/python_reference/master/Data/some_soccer_data.csv')
df.head()


# In[5]:


df.query("SOT > 5 and PPG < 10")


# # References
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-block alert-warning">
# <font color=black>
#  
# - https://nbviewer.org/github/rasbt/python_reference/blob/master/tutorials/things_in_pandas.ipynb
# 
# </font>
# </div>

# # Requirements
# <hr style="border:2px solid black"> </hr>

# In[34]:


get_ipython().run_line_magic('load_ext', 'watermark')
get_ipython().run_line_magic('watermark', '-v -iv')


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import time
import numpy as np


# The first dataset is the Poker card game dataset which is shown below:
# 
# 

# In[2]:


poker_data = pd.read_csv('./poker_hand.csv')
poker_data.head()


# In each poker round, each player has five cards in hand, each one characterized by its symbol, which can be either hearts, diamonds, clubs, or spades, and its rank, which ranges from 1 to 13. The dataset consists of every possible combination of five cards one person can possess.
# 
# * Sn: symbol of the n-th card where: 1 (Hearts), 2 (Diamonds), 3 (Clubs), 4 (Spades)
# * Rn: rank of the n-th card where: 1 (Ace), 2–10, 11 (Jack), 12 (Queen), 13 (King)

# ## 3. Iterate Effectively Through Pandas DataFrame
# 

# As a data scientist, you will need to iterate through your dataframe extensively, especially in the data preparation and exploration phase, so it is important to be able to do this efficiently, as it will save you much time and give space for more important work. We will walk through three methods to make your loops much faster and more efficient:
# 
# * Looping using the .iterrows() function
# * Looping using the .apply() function
# * Vectorization
# 

# ### 3.1. Looping effectively using .iterrows()
# Before we talk about how to use the .iterrows() function to improve the looping process, let’s refresh the notion of a generator function.
# 
# Generators are a simple tool to create iterators. Inside the body of a generator, instead of return statements, you will find only yield() statements. There can be just one, or several yield() statements. Here, we can see a generator, city_name_generator(), that produces four city names. We assign the generator to the variable city_names for simplicity.
# 
# 

# In[3]:


def city_name_generator():
    yield ('New York')
    yield ('London')
    yield ('Tokyo')
    yield ('Sao Paolo')


city_names = city_name_generator()


# To access the elements that the generator yields we can use Python’s next() function. Each time the next() command is used, the generator will produce the next value to yield, until there are no more values to yield. We here have 4 cities. Let’s run the next command four times and see what it returns:
# 
# 

# In[4]:


next(city_names)


# In[5]:


next(city_names)


# In[6]:


next(city_names)


# In[7]:


next(city_names)


# As we can see that every time we run the next() function it will print a new city name.
# 
# 

# Let's go back to the .iterrows() function. The .iterrows() function is a property of every pandas DataFrame. When called, it produces a list with two elements. We will use this generator to iterate through each line of our poker DataFrame. The first element is the index of the row, while the second element contains a pandas Series of each feature of the row: the Symbol and the Rank for each of the five cards. It is very similar to the notion of the enumerate() function, which when applied to a list, returns each element along with its index.
# 
# The most intuitive way to iterate through a Pandas DataFrame is to use the range() function, which is often called crude looping. This is shown with the code below:
# 
# 

# In[8]:


start_time = time.time()
for index in range(poker_data.shape[0]):
    next
print("Time using range(): {} sec".format(time.time() - start_time))


# One smarter way to iterate through a pandas DataFrame is to use the **.iterrows()** function, which is optimized for this task. We simply define the **‘for’** loop with two iterators, one for the number of each row and the other for all the values.
# 
# Inside the loop, the **next()** command indicates that the loop moves to the next value of the iterator, without actually doing something.

# In[9]:


data_generator = poker_data.iterrows()
start_time = time.time()
for index, values in data_generator:
    next
print("Time using .iterrows(): {} sec".format(time.time() - start_time))


# Comparing the two computational times we can also notice that the use of .iterrows() does not improve the speed of iterating through pandas DataFrame. It is very useful though when we need a cleaner way to use the values of each row while iterating through the dataset.
# 

# ### 3.2. Looping effectively using .apply()

# Now we will use the **.apply()** function to be able to perform a specific task while iterating through a pandas DataFrame. The **.apply()** function does exactly what it says; it applies another function to the whole DataFrame.
# 
# The syntax of the **.apply()** function is simple: we create a mapping, using a lambda function in this case, and then declare the function we want to apply to every cell. Here, we’re applying the square root function to every cell of the DataFrame. In terms of speed, it matches the speed of just using the NumPy sqrt() function over the whole DataFrame.
# 

# In[10]:


data_sqrt = poker_data.apply(lambda x: np.sqrt(x), axis =0 )
data_sqrt.head()


# This is a simple example since we would like to apply this function to the dataframe.
# 
# But what happens when the function of interest is taking more than one cell as an input? For example, what if we want to calculate the sum of the rank of all the cards in each hand? In this case, we will use the .apply() function the same way as we did before, but we need to add ‘axis=1’ at the end of the line to specify we’re applying the function to each row.
# 
# 

# In[11]:


apply_start_time = time.time()
poker_data[['R1', 'R2', 'R3', 'R4', 'R5']].apply(lambda x: sum(x), axis=1)
apply_end_time = time.time()
apply_time = apply_end_time - apply_start_time
print("Time using .apply(): {} sec".format(apply_time))


# Then, we will use the .iterrows() function we saw previously, and compare their efficiency.
# 
# 

# In[12]:


for_loop_start_time = time.time()
for ind, value in poker_data.iterrows():
    sum([value[1], value[3], value[5], value[7], value[9]])
for_loop_end_time = time.time()

for_loop_time = for_loop_end_time - for_loop_start_time
print("Time using .iterrows(): {} sec".format(for_loop_time))


# Using the .apply() function is significantly faster than the .iterrows() function, with a magnitude of around 400 percent, which is a massive improvement!
# 
# 

# In[13]:


print('The differnce: {} %'.format((for_loop_time - apply_time) / apply_time * 100))


# As we did with rows, we can do exactly the same thing for the columns; apply one function to each column. By replacing the axis=1 with axis=0, we can apply the sum function on every column.
# 
# 

# In[14]:


apply_start_time = time.time()
poker_data[['R1', 'R2', 'R3', 'R4', 'R5']].apply(lambda x: sum(x), axis=0)
apply_end_time = time.time()
apply_time = apply_end_time - apply_start_time
print("Time using .apply(): {} sec".format(apply_time))


# By comparing the **.apply()** function with the native panda's function for summing over rows, we can see that pandas’ native .sum() functions perform the same operation faster.
# 
# 

# In[15]:


pandas_start_time = time.time()
poker_data[['R1', 'R1', 'R3', 'R4', 'R5']].sum(axis=0)
pandas_end_time = time.time()
pandas_time = pandas_end_time - pandas_start_time
print("Time using pandas: {} sec".format(pandas_time))


# In[16]:


print('The differnce: {} %'.format((apply_time - pandas_time) / pandas_time * 100))


# In conclusion, we observe that the .apply() function performs faster when we want to iterate through all the rows of a pandas DataFrame, but is slower when we perform the same operation through a column.
# 
# 

# ### 3.3.Looping effectively using vectorization

# To understand how we can reduce the amount of iteration performed by the function, recall that the fundamental units of Pandas, DataFrames, and Series, are both based on arrays. Pandas perform more efficiently when an operation is performed to a whole array than to each value separately or sequentially. This can be achieved through vectorization. Vectorization is the process of executing operations on entire arrays.
# 
# In the code below we want to calculate the sum of the ranks of all the cards in each hand. In order to do that, we slice the poker dataset keeping only the columns that contain the ranks of each card. Then, we call the built-in .sum() property of the DataFrame, using the parameter axis = 1 to denote that we want the sum for each row. In the end, we print the sum of the first five rows of the data.
# 
# 

# In[17]:


start_time_vectorization = time.time()

poker_data[['R1', 'R2', 'R3', 'R4', 'R5']].sum(axis=1)
end_time_vectorization = time.time()

vectorization_time = end_time_vectorization  - start_time_vectorization
print("Time using pandas vectorization: {} sec".format(vectorization_time))


# We saw previously various methods that perform functions applied to a DataFrame faster than simply iterating through all the rows of the DataFrame. Our goal is to find the most efficient method to perform this task.
# 
# 

# Using .iterrows() to loop through the DataFrame:
# 

# In[18]:


data_generator = poker_data.iterrows()

start_time_iterrows = time.time()

for index, value in data_generator:
    sum([value[1], value[3], value[5], value[7]])

end_time_iterrows = time.time()
iterrows_time = end_time_iterrows - start_time_iterrows
print("Time using .iterrows() {} seconds " .format(iterrows_time))


# Using the .apply() mehtod
# 

# In[19]:


start_time_apply = time.time()
poker_data[['R1', 'R2', 'R3', 'R4', 'R5']].apply(lambda x: sum(x), axis=1)
end_time_apply = time.time()

apply_time = end_time_apply - start_time_apply

print("Time using apply() {} seconds"  .format(apply_time))


# Comparing the time it takes to sum the ranks of all the cards in each hand using vectorization, the .iterrows() function, and the .apply() function, we can see that the vectorization method performs much better.
# 
# We can also use another vectorization method to effectively iterate through the DataFrame which is using Numpy arrays to vectorize the DataFrame.
# 
# The NumPy library, which defines itself as a “fundamental package for scientific computing in Python”, performs operations under the hood in optimized, pre-compiled C code. Similar to pandas working with arrays, NumPy operates on arrays called ndarrays. A major difference between Series and ndarrays is that ndarrays leave out many operations such as indexing, data type checking, etc. As a result, operations on NumPy arrays can be significantly faster than operations on pandas Series. NumPy arrays can be used in place of the pandas Series when the additional functionality offered by the pandas Series isn’t critical.
# 
# For the problems we explore in this article, we could use NumPy ndarrays instead of the pandas series. The question at stake is whether this would be more efficient or not.
# 
# Again, we will calculate the sum of the ranks of all the cards in each hand. We convert our rank arrays from pandas Series to NumPy arrays simply by using the .values method of pandas Series, which returns a pandas Series as a NumPy ndarray. As with vectorization on the series, passing the NumPy array directly into the function will lead pandas to apply the function to the entire vector.
# 
# 

# In[20]:


start_time = time.time()

poker_data[['R1', 'R2', 'R3', 'R4', 'R5']].values.sum(axis=1)

print("Time using NumPy vectorization: {} sec" .format(time.time() - start_time))


# In[21]:


start_time = time.time()
poker_data[['R1', 'R2', 'R3', 'R4', 'R5']].sum(axis=1)
print("Time using the pandas vectorization %s seconds" % (time.time() - start_time))


# # Conclusions
# * Using **.iterrows()** does not improve the speed of iterating through the DataFrame but it is more efficient.
# * The **.apply()** function performs faster when we want to iterate through all the rows of a pandas DataFrame, but is slower when we perform the same operation through a column.
# * Vectorizing over the pandas series achieves the overwhelming majority of optimization needs for everyday calculations. However, if speed is of the highest priority, we can call in reinforcements in the form of the NumPy Python library.

# # References

# - https://github.com/timmajani/Efficient-Python-for-Data-Scientists/blob/main/Best_Practices_To_Use_Pandas_Efficiently_As_A_Data_Scientist.ipynb

# In[ ]:





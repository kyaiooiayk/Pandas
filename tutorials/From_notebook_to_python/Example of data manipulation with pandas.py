#!/usr/bin/env python
# coding: utf-8

# # Introduction

# <div class="alert alert-block alert-warning">
# <font color=black><br>
# 
# **What?** Example of data manipulation with pandas
# 
# <br></font>
# </div>

# # Import modules

# In[2]:


import pandas as pd


# # Load dataset

# <div class="alert alert-block alert-info">
# <font color=black><br>
# 
# - 'bike_rentals.csv' to dataFrame
# - We use this data with no other reason than the fact it provides some useful features to show case data manipulation 
# 
# <br></font>
# </div>

# In[3]:


df_bikes = pd.read_csv('../DATASETS/bike_rentals.csv')


# # Display first & last 5 rows

# In[4]:


df_bikes.head(5)


# In[5]:


df_bikes.tail()


# # Compute the 4 moments

# <div class="alert alert-block alert-info">
# <font color=black><br>
# 
# - Comparing the mean and median (50%) gives an indication of skewness. 
# - Id mean and median are close to one another, so the data is roughly symmetrical
# 
# <br></font>
# </div>

# In[7]:


df_bikes.describe()


# # Count non-null values and show type

# <div class="alert alert-block alert-info">
# <font color=black><br>
# 
# - As you can see, .info() gives the number of rows, number of columns, column types, and non-null values.
# - If non-null values differs between columns, null values must be present.
# 
# <br></font>
# </div>

# In[9]:


df_bikes.info()


# # Total number of null values

# <div class="alert alert-block alert-info">
# <font color=black><br>
# 
# - If null values are not corrected, unexpected errors may arise down the road.
# - Note that two .sum() methods are required. 
# - The first method sums the null values of each column, while the second method sums the column counts.
# - The following code displays the total number of null values
# 
# <br></font>
# </div>

# In[11]:


df_bikes.isna().sum().sum()


# # Visualise null values

# <div class="alert alert-block alert-info">
# <font color=black><br>
# 
# - Now we'd like to see those 12 values missing tagged as "NaN" = Not a Number
# - This code may be broken down as follows: df_bikes[conditional] is a subset of df_bikes that meets the condition in  brackets .df_bikes.isna().any gathers any and all null values while (axis=1) specifies values in the columns. 
# - In pandas, rows are axis 0 and columns are axis 1. 
# 
# <br></font>
# </div>

# In[13]:


df_bikes[df_bikes.isna().any(axis=1)]


# # Fill in null values

# <div class="alert alert-block alert-info">
# <font color=black><br>
# 
# - **df_bikes['windspeed'].fillna** means that the null values of the 'windspeed' column will be filled
# - **df_bikes['windspeed'].median()** is the median of the 'windspeed' column
# - **inplace=True ensures that the** changes are permanent
# - **Mean vs. Meadian?** The median is often a BETTER choice than the mean. 
# - The median guarantees that half the data is greater than the given value and half the data is lower. 
# - The mean, by contrast, is vulnerable to outliers.
# 
# <br></font>
# </div>

# In[15]:


# Fill windspeed null values with median
df_bikes['windspeed'].fillna((df_bikes['windspeed'].median()), inplace=True)


# In[16]:


# Display rows 56, 81, 128. Just checking if it has worked
df_bikes.iloc[[56, 81, 128]]


# <div class="alert alert-block alert-info">
# <font color=black><br>
# 
# - Groupby season with median offer some value we can use to crrect the humidity level that are missing as shown before.
# 
# <br></font>
# </div>

# In[18]:


df_bikes.groupby(['season']).median()


# <div class="alert alert-block alert-info">
# <font color=black><br>
# 
# - Convert 'hum' null values to median of season
# - To correct the null values in the hum column, short for humidity, we can take the median humidity by season.
# 
# <br></font>
# </div>

# In[20]:


df_bikes['hum'] = df_bikes['hum'].fillna(df_bikes.groupby('season')['hum'].transform('median'))


# In[21]:


# Show null values of 'temp' column
df_bikes[df_bikes['temp'].isna()]


# <div class="alert alert-block alert-info">
# <font color=black><br>
# 
# - When correcting temperature, aside from consulting historical records, taking the mean temperature of the day before and the day after should give a good estimate.
# 
# <br></font>
# </div>

# In[23]:


# Compute mean temp and atemp by row
mean_temp = (df_bikes.iloc[700]['temp'] + df_bikes.iloc[702]['temp'])/2
mean_atemp = (df_bikes.iloc[700]['atemp'] + df_bikes.iloc[702]['atemp'])/2

# Replace null values with mean temperatures
df_bikes['temp'].fillna((mean_temp), inplace=True)
df_bikes['atemp'].fillna((mean_atemp), inplace=True)


# # Drop a columns from dataset

# In[24]:


# Drop 'casual', 'registered' columns
df_bikes = df_bikes.drop(['casual', 'registered'], axis=1)
df_bikes.head(2)


# # Export 'bike_rentals_cleaned' csv file

# In[26]:


df_bikes.to_csv('bike_rentals_cleaned.csv', index=False)


# # Reference

# <div class="alert alert-block alert-warning">
# <font color=black>
# 
# - Corey Wade. “Hands-On Gradient Boosting with XGBoost and scikit-learn
# - https://github.com/PacktPublishing/Hands-On-Gradient-Boosting-with-XGBoost-and-Scikit-learn
# 
# </font>
# </div>

# In[ ]:





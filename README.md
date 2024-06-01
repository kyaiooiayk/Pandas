# Pandas
Notes, tutorials, code snippets and templates
***

## A note on the notebook rendering
Each notebook has two versions (all python scripts are unaffected by this):
- One where all the markdown comments are rendered in black& white. These are placed in the folder named `GitHub_MD_rendering` where MD stands for MarkDown.
- One where all the markdown comments are rendered in coloured. 
***

## Available tutorials
- [Automatic data profiling powered by Pandas](https://github.com/kyaiooiayk/Pandas-Notes/blob/main/tutorials/GitHub_MD_rendering/Automatic%20data%20profiling%20powered%20by%20Pandas.ipynb)
- [Cheatsheet](https://github.com/kyaiooiayk/Pandas-Notes/blob/main/tutorials/GitHub_MD_rendering/Cheatsheet.ipynb)
- [Complex selections](https://github.com/kyaiooiayk/Pandas-Notes/blob/main/tutorials/GitHub_MD_rendering/Complex%20selections.ipynb)
- [Concatenating, merging and joining](https://github.com/kyaiooiayk/Pandas-Notes/blob/main/tutorials/GitHub_MD_rendering/Concatenating%2C%20merging%20and%20joining.ipynb)
- [Efficiently iterating over rows in a Pandas DataFrame](https://github.com/kyaiooiayk/Pandas-Notes/blob/main/tutorials/GitHub_MD_rendering/Efficiently%20iterating%20over%20rows%20in%20a%20Pandas%20DataFrame.ipynb)
- [Example of data manipulation with pandas](https://github.com/kyaiooiayk/Pandas-Notes/blob/main/tutorials/GitHub_MD_rendering/Example%20of%20data%20manipulation%20with%20pandas.ipynb)
- [Feature engineering in Pandas](https://github.com/kyaiooiayk/Pandas-Notes/blob/main/tutorials/GitHub_MD_rendering/Feature%20engineering%20in%20Pandas.ipynb)
- [How to use Pandas for plotting](https://github.com/kyaiooiayk/Pandas-Notes/blob/main/tutorials/GitHub_MD_rendering/How%20to%20use%20Pandas%20for%20plotting.ipynb)
- [Introduction to Pandas object types](https://github.com/kyaiooiayk/Pandas-Notes/blob/main/tutorials/GitHub_MD_rendering/Introduction%20to%20Pandas%20object%20types.ipynb)
- [Optimising Pandas - reduce memory footprint](https://github.com/kyaiooiayk/Pandas-Notes/blob/main/tutorials/GitHub_MD_rendering/Optimising%20Pandas%20-%20reduce%20memory%20footprint.ipynb)
- [Pandas - code snippets](https://github.com/kyaiooiayk/Pandas-Notes/blob/main/tutorials/GitHub_MD_rendering/Pandas%20-%20code%20snippets.ipynb)
- [Pandas group-by](https://github.com/kyaiooiayk/Pandas-Notes/blob/main/tutorials/GitHub_MD_rendering/Pandas%20group-by.ipynb)
- [Pandas pivot and unstack table](https://github.com/kyaiooiayk/Pandas-Notes/blob/main/tutorials/GitHub_MD_rendering/Pandas%20pivot%20and%20unstack%20table.ipynb)
- [Performance aspects](https://github.com/kyaiooiayk/Pandas-Notes/blob/main/tutorials/GitHub_MD_rendering/Performance%20aspects.ipynb)
- [Simple Tricks To Speed up the Sum Calculation in Pandas](https://github.com/kyaiooiayk/Pandas-Notes/blob/main/tutorials/GitHub_MD_rendering/Simple%20Tricks%20To%20Speed%20up%20the%20Sum%20Calculation%20in%20Pandas.ipynb)
***

## When you need performance think about `polars`
- [polars](https://github.com/pola-rs/polars)
- Using Pandas is good for prototyping, but it can be very slow when used in a training pipeline. Typical training pipelines use a lot of indexing and row-wise operations, and Pandas is not optimized for this. E.g. compare the performance of df.iloc[i] and array[i] to estimate the difference at scale of many millions of calls. When columns-wise operations are needed, we prefer to use polars — an optimized library with an API similar to Pandas, written in Rust.
- Although it is written in Rust, Polars has a Python package, which makes it a potential alternative to Pandas. Polars has two different APIs: an eager API and a lazy API. The eager execution is similar to Pandas. That means the code is run directly, and its results are returned immediately.
***

## GPU-power pandas
- [Mastering GPUs: A Beginner’s Guide to GPU-Accelerated DataFrames in Python](https://www.kdnuggets.com/2023/07/mastering-gpus-beginners-guide-gpu-accelerated-dataframes-python.html)
***

## Others
- [How fast can we process csv file in pandas](https://datapythonista.me/blog/how-fast-can-we-process-a-csv-file?utm_source=substack&utm_medium=email)
***

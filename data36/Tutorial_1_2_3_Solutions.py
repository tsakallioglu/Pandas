# Solutions to excercises found under the website;
# https://data36.com/pandas-tutorial-1-basics-reading-data-files-dataframes-data-selection/

import pandas as pd
import numpy as np
import datetime

# Pandas Tutorial 1: Pandas Basics (Reading Data Files, DataFrames, Data Selection)

### Read in the data files ###
article_read = pd.read_csv("C:/Users/Mehmet Sakallioglu/Desktop/pandas_tutorial_read.csv", delimiter = ";",
                       names = ['my_datetime', 'event', 'country', 'user_id', 'source', 'topic'])

# Exercise
# Select the user_id, the country and the topic columns for the users who are from country_2!
# Print the first five rows only!
print(article_read[article_read.country == "country_2"][["user_id", "country", "topic"]].head(5))




### Pandas Tutorial 2: Aggregation and Grouping ###
zoo = pd.read_csv("C:/Users/Mehmet Sakallioglu/Desktop/zoo.csv", delimiter = ',')

# Excercise 1
# What’s the most frequent source in the article_read dataframe?
print (article_read.groupby("source").count()["user_id"])


# Exercise 2
# For the users of country_2, what was the most frequent topic and source combination?
# Or in other words: which topic, from which source, brought the most views from country_2?
print (article_read[article_read.country == "country_2"].groupby(["topic", "source"]).count())




### Pandas Tutorial 3: Important Data Formatting Methods (merge, sort, reset_index, fillna) ###
zoo_eats = pd.DataFrame([['elephant','vegetables'], ['tiger','meat'], ['kangaroo','vegetables'],
                         ['zebra','vegetables'], ['giraffe','vegetables']], columns=['animal', 'food'])
blog_buy = pd.read_csv("C:/Users/Mehmet Sakallioglu/Desktop/pandas_tutorial_buy.csv", delimiter = ';',
                       names = ['my_date_time', 'event', 'user_id', 'amount'])

# Excercise 1
# What’s the average (mean) revenue between 2018-01-01 and 2018-01-07 from the users in the article_read dataframe?
article_read_buy = article_read.merge(blog_buy, how = 'left', left_on = 'user_id', right_on = 'user_id')

# Solution 1; looking at the users that only made a purchase
article_read_buy.my_datetime = pd.to_datetime(article_read_buy.my_datetime)
date_constraint = (article_read_buy.my_date_time >= '2018-01-01') & (article_read_buy.my_date_time <= '2018-01-07')
print (article_read_buy[date_constraint].amount.mean())

# Solution 2; taking an average considering the users that didn't buy anything as well
article_read_buy.amount = article_read_buy.amount.fillna(0)
print (article_read_buy.amount.mean())


# Exercise 2
# TASK #2: Print the top 3 countries by total revenue between 2018-01-01 and 2018-01-07!
# (Obviously, this concerns the users in the article_read dataframe again.)
print (article_read_buy.fillna(0).groupby('country').amount.sum().sort_values(ascending = False).head(3))



# Ex - GroupBy
# Introduction:
# GroupBy can be summarizes as Split-Apply-Combine.

# Step 1. Import the necessary libraries
import numpy as np
import pandas as pd

# Step 2. Import the dataset from this address.
# Step 3. Assign it to a variable called drinks.
drinks = pd.read_csv("https://raw.githubusercontent.com/justmarkham/DAT8/master/data/drinks.csv", delimiter = ",")

# Step 4. Which continent drinks more beer on average?
print (drinks.groupby("continent").beer_servings.sum().sort_values(ascending = False).index.values[0])

# Step 5. For each continent print the statistics for wine consumption.
print (drinks.groupby("continent").wine_servings.describe())

# Step 6. Print the mean alcoohol consumption per continent for every column
print (drinks.groupby("continent").mean())

# Step 7. Print the median alcoohol consumption per continent for every column
print (drinks.groupby("continent").median())

# Step 8. Print the mean, min and max values for spirit consumption.
# This time output a DataFrame
print (drinks.groupby("continent").spirit_servings.agg(["mean", 'min', 'max']))

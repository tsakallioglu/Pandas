
# Getting and Knowing your Data
# This time we are going to pull data directly from the internet

# Step 1. Import the necessary libraries
import pandas as pd
import numpy as np

# Step 2. Import the dataset from this address.
# Step 3. Assign it to a variable called chipo.
chipo = pd.read_csv("https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv", delimiter = "\t")

# Step 4. See the first 10 entries
print(chipo.head(10))

# Step 5. What is the number of observations in the dataset?
print(chipo.shape[0])

# Step 6. What is the number of columns in the dataset?
print(chipo.shape[1])

# Step 7. Print the name of all the columns.
print(chipo.columns.values)

# Step 8. How is the dataset indexed?
print(chipo.index)

# Step 9. Which was the most-ordered item?
print(chipo.groupby("item_name").quantity.sum().sort_values(ascending = False).head(1).index[0])

# Step 10. For the most-ordered item, how many items were ordered?
print(chipo.groupby("item_name").quantity.sum().sort_values(ascending = False).head(1)[0])

# Step 11. What was the most ordered item in the choice_description column?
print(chipo.groupby("choice_description").quantity.sum().sort_values(ascending = False).index[0])

# Step 12. How many items were orderd in total?
print(chipo.quantity.sum())

# Step 13. Turn the item price into a float
# Step 13.a. Check the item price type
print(chipo.item_price.dtype)

# Step 13.b. Create a lambda function and change the type of item price
chipo.item_price = chipo.item_price.apply(lambda x: float(x[1:]))

# Step 13.c. Check the item price type
print(chipo.item_price.dtype)

# Step 14. How much was the revenue for the period in the dataset?
print ("Revenue was: $" + str((chipo.quantity * chipo.item_price).sum()))

# Step 15. How many orders were made in the period?
print (len(chipo.order_id.unique()))

# Step 16. What is the average revenue amount per order?
chipo["revenue"] = chipo.quantity * chipo.item_price
print (chipo.groupby("order_id").sum().revenue.mean())

# Step 17. How many different items are sold?
print (len(chipo.item_name.unique()))


# Step 1
import pandas as pd
import numpy as np

# Step 2. Download the dataset to your computer and unzip it.
# Step 3. Use the tsv file and assign it to a dataframe called food
food = pd.read_csv("C:/Users/Mehmet Sakallioglu/Desktop/world-food-facts/en.openfoodfacts.org.products.tsv", delimiter = "\t")

# Step 4. See the first 5 entries
print (food.head(5))

# Step 5. What is the number of observations in the dataset?
print (food.shape[0])

# Step 6. What is the number of columns in the dataset?
print (food.shape[1])

# Step 7. Print the name of all the columns.
print (food.columns)

# Step 8. What is the name of 105th column?
print (food.columns[104])

# Step 9. What is the type of the observations of the 105th column?
print (food["-glucose_100g"].dtype)

# Step 10. How is the dataset indexed?
print (food.index)

# Step 11. What is the product name of the 19th observation?
print (food.product_name[18])

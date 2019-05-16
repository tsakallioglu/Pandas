# Step 1
import pandas as pd
import numpy as np

# Step 2. Import the dataset from this address.
# Step 3. Assign it to a variable called chipo.
chipo = pd.read_csv("https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv", delimiter = "\t")
chipo.item_price = [float(x[1:-1]) for x in chipo.item_price]

# Step 5. What is the price of each item?
print (chipo.drop_duplicates(["item_name", "quantity"])[chipo.quantity == 1][["item_name", "item_price"]].sort_values("item_price",ascending = False))

# Step 6. Sort by the name of the item
chipo = chipo.sort_values("item_name")

# Step 7. What was the quantity of the most expensive item ordered?
print (chipo.sort_values("item_price").tail(1).item_name.values)

# Step 8. How many times were a Veggie Salad Bowl ordered?
print (chipo[chipo.item_name == "Veggie Salad Bowl"].shape[0])

# Step 9. How many times people orderd more than one Canned Soda?
canned_soda_sum = chipo[chipo.item_name == "Canned Soda"].groupby("order_id").quantity.sum()

print (canned_soda_sum[canned_soda_sum > 1].count())

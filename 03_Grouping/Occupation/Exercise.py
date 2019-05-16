# Step 1. Import the necessary libraries
import numpy as np
import pandas as pd

# Step 2. Import the dataset from this address.
# Step 3. Assign it to a variable called users.
users = pd.read_csv("https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user", delimiter = "|")

# Step 4. Discover what is the mean age per occupation
print (users.groupby("occupation").age.mean().sort_values(ascending = False))

# Step 5. Discover the Male ratio per occupation and sort it from the most to the least
print ((users[users.gender == "M"].groupby('occupation').user_id.count() 
       / users.groupby('occupation').user_id.count() * 100).sort_values(ascending = False))

# Step 6. For each occupation, calculate the minimum and maximum ages
print (users.groupby('occupation').age.agg(['min', 'max']))

# Step 7. For each combination of occupation and gender, calculate the mean age
print (users.groupby(['occupation', 'gender']).age.mean())

# Step 8. For each occupation present the percentage of women and men
occup_count = users.groupby('occupation').age.count()
gender_count = users.groupby(['occupation', 'gender']).age.count()
print (gender_count.divide(occup_count, level = 'occupation') * 100)

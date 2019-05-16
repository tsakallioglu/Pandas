# Step 1. Import the necessary libraries
import pandas as pd
import numpy as np

# Step 2. Import the dataset from this address.
# Step 3. Assign it to a variable called df.
df = pd.read_csv("https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/Students_Alcohol_Consumption/student-mat.csv", delimiter = ',')

# Step 4. For the purpose of this exercise slice the dataframe from 'school' until the 'guardian' column
df = df.loc[:,'school':'guardian']

# Step 5. Create a lambda function that capitalize strings.
capitalizer = lambda x: x.upper()

# Step 6. Capitalize both Mjob and Fjob
df.Mjob = df.Mjob.apply(capitalizer)
df.Fjob = df.Fjob.apply(capitalizer)

# Step 7. Print the last elements of the data set.
print (df.tail())

# Step 8. Create a function called majority that return a boolean value to a new column called legal_drinker (Consider majority as older than 17 years old)
def majority(x):
    if x > 17:
        return True
    else:
        return False
    
df["legal_drinker"] = df.age.apply(majority)
    
# Step 9. Multiply every number of the dataset by 10.
# I know this makes no sense, don't forget it is just an exercise
def multp10(x):
    if type(x) is int:
        return 10 * x
    else:
        return x
    
df = df.applymap(multp10)

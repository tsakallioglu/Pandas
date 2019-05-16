# Step 1
import pandas as pd
import numpy as np

# Step 2. Import the dataset from this address.
# Step 3. Assign it to a variable called euro12.
euro12 = pd.read_csv("https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv", delimiter = ",")

# Step 4. Select only the Goal column.
print (euro12.Goals)

# Step 5. How many team participated in the Euro2012?
print (euro12.Team.nunique())

# Step 6. What is the number of columns in the dataset?
print (euro12.shape[1])

# Step 7. View only the columns Team, Yellow Cards and Red Cards and assign them to a dataframe called discipline
discipline = euro12[["Team", "Yellow Cards", "Red Cards"]]

# Step 8. Sort the teams by Red Cards, then to Yellow Cards
discipline = discipline.sort_values(["Red Cards", "Yellow Cards"], ascending = False)

# Step 9. Calculate the mean Yellow Cards given per Team
print (discipline["Yellow Cards"].mean())

# Step 10. Filter teams that scored more than 6 goals
print (euro12[["Team", "Goals"]][euro12.Goals > 5])

# Step 11. Select the teams that start with G
print (euro12[euro12.Team.str[0] == "G"])

# Step 12. Select the first 7 columns
print (euro12.iloc[:,:7])

# Step 13. Select all columns except the last 3.
print (euro12.iloc[:,:-3])

# Step 14. Present only the Shooting Accuracy from England, Italy and Russia
print (euro12[euro12.Team.isin(["England", "Italy", "Russia"])][["Team", "Shooting Accuracy"]])

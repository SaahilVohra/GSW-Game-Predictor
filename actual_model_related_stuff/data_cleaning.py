import pandas as pd
import numpy as np
from scipy import stats

combined_data = pd.read_csv('warriors_all_seasons_gamelog_with_opponents.csv')

#Inspect the data
print(combined_data.head())
print(combined_data.info())
print(combined_data.describe())

df = pd.DataFrame(combined_data)

#dealing with missing values by creating a boolean mask
mask = df.isnull().any(axis=1)

rows_with_missing_values = df[mask]

#since only a few rows have missing data, we can drop them
combined_data = combined_data.dropna()


#after dealing with missing values, now we deal with duplicates
duplicates = combined_data.duplicated()

#In this case, all duplicate rows are just rows with subheadings/headings so can be removed

combined_data = combined_data.drop_duplicates(keep=False)

#Check data types of each column and convert to ints/floats
print(combined_data.dtypes)
combined_data = combined_data.apply(pd.to_numeric, errors='coerce')

#After dealing with missing vals and duplicates, inspect outliers and anomalies using z-scores 

z_scores = np.abs(stats.zscore(combined_data))
z_scores_df = pd.DataFrame(z_scores)
outlier_mask = z_scores_df > 3

#This loop gives me a detailed understanding of each outlier, telling us what column it is in and the 
#value of the outlier so I can decide whether to remove it or not
for col in combined_data:
    outliers = outlier_mask[col]
    print(f'Column: {col}')
    print(f'Number of outliers: {outliers.sum()}')
    print(combined_data.loc[outliers, col]) 

#After all the outlier calculation, there were 25-30 outliers. Almost all of those outliers were worth 
#keeping, as they were conventional outliers, meaning they were slightly exaggerated stats that still
#resulted in the outcome they should've. E.g. a game with 65% from 3 leading to a win. This high a 3P%  
#would almost always result in a win, so it shouldn't be taken out. The only true outliers were
#removed as a result and this finished the process of cleaning the data. 

#Keeping rows with conventional outliers (slightly exaggerated stats that still resulted in the outcome 
#expected, such a game with 65% 3P% leading to a win). Removing outliers that would confuse the model
combined_data = combined_data.drop(38)
combined_data = combined_data.drop(125)
combined_data = combined_data.drop(172)
combined_data = combined_data.drop(199)
combined_data = combined_data.drop(209)

combined_data = combined_data.reset_index(drop=True)

cleaned_data = combined_data

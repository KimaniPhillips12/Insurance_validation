import pandas as pd
import numpy as np

#-- Questions to answer:
#- What are the first five rows of the dataset?
#- How many rows and columns are in the dataset?
#- clean the dataset by removing rows with missing values
#- Are there any missing values in the dataset?
#- standardized categories in region
#- Standardized sets to just two categories
#- change smoker column to boolenan
#- Standardize charges data type  (float)


#load insurance dataset
df = pd.read_csv('insurance.csv')
insurance_df = pd.DataFrame(df)
print(insurance_df.head())


insurance_filled = insurance_df
insurance_filled.dropna(inplace=True)

insurance_filled['region'] = insurance_filled['region'].str.lower()
FEMALE = 'female'
MALE = 'male'
sex_map = {'F': FEMALE, 'woman': FEMALE, 'man': MALE, 'M': MALE}

insurance_filled['sex'].unique()

insurance_filled['sex'] = insurance_filled['sex'].replace(sex_map)

insurance_filled['smoker'] = (insurance_filled['smoker'] == 'yes')

insurance_filled['charges'] = insurance_filled['charges'].str.strip('$').astype(float)

insurance_filled.sample(10)

print(insurance_filled.head())


# Task 2: scatterplots of relatiopnships between variables and charges

import matplotlib.pyplot as plt

df =insurance_df.copy()
x = df['smoker']
y = df['charges']

plt.scatter(x, y, color='blue', marker='o')

plt.xlabel('smoker')
plt.ylabel('charges')
plt.title('Scatter plot of Age vs Charges')

plt.show()

# Task 3: Try to fit the data for a linear regression model
# assume `df` exists above

# create one-hot columns for region
insurance_df = pd.get_dummies(df, prefix='region', columns=['region'])

# drop a specific dummy column if present
if 'region_southwest' in insurance_df.columns:
    insurance_df = insurance_df.drop(columns=['region_southwest'])

# ensure smoker is 0/1 (handles "yes"/"no" strings and numeric already)
if insurance_df['smoker'].dtype == object:
    insurance_df['smoker'] = insurance_df['smoker'].map({'yes': 1, 'no': 0})

insurance_df['smoker'] = insurance_df['smoker'].astype('bool')

print(insurance_df.head())
# ...existing code...
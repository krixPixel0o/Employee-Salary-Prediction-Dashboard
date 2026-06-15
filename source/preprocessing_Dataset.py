# Primary Module import

import pandas as pd


# Loading the Dataset

try :
    df = pd.read_csv('data/Employee_Details.csv')
    print("Dataset loaded successfully")
    print("Dataset shape - ", df.shape)
    print("Dataset columns - ", df.columns)
    print("Dataset info - ")
    print(df.info())
except FileNotFoundError :
    print("Dataset not found. Please generate the dataset first using 'generate_Dataset.py' script.")

# Since the dataset if generated with our specific ranges, we do not expect the dataset to have any missing / NA values.
# Let us confirm this once !

print("Dataset Null Values Check - ")
print(df.isnull().sum())

# Now let us check for duplicate instances !

print("Dataset Duplicate Values Check - ")
print(df.duplicated().sum())

# The duplicate count is 0. Thus, there is no need to drop any records !


# Categorical Encoding of the dataset [One Hot Encoding]

categorical_Features = ["Gender", "EducationLevel", "JobRole", "CompanyType"]

df_Encoded = pd.get_dummies(df, columns = categorical_Features, drop_first = True, dtype  = int)

# Now we store the preprocessed dataset in a new CSV file !

df_Encoded.to_csv("data/Employee_Details_Encoded.csv", index = False)

print("Dataset preprocessed and saved successfully as 'Employee_Details_Encoded.csv'")
print("Preprocessed Dataset shape - ", df_Encoded.shape)
print("Preprocessed Dataset columns - ", df_Encoded.columns)
print("Preprocessed Dataset Head - ")
print(df_Encoded.head())

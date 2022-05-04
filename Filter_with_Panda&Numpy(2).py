import pandas as pd
import numpy as np

# 1.	Read the data in the attached submission and set the row index to 0.

df = pd.read_csv(r"C:\Users\tungt\OneDrive\Desktop\Spring2022\SYST-230-001\Week13_Exercise8\data(1).csv", index_col=0)

# 2.	Determine how many null values are there in column “secure_internet_servers_total”.

a1 = df['secure_internet_servers_total'].isnull().sum()
print(f"#2 The number of null values in secure_internet_servers_total: {a1}\n")


# 3.	Determine the percentage of null values in the whole data set

percent_null = df.isnull().sum() * 100 / len(df)
print(f"#3 The percentage of null values in whole data set:\n{percent_null}\n")

# 4.	Determine how many unique values are there in each categorical column

print(f"#4 Unique values in each categorical column:\nUnique values: *--------------------*\n{df.nunique()}\n")


# 5.	Transform the column 'internet_users' from strings to percentages, and add the resulting new column to the
# data set, after deleting the old one. what are the unique values of 'internet_users'
# Clean it by transforming the stings into proportions

print("\n#5 Strings to proportions:\n")
for i in df.index:
    if df.loc[i,'internet_users']!='unknown':
        a=df.loc[i,'internet_users'].split()
        prop=float(a[0])/float(a[2])
        df.loc[i,'internet_users']=prop
    print(prop)

# 6.	In column "mobile_subscriptions" assign a value of 1 if mobile subscriptions is less than 1 per person, otherwise 2.

df['mobile_subscriptions'] = [1 if x == 'less than 1 per person' else 2 for x in df['mobile_subscriptions']]
print(f"\n#6 assign value:\n{df['mobile_subscriptions']}")

# 7.	In column "national_income" assign 1 for “very low”, 2 for “medium low”, 3 for “low”, 4 for “medium high”, 5 for “high”, 6 for “very high” and 0 for “unkown”.

D={'unknown':0, 'very low': 1, 'medium low': 2,'low': 3, 'medium high': 4, 'high': 5, 'very high': 6}
df['national_income'].replace(D, inplace=True)
print(f"\n#7 Replace strings with int:\n{df['national_income']}")

# 8.	Extract and print out all column names that have the word “cities” and then replace the NAN values of these columns by the mean of the corresponding column.

a = []
for i in df.columns:
    if i.find('cities') != -1:
        a.append(i)
b = df[a[0]].mean()
c = df[a[1]].mean()
d = df[a[0]].fillna(value=c)
e = df[a[1]].fillna(value=b)

print(f"\n#8 Replace NAN values of these columns by the mean of the corresponding column\n")
print(f"urban_pop_minor_cities")
print(e)
print(f"\nurban_pop_major_cities")
print(d)

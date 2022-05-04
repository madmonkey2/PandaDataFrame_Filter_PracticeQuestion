import pandas as pd
import numpy as np


# QUESTION 1
# **********************************************************************

# a. Read the data in the attached submission and set the “Order ID” column to be the row index
df = pd.read_csv(r"C:\Users\tungt\OneDrive\Desktop\Spring2022\SYST-230-001\Week12\Tung_Truong.py\orders.csv", index_col=1)

# b. Show all information of all orders on the date “8/26/2021”.

date_filter = df[df["Order Date"]=="8/26/2021"]
print(date_filter)

# c.  Determine the order id which had the lowest purchase of “Item Total”.

lowest1 = df.nsmallest(1,'Item Total')
print(lowest1)

# d.	Among those who purchased with an amount greater than $100, determine the order
# ids belonging to either of the following two groups: “Computer & Electronics”, “Kitchen”.

data = df[(df['Item Total']>100) & ((df['Group']=='Computer & Electronics') | (df['Group']=='Kitchen'))].index
print(data)

# e.	Determine the count of occurrences of “Amazon.com” in the “Seller” column.

count = df['Seller'].value_counts()['Amazon.com']
print(count)

# f. Show the “Description” of the SOFA sold on “8/29/2021”.

sofa_description = df[(df['Item Category']=='SOFA') & (df['Order Date']=='8/29/2021')].loc[:,'Description']
print(sofa_description)
# ************************************************** -> Alternative below without specific date
# sofa_description = (df['Item Category'] == 'SOFA')
# description = df.loc[sofa_description, 'Description']
# print(description)

# QUESTION 2
# **********************************************************************
# a.	Change the row index to be the “Order Date” and store the new data frame in a new variable.

df1 = pd.read_csv(r"C:\Users\tungt\OneDrive\Desktop\Spring2022\SYST-230-001\Week12\Tung_Truong.py\orders.csv", index_col=0)

# b.	Show all information of all orders on the date “9/1/2021”.

date_filter = df1.loc['9/1/2021']
print(date_filter)

# c.	Among those being sold on “8/26/2021”, determine the order id which had the highest purchase.

date_filter = df1.loc['8/26/2021']
print(date_filter)
data = df1.loc['8/26/2021', 'Order ID'].max()
print(data)

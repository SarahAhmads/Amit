import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import datetime as dt
from numpy import median

cafe = pd.read_csv(r'C:\Users\NOTEBOOK\Downloads\cafe.csv')

item_mode = cafe['Item'].mode()[0]
cafe['Item'] = cafe['Item'].fillna(item_mode)
cafe.loc[cafe['Item'] == 'UNKNOWN' , 'Item'] = item_mode
cafe.loc[cafe['Item'] == 'ERROR' , 'Item'] = item_mode

cafe['Quantity'] = cafe['Quantity'].replace(['UNKNOWN', 'ERROR', 'N/A'], np.nan)
cafe['Quantity'] = cafe['Quantity'].astype(float)
quantity_mean = cafe['Quantity'].mean().round()
cafe['Quantity'] = cafe['Quantity'].fillna(quantity_mean)
cafe['Quantity'] = cafe['Quantity'].astype(int)

cafe['Price Per Unit'] = cafe['Price Per Unit'].replace(['UNKNOWN', 'ERROR', 'N/A'], np.nan)
cafe['Price Per Unit'] = cafe['Price Per Unit'].astype(float)
Price_per_unit_mean = cafe['Price Per Unit'].mean().round()
cafe['Price Per Unit'] = cafe['Price Per Unit'].fillna(Price_per_unit_mean)
cafe['Price Per Unit'] = cafe['Price Per Unit'].astype(int)

cafe['Total Spent'] = cafe['Total Spent'].replace(['UNKNOWN', 'ERROR', 'N/A'], np.nan)
cafe['Total Spent'] = cafe['Total Spent'].astype(float)
Price_per_unit_mean = cafe['Total Spent'].mean().round()
cafe['Total Spent'] = cafe['Total Spent'].fillna(Price_per_unit_mean)
cafe['Total Spent'] = cafe['Total Spent'].astype(int)

payment_mode = cafe['Payment Method'].mode()[0]
cafe.loc[cafe['Payment Method'] == 'UNKNOWN', 'Payment Method'] = payment_mode
cafe.loc[cafe['Payment Method'] == 'ERROR', 'Payment Method'] = payment_mode
cafe['Payment Method'] = cafe['Payment Method'].fillna(payment_mode)

cafe = cafe.drop('Location', axis = 1)

cafe['Transaction Date'] = pd.to_datetime(cafe['Transaction Date'], errors='coerce')
date_mode = cafe['Transaction Date'].mode()[0]
cafe['Transaction Date'] = cafe['Transaction Date'].fillna(date_mode)
today_date = dt.datetime.today()
cafe.loc[cafe['Transaction Date'] > today_date, 'Transaction Date'] = today_date

for col in cafe.select_dtypes(include='object'):
    cafe[col] = cafe[col].str.strip()

cafe = cafe.drop_duplicates()

cafe['Transaction Year'] = cafe['Transaction Date'].dt.year
cafe['Transaction Month'] = cafe['Transaction Date'].dt.month
cafe = cafe.drop('Transaction Date', axis = 1)

cafe = cafe.rename(columns={'Item' : 'Item Name'})

cafe['Check Total Spent'] = cafe['Quantity'].multiply(cafe['Price Per Unit'])
#total spent column is not equal check total spent
cafe['Total Spent'] = cafe['Check Total Spent']
cafe = cafe.drop('Check Total Spent', axis = 1)

cafe.to_csv(r'C:\Users\NOTEBOOK\Downloads\Cafe_Data_Cleaning.csv', index=False)
print(cafe.head().T)


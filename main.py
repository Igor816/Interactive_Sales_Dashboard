import pandas as pd 
from sqlalchemy import create_engine


df = pd.read_excel('Sales_Dataset_2024.xlsx')

print(df.head())
# print(df.tail())


# Преобразуй даты
df['Date']= pd.to_datetime(df['Date'])

# Убедись, что числовые поля корректны
df['Sales'] = pd.to_numeric('Sales', errors='coerce')
df['Profit'] = pd.to_numeric('Profit', errors='coerce')



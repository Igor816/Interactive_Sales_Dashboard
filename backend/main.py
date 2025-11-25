import pandas as pd 


df = pd.read_excel('Sales_Dataset_2024.xlsx')

print(df)



# Преобразуй даты
df['Date']= pd.to_datetime(df['Date'])

# Убедись, что числовые поля корректны
df['Profit'] = pd.to_numeric(df['Profit'], errors='coerce')
df['Unit_Price'] = pd.to_numeric(df['Unit_Price'], errors='coerce')



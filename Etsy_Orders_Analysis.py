import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 150)

df = pd.read_csv('Pandas-practice/Etsy_Sold_Orders_2023_July-Oct - Etsy_Sold_Orders_2023_July-Oct.csv')
df.columns = ['Sales Date', 'Order ID', 'Customer ID', 'Number of Items', 'Shipping Date', 'City', 'State', 
              'Country', 'Subtotal', 'Discount Amount', 'Shipping cost', 'Order Total', 'Card Processing Fee', 
              'Zipcode', 'Net Profit', 'Coupon Code']
print(df.head())
print(df.info())

# Repeat customers
customers = df.groupby('Customer ID')['Order ID'].count().sort_values(ascending=False)
print(customers)


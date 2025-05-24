import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("book2.csv")
print("First 10 rows:")
print(df.head(10))

df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
df['Month'] = df['Date'].dt.month
df['day'] = df['Date'].dt.day_name()
df['total'] = df['Qty sold'] * df['Unt price']
df = df.fillna(0)

monthly_dealing = df.groupby('Month')['total'].sum()
plt.bar(monthly_dealing.index, monthly_dealing.values, color='red')
plt.title("Monthly Dealing")
plt.xlabel("Month")
plt.ylabel("Total Income")
plt.show()

top_products = df.groupby('Product name')['total'].sum().sort_values(ascending=False).head(10)
plt.bar(top_products.index, top_products.values, color='green')
plt.title("Top 10 Products by Dealing")
plt.xlabel("Product")
plt.ylabel("Dealing")
plt.xticks(rotation=45)
plt.show()

payment_type_totals = df['Payment system'].value_counts()
plt.pie(payment_type_totals, labels=payment_type_totals.index, autopct='%1.1f%%')
plt.title("Payment Type Totals")
plt.show()

location_dealing = df.groupby('Stock location')['total'].sum()
plt.bar(location_dealing.index, location_dealing.values, color='blue')
plt.title("Dealing by Store Location")
plt.xlabel("Location")
plt.ylabel("Dealing")
plt.xticks(rotation=45)
plt.show()

weekdays_sales = df.groupby('day')['total'].sum()
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weekdays_sales = weekdays_sales.reindex(days).fillna(0)
plt.bar(weekdays_sales.index, weekdays_sales.values, color='yellow')
plt.title("Dealing by Weekdays")
plt.xlabel("Days")
plt.ylabel("Dealing")
plt.show()
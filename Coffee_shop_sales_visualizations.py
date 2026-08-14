import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
coffee = np.array(["Espresso","Latte","Cappuccino","Mocha","Cold Coffee"])
cups_sold = np.array([120,95,150,80,110])
price = np.array([120,180,160,200,150])
df = pd.DataFrame({
    "Coffee": coffee,
    "Cups Sold": cups_sold,
    "Price": price
})

df["Revenue"] = df["Cups Sold"] * df["Price"]
print(df)
plt.figure(figsize=(6,4))
plt.bar(df["Coffee"], df["Cups Sold"])
plt.title("Cups Sold by Coffee")
plt.xlabel("Coffee")
plt.ylabel("Cups Sold")
plt.show()
plt.figure(figsize=(6,6))
plt.pie(df["Cups Sold"], labels=df["Coffee"], autopct="%1.1f%%")
plt.title("Coffee Sales Distribution")
plt.show()
plt.figure(figsize=(6,4))
plt.plot(df["Coffee"], df["Price"], marker="o")
plt.title("Coffee Price")
plt.xlabel("Coffee")
plt.ylabel("Price")
plt.show()
plt.figure(figsize=(6,4))
plt.hist(df["Price"], bins=5)
plt.title("Distribution of Coffee Prices")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.show()
plt.figure(figsize=(6,4))
plt.scatter(df["Cups Sold"], df["Price"])
plt.title("Cups Sold vs Price")
plt.xlabel("Cups Sold")
plt.ylabel("Price")
plt.show()
plt.figure(figsize=(6,4))
sns.barplot(data=df, x="Coffee", y="Revenue")
plt.title("Revenue by Coffee")
plt.show()
plt.figure(figsize=(5,4))
sns.boxplot(y=df["Price"])
plt.title("Coffee Price Distribution")
plt.show()
plt.figure(figsize=(5,4))
sns.heatmap(df[["Cups Sold","Price","Revenue"]].corr(), annot=True, cmap="Blues")
plt.title("Correlation Heatmap")
plt.show()
print("Most Sold Coffee:")
print(df.loc[df['Cups Sold'].idxmax()])

print("\nMost Expensive Coffee:")
print(df.loc[df['Price'].idxmax()])

print("\nAverage Coffee Price:", df["Price"].mean())

print("Total Revenue:", df["Revenue"].sum())
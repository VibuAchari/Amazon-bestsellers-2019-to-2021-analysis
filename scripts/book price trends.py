df['price'] = df['price'].replace('[\$,]', '', regex=True).astype(float)

# Group by 'year' and 'genre', and calculate the average price
avg_price_by_genre = df.groupby(['year', 'genre'])['price'].mean().unstack()

# Plotting the trend
plt.figure(figsize=(14, 8))
sns.lineplot(data=avg_price_by_genre, palette='tab10', markers=True)

# Adding labels and title
plt.xlabel('Year')
plt.ylabel('Average Price ($)')
plt.title('Trend of Average Book Prices Over Time by Genre')
plt.legend(title='Genre')
plt.grid(True)
plt.show()
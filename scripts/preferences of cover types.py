# Data Cleaning: Convert 'price' to numeric (remove any non-numeric characters if necessary)
df['price'] = df['price'].replace('[\$,]', '', regex=True).astype(float)

# 1. Distribution of Book Types
book_type_counts = df['cover_type'].value_counts()
print("Distribution of Book Types:")
print(book_type_counts)

# Plot the distribution of book types
plt.figure(figsize=(10, 6))
sns.barplot(x=book_type_counts.index, y=book_type_counts.values, palette='inferno')
plt.xlabel('Cover Type')
plt.ylabel('Number of Books')
plt.title('Distribution of Paperback, Hardcover, and Mass Paperback Books')
plt.show()

# 2. Price Comparison
avg_price_by_type = df.groupby('cover_type')['price'].mean()
print("\nAverage Price by Book Type:")
print(avg_price_by_type)

# Plot average prices by book type
plt.figure(figsize=(10, 6))
sns.barplot(x=avg_price_by_type.index, y=avg_price_by_type.values, palette='inferno')
plt.xlabel('Cover Type')
plt.ylabel('Average Price ($)')
plt.title('Average Price of Paperback, Hardcover, and Mass Paperback Books')
plt.show()

# 3. Genre Distribution
genre_distribution = df.groupby('cover_type')['genre'].value_counts().unstack().fillna(0)
print("\nGenre Distribution by Book Type:")
print(genre_distribution)

# Plot genre distribution by book type
genre_distribution.plot(kind='bar', stacked=True, figsize=(14, 8), colormap='inferno')
plt.xlabel('Cover Type')
plt.ylabel('Number of Books')
plt.title('Genre Distribution by Paperback, Hardcover, and Mass Paperback')
plt.legend(title='Genre')
plt.show()

# 4. Trend Over Time
# Convert 'year' to integer if not already
df['year'] = df['year'].astype(int)
yearly_distribution = df.groupby(['year', 'cover_type']).size().unstack().fillna(0)

# Plot trend over time
plt.figure(figsize=(14, 8))
yearly_distribution.plot(kind='line', marker='o', colormap='inferno')
plt.xlabel('Year')
plt.ylabel('Number of Books')
plt.title('Trend of Paperback, Hardcover, and Mass Paperback Books Over Time')
plt.legend(title='Cover Type')
plt.grid(True)
plt.show()

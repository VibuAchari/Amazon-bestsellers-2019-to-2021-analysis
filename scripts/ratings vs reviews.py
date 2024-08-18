# Convert 'ratings' to numeric (remove any non-numeric characters and handle errors)
df['ratings'] = df['ratings'].replace('[\$,]', '', regex=True).astype(float)
# Convert 'no_of_reviews' to numeric (remove commas and convert to float)
df['no_of_reviews'] = df['no_of_reviews'].replace('[\$,]', '', regex=True).astype(float)

# Drop rows with missing values in 'ratings' or 'no_of_reviews'
df = df.dropna(subset=['ratings', 'no_of_reviews'])

# Calculate the correlation
correlation = df['ratings'].corr(df['no_of_reviews'])

# Print correlation
print(f'Correlation between Ratings and Number of Reviews: {correlation:.2f}')

# Plotting
plt.figure(figsize=(10, 6))
sns.scatterplot(x='no_of_reviews', y='ratings', data=df, alpha=0.6)
plt.xlabel('Number of Reviews')
plt.ylabel('Ratings')
plt.title('Scatter Plot of Ratings vs. Number of Reviews')
plt.grid(True)
plt.show()
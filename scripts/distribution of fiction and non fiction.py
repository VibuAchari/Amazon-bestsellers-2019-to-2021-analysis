y1 = np.arange(2009, 2015)
y2 = np.arange(2015, 2022)
years = np.concatenate((y1, y2))

fiction_counts = []
non_fiction_counts = []


for year in years:
    counts = df[df['year'] == year]['genre'].value_counts()
    fiction_counts.append(counts.get('Fiction', 0))
    non_fiction_counts.append(counts.get('Non Fiction', 0))
    
# Plotting the data
fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(years, fiction_counts, marker='o', linestyle='-', color='#800020', label='Fiction')
ax.plot(years, non_fiction_counts, marker='o', linestyle='-', color='#191970', label='Non Fiction')


# Adding labels and titles
ax.set_title('Distribution of Fiction and Non-Fiction books from 2009 to 2021', fontsize=20)
ax.set_xlabel('Year', fontsize=15)
ax.set_ylabel('Number of Books', fontsize=15)
ax.legend()

# Show the plot
plt.show()

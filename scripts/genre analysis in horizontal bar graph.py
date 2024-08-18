no_dup = df.drop_duplicates('title')
g_count = no_dup['genre'].value_counts()

# Dark color palette for the bar chart
genre_col = ['#800020','#191970','#2F4F4F']

# Plotting the horizontal bar chart
fig, ax = plt.subplots(figsize=(10, 7))
ax.barh(g_count.index, g_count.values, color=genre_col, edgecolor='black')

# Adding title and labels
ax.set_title('Distribution of Genre for All Unique Books from 2009 to 2021', fontsize=20)
ax.set_xlabel('Number of Books', fontsize=15)
ax.set_ylabel('Genre', fontsize=15)

# Customizing the y-axis labels
ax.set_yticklabels(g_count.index, fontsize=12)

# Display the chart
plt.tight_layout()
plt.show()

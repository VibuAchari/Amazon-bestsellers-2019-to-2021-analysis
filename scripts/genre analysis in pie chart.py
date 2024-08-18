no_dup = df.drop_duplicates('title')
g_count = no_dup['genre'].value_counts()

fig, ax = plt.subplots(figsize=(7,7))

def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{p:.2f}%\n({v:d})'.format(p=pct,v=val)
    return my_autopct


genre_col = ['#800020','#191970','#228B22']

center_circle = plt.Circle((0, 0), 0.6, color='white')
plt.pie(x=g_count.values, labels=g_count.index, autopct=make_autopct(g_count.values),
          startangle=90, textprops={'size': 15}, pctdistance=0.5, colors=genre_col,wedgeprops={'edgecolor': 'black'}) 
ax.add_artist(center_circle)

fig.suptitle('Distribution of Genre for all unique books from 2009 to 2021', fontsize=20)
fig.show()
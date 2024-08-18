best_nf_authors = df.groupby(['author', 'genre']).agg({'title': 'count'}).unstack()['title', 'Non Fiction'].sort_values(ascending=False)[:11]
best_f_authors = df.groupby(['author', 'genre']).agg({'title': 'count'}).unstack()['title', 'Fiction'].sort_values(ascending=False)[:11]

with plt.style.context('Solarize_Light2'):
    fig, ax = plt.subplots(1, 2, figsize=(8,8))
    if len(genre_col) < 2:
        genre_col=['#800020','#191970'] 
    ax[0].barh(y=best_nf_authors.index, width=best_nf_authors.values,
           color=genre_col[0])
    ax[0].invert_xaxis()
    ax[0].yaxis.tick_left()
    ax[0].set_xticks(np.arange(max(best_f_authors.values)+1))
    ax[0].set_yticklabels(best_nf_authors.index, fontsize=12, fontweight='semibold')
    ax[0].set_xlabel('Number of appreances')
    ax[0].set_title('Non Fiction Authors')

    
    if len(genre_col) < 2:
        genre_col=(['#800020','#191970'])  
    ax[1].barh(y=best_f_authors.index, width=best_f_authors.values,
           color=genre_col[1])
    ax[1].yaxis.tick_right()
    ax[1].set_xticks(np.arange(max(best_f_authors.values)+1))
    ax[1].set_yticklabels(best_f_authors.index, fontsize=12, fontweight='semibold')
    ax[1].set_title('Fiction Authors')
    ax[1].set_xlabel('Number of appreances')
    plt.suptitle('Top 10 best selling Authorsfrom 2009 to 2021', fontsize=15)
    fig.legend(['Non Fiction', 'Fiction'], fontsize=12)

plt.show()
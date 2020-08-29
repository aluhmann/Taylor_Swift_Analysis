# Import packages
import glob, os
import string
from nltk.corpus import stopwords 
import pandas as pd
import matplotlib.pyplot as plt
import math
from itertools import chain
import seaborn as sns

##############################
########## folklore ########## 
##############################

# Change directory for folklore album 
os.chdir('Taylor_Swift')

# Iterate through each song in folklore and extract the title and text
folklore = []
for file in sorted(glob.glob('folklore/*.txt')):
    # Remove punctuation and make all letters lowercase - this will ensure words are not double counted later
    text = open(file).read().translate(str.maketrans(',?.:;()', '       '))
    # Title is the first line
    title = text.partition('\n')[0]
    # Remove title and split the remaining text into separate words
    text = text.replace(title, '').lower().split()
    # Remove stop words since they do not provide meaning
    stop_words = stopwords.words('english')
    text = [x for x in text if not x in stop_words]
    # Add title and lyrics into dictinoary 
    folklore.append({
        'Title': title,
        'Lyrics': text,
        'Total Length': len(text),
        'Unique Words': len(set(text))
    })

# Number of Unique words for each song

# Look at all lyrics from the entire album
folklore_all_lyrics = [x['Lyrics'] for x in folklore]
folklore_all_lyrics = list(chain.from_iterable(i if isinstance(i, list) else [i] for i in folklore_all_lyrics))

print('The total number of words in Folklore is', len(folklore_all_lyrics))
print('The number of unique words in Folklore is', len(set(folklore_all_lyrics)))

# Look at each song in the album
folklore_df=pd.DataFrame([dict((k,x[k]) for k in ['Title','Total Length','Unique Words'] if k in x) for x in folklore])
folklore_df['Percent Unique'] = folklore_df['Unique Words']/folklore_df['Total Length']*100
folklore_df

# Find the average percent of unique words
folklore_df['Percent Unique'].mean()

# Most used words

# Create function to show top words
def top_words(text, top = None):
    count = dict()
    for word in text:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    if(top is not None):
        sorted_count = sorted(count, key=count.get, reverse=True)[:top]
        top_words = {key: count[key] for key in sorted_count}
        return top_words
    else:
        return count

# Top words for album
folklore_top = pd.DataFrame(top_words(folklore_all_lyrics,top=25).items(),columns=['Word','Count'])
# Reset index
folklore_top.index = folklore_top.index + 1
folklore_top

# Find top words for each song
folklore_top_counts = [{'Title': x['Title'], 'Counts': top_words(x['Lyrics'], top=8)} for x in folklore]
for song in folklore_top_counts:
    print(song['Title'])
    for word in song['Counts']:
        print(word,':', song['Counts'][word])
    print('\n')

# Create pie charts to show how often each word is used relative to other words
folklore_counts = [{'Title': x['Title'], 'Counts': top_words(x['Lyrics'])} for x in folklore]
fig, axs = plt.subplots(4,4,figsize=(9,9),subplot_kw={'aspect':'equal'})
axs = axs.flatten()
for ax, song in zip(axs,folklore_counts):
    sizes = []
    for x, y in song['Counts'].items():
        sizes.append(y)
    ax.pie(sizes)
    if(int(len(song['Title']) < 25)):
        ax.set_title(song['Title'])
    else:
        split = math.floor(int(len(song['Title']))/2)
        title_line1 = song['Title'][:split]
        title_line2 = song['Title'][split:]
        ax.set_title(title_line1+'\n'+title_line2)
fig.suptitle("Word Usage in Taylor Swift's Album 'folklore'",fontsize=16)
plt.show()



##############################
######## Taylor Swift ########
##############################

# Repeat above analysis for Taylor Swift album

# Iterate through each song in folklore and extract the title and text
Taylor_Swift = []
for file in sorted(glob.glob('Taylor_Swift/*.txt')):
    # Remove punctuation and make all letters lowercase - this will ensure words are not double counted later
    text = open(file).read().translate(str.maketrans(',?.:;()', '       '))
    # Title is the first line
    title = text.partition('\n')[0]
    # Remove title and split the remaining text into separate words
    text = text.replace(title, '').lower().split()
    # Remove stop words since they do not provide meaning
    stop_words = stopwords.words('english')
    text = [x for x in text if not x in stop_words]
    # Add title and lyrics into dictinoary 
    Taylor_Swift.append({
        'Title': title,
        'Lyrics': text,
        'Total Length': len(text),
        'Unique Words': len(set(text))
    })

# Look at all lyrics from the entire album
Taylor_Swift_all_lyrics = [x['Lyrics'] for x in Taylor_Swift]
Taylor_Swift_all_lyrics = list(chain.from_iterable(i if isinstance(i, list) else [i] for i in Taylor_Swift_all_lyrics))

print("The total number of words in 'Taylor Swift' is", len(Taylor_Swift_all_lyrics))
print("The number of unique words in 'Taylor Swift' is", len(set(Taylor_Swift_all_lyrics)))

TS_df = pd.DataFrame([dict((k,x[k]) for k in ['Title','Total Length','Unique Words'] if k in x) for x in Taylor_Swift])
TS_df['Percent Unique'] = TS_df['Unique Words']/TS_df['Total Length']*100
TS_df

TS_df['Percent Unique'].mean()

# Top words for album
TS_top = pd.DataFrame(top_words(Taylor_Swift_all_lyrics, top = 25).items(), columns = ['Word', 'Count'])
TS_top.index = TS_top.index + 1
TS_top

Taylor_Swift_top_counts = [{'Title': x['Title'], 'Counts': top_words(x['Lyrics'], top=8)} for x in Taylor_Swift]
for song in Taylor_Swift_top_counts:
    print(song['Title'])
    for word in song['Counts']:
        print(word,':', song['Counts'][word])
    print('\n')

Taylor_Swift_counts = [{'Title': x['Title'], 'Counts': top_words(x['Lyrics'])} for x in Taylor_Swift]

fig, axs = plt.subplots(4,4,figsize=(9,9),subplot_kw={'aspect':'equal'})
axs[3,3].axis('off')
axs[3,2].axis('off')
axs = axs.flatten()
for ax, song in zip(axs,Taylor_Swift_counts):
    sizes = []
    for x, y in song['Counts'].items():
        sizes.append(y)
    ax.pie(sizes)
    if(int(len(song['Title']) < 20)):
        ax.set_title(song['Title'])
    else:
        split = math.floor(int(len(song['Title']))/2)
        title_line1 = song['Title'][:split]
        title_line2 = song['Title'][split:]
        ax.set_title(title_line1+'\n'+title_line2)
fig.suptitle("Word Usage in Taylor Swift's Album 'Taylor Swift'",fontsize=16)
plt.show()




##############################
######### Comparison ######### 
##############################

# Create plot to comapre the two albums

# Set up figure
f, ax = plt.subplots(1,2, figsize=(20,10))
# Want y-axis limits same for easy comparison
plt.setp(ax, ylim=[0,240])


# folklore
sns.set_color_codes('pastel')
# Graph total words
sns.barplot(x = 'Title', y = 'Total Length', data = folklore_df.sort_values('Total Length', ascending=False),
            label = 'Total', color = 'b', edgecolor = 'w', ax=ax[0])
sns.set_color_codes('muted')
# Graph unique words ontop
sns.barplot(x = 'Title', y = 'Unique Words', data = folklore_df.sort_values('Total Length',ascending=False),
            label = 'Unique Words', color = 'b', edgecolor = 'w', ax=ax[0])
ax[0].axhline(folklore_df['Total Length'].mean(), ls='--', c='red')
ax[0].text(10,145, "Average Total", fontsize=16, fontweight='bold')
ax[0].axhline(folklore_df['Unique Words'].mean(), ls='--', c='red')
ax[0].text(10,88, "Average Unique Words", fontsize=16, fontweight='bold')
ax[0].legend(ncol = 2, loc = 'upper right')
ax[0].set_xticklabels(ax[0].get_xticklabels(), rotation=90)
ax[0].set_ylabel('Number of Words')
ax[0].set_title("'folklore' (2020)", fontsize=20)


# Taylor Swift
sns.set_color_codes('pastel')
sns.barplot(x = 'Title', y = 'Total Length', data = TS_df.sort_values('Total Length',ascending=False),
            label = 'Total', color = 'b', edgecolor = 'w', ax=ax[1])
sns.set_color_codes('muted')
sns.barplot(x = 'Title', y = 'Unique Words', data = TS_df.sort_values('Total Length',ascending=False),
            label = 'Unique Words', color = 'b', edgecolor = 'w', ax=ax[1])
ax[1].axhline(TS_df['Total Length'].mean(), ls='--', c='red')
ax[1].text(9,140, "Average Total", fontsize=16, fontweight='bold')
ax[1].axhline(TS_df['Unique Words'].mean(), ls='--', c='red')
ax[1].text(8,72, "Average Unique Words", fontsize=16, fontweight='bold')
ax[1].legend(ncol = 2, loc = 'upper right')
ax[1].set_xticklabels(ax[1].get_xticklabels(), rotation=90)
ax[1].set_ylabel('Number of Words')
ax[1].set_title("'Taylor Swift' (2006)", fontsize=20)
f.suptitle("Word Usage in Taylor Swift Albums", fontsize=30, fontweight='bold')
plt.show()
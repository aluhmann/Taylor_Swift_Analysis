# Has Taylor Swift's Vocabulary Increased in Her New Album?

Taylor Swift, since her debut in 2006, has gone through many changes in her musical career. At the end of July 2020, Taylor Swift released her most recent album, 'folklore'. 'folklore' is not only a shift from Taylor Swift's regular style, but also is being considered by many critics as her best album, especially from a lyrical standpoint. I wanted to look further into the lyrics of 'folklore' and compare this album to her debut album 'Taylor Swift' to see if there are notable differences  from a lyrical standpoint. 


### How many unique words?

The first aspect of the albums I decided to look at was the total number of words used as well as the number of unique words used. Before looking into this, I removed 'stop words'. These are words that are not considered useful to word analysis such as a, the, and for. This was completed using the nltk.corpus library in Python. 

![Alt text](/Images/Word_Usage_Comparison.png)
  
  
In 'folklore', about 61% of the total words in the album were unique words compared to 'Taylor Swift' where only about 49% of the total words in the album were unique words. This is clear in the above visualization where you can see the average total number of words between the two albums does not differ by much, however, the number of unique words is noticeably higher in 'folklore'. 


### Popular Words in Each Song

I was also interested in the looking if certain words were used more frequently than other words. 

For 'folklore', the 25 most used words were as follows:

![alt-text-1](/Images/folklore_top_1_12.png) ![alt-text-2](/Images/folklore_top_13_25.png)
  
  
For 'Taylor Swift', the top 25 most used words are as follows:

![alt-text-1](/Images/TS_top_1_12.png) ![alt-text-2](/Images/TS_top_13_25.png)

  
Interestingly, the word 'oh' is the second most used word in Taylor Swift's debut album, 'Taylor Swift'. In her most recent album, 'oh' does not even make it as one of the top 25 most used words, showing the increase in maturity within her lyrics between the two albums. 


Now to look more in depth at each song within the two albums. 

![alt-text-1](/Images/Pie_Chart_folklore.png) ![alt-text-2](/Images/Pie_Chart_TS.png)
  
  
Each slice of the pie represents how often a word is used in the song. Thus, large slices of the pie indicate that word is used more often compared to other words in the song. The album 'folklore' has been acclaimed as a more storytelling album. This is evident by the overall smaller pie slices, indicating no single word is being used more than other words. In contrast there are several songs in the album 'Taylor Swift' with large pie slices. In fact, in the song 'A Place in This World' from 'Taylor Swift', the second most used word is 'oh', being used a total of 13 times! 


### Conclusions

While there are many factors involved in the analysis of lyrics, these factors do indicate the increase in vocabulary in Taylor Swift's lyrics between her two albums. The increase in unique words and more storytelling nature of her latest album 'folklore' shows the maturity and growth in Taylor Swift's career as an artist. 

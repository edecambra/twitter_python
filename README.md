Data Science Assignment 1: Python and Twitter API Data
===================================================
This repository contains all the python scripts, and harvested twitter API data for the first assignment in the coursera data science program.  The tweets can be harvested by any user with the script twitterstream.py, however you must set up a twitter API developers account, and produce access keys and tokens.  Open the sctipt and use the following code to generate your dataset:  python twitterstream.py > output.txt 

These scripts that use this output.txt code are as follows:

 - tweet_sentiment.py -> This script combines the AFINN-111.txt dictionary file which contains words and their "sentiment" score, with the parsed tweet data to assign an overall score to each tweet
 - term_sentiment.py -> This script takes the scored tweets from tweet_sentiment.py and uses these scores to assign a sentiment to words outside of the AFINN-111.txt dictionary that are in the tweet, essentially expanding the body of scored words
 - frequency.py -> This script breaks each tweet into its terms and counts a general frequency across the terms for the entire dataset
 - top_ten.py -> This script looks at the JSON object in each tweet assigned to hashtags, and performs a count across all tweets, and sorts into the top ten most used tags
 - happiest_state.py -> This script looks at a source of location data embedded in each tweet object, and couples this with the sentiment analysis described in tweet_sentiment.py and term_sentiment.py to calculate the "happiest" U.S. state.  
# This script is the second problem in coursera assignment 1
# it looks at many tweets from live twitter stream collected by
# twitterstream.py, using the API oauth framework
# Then the script uses a sentiment scoring dictionary to parse the words in 
# each tweek and assign a sentiment score that is the simple sum of matched
# words


import sys, json, re


def hw():
    print 'Hello, world!'

# Puts the existing sentiment scores into a dictionary, with scores   
def sentiDict(fp):
	for line in fp:
		term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
		scores[term] = int(score)  # Convert the score to an integer.

#This loop set reads each tweet, checks for English, uses unicode, 
#matches to the score dictionary and appends this score to an array
#and prints the sum of the score for each tweet
def sentiScore(fp):
    for line in fp:
        text = (json.loads(line)).get("text") 
        if((json.loads(line)).get("lang") == "en"): #only uses English coded tweets, to use all tweets comment this and unindent
            if(text != None): #only uses tweets, not deletes
                text = text.encode("utf-8")
                text = text.lower()
                words = text.split()
                tweetScore = []
                for word in words:
                    word = re.sub("[\W]", "", word) #regex to scrub all non-alphanumeric chars
                    word = re.sub("[_]", "", word) #regex to scrub all underscore
                    if (scores.get(word) != None):
                        tweetScore.append(scores.get(word))
                print sum(tweetScore)

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    sentiDict(sent_file)
    sentiScore(tweet_file)

#global values initilization 
scores = {}
tweets = {}

#Calculation execution   
main()
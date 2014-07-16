#This program contains similar structure to tweet_sentiment.py however
#it is modified to extend the sentiment score to alternative words outside
#of the AFINN-111.txt file

import sys, json, re

# Puts the existing sentiment scores into a dictionary, with scores   
def sentiDict(fp):
        for line in fp:
            if " " not in line:
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
                for word in words:
                    word = re.sub("[\W]", "", word) #regex to scrub all non-alphanumeric chars
                    word = re.sub("[_]", "", word) #regex to scrub all underscore
                    if (scores.get(word) == None):
                            totals[word] = totals.get(word, 0) + sum(tweetScore)
                            counts[word] = counts.get(word, 0) + 1    
    #print len(totals), len(counts)

def termScore():
    for key in totals:
        tot = totals.get(key)
        cnt = counts.get(key)
        newTerms[key] = tot/cnt

def printTerms():
    for key in newTerms:
        print "{0} {1}".format(key, newTerms[key])
    
def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    sentiDict(sent_file)
    sentiScore(tweet_file)
    termScore()
    printTerms()
    
#global values initilization 
scores = {}
tweets = {}
totals = {}
counts = {}
neg = {}
pos = {}
newTerms = {}

#Calculation execution   
main()
#hw()

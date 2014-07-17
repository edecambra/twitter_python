# This is a counter for unique hashtags in any harvested
# twitter API stream file.  It looks through each tweet,
# finds the hashtags, and counts them

import sys, json, re
from operator import itemgetter

def hw():
    print 'Hello, world!'

#This loop parses each tweets hashtags and creates a count
#dictionary of tags and tweets
def hashtagParse(fp):
    for line in fp:
        ent = json.loads(line).get("entities")
        if ent is not None:
            hash = ent.get("hashtags")            
            if hash: 
                for tag in hash:
                    text = tag.get("text")
                    text = text.encode("utf-8")
                    hashtagsDict[text] = hashtagsDict.get(text,0) + 1

#This loop transforms the dictionary into a list of tuples
#allowing list sorting on the second item in each  tuple
#which is the count of each tag  
def hashtagSort():
    for tag, count in hashtagsDict.items():
        hashtagsList.append( (tag, count) )
    hashtagsList.sort(key=itemgetter(1), reverse = True)
    for tag, count in hashtagsList[0:10]:
        print tag, count

        
def main():
    #hw()
    tweet_file = open(sys.argv[1])
    hashtagParse(tweet_file)
    hashtagSort()
  

#global values initilization 
hashtagsDict = {}
hashtagsList = []
#Calculation execution   
main()
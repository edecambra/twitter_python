# This script will use the same twiter data harvested from output.txt using
# twitterstream.py, and merge this with the imbedded json data about
# the state location.  It will then use the sentiment data to see which
# state is the "happiest"


import sys, json, re
from operator import itemgetter

states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}


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
        if((json.loads(line)).get("lang") == "en"): #only uses English coded tweets, to use all tweets comment this and unindent
            #this portion calculates the sentiment of a tweet
            text = json.loads(line).get("text")
            score = 0
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
                score = sum(tweetScore)        
            #this portion determines what state the tweet is in
            user = json.loads(line).get("place")
            if user is not None:
                local = user.get("full_name")
                local = local.encode("utf-8")
                items = local.split(",")
                for item in items:
                    item = item.lstrip(" ")
                    if item in states.keys() or item in states.values():                        
                        stateScores[item] = stateScores.get(item, 0) + score
                        
def scoreCompress():
    for key in stateScores:
        if key in states.keys():
            finalList[key] = stateScores[key]
        if key in states.values():
            for k, v in states.items():
                if key == v:
                    finalList[k] = stateScores[key]
#This is used to take the final, compressed list and sort it to find the
#happiest state and print to the stdout
def sortList():
    for k, v in finalList.items():
        list.append( (k,v) )
    list.sort(key=itemgetter(1), reverse = True)
    print list[0][0]
  
def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    sentiDict(sent_file)
    sentiScore(tweet_file)
    scoreCompress()
    sortList()

#global values initilization 
scores = {}
stateScores = {}
finalList = {}
list = []
#Calculation execution   
main()
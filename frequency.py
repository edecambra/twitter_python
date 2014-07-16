import sys, json, re


def hw():
    print 'Hello, world!'

#global values initilization 
counts = 0
terms = {}
freqs = {}   
tweet_file = open(sys.argv[1])
#totalCounts loops
for line in tweet_file:
    text = (json.loads(line)).get("text")
    if (json.loads(line)).get("lang") == "en":
        if text is not None:
            text = text.encode("utf-8")            
            words = text.split()                        
            for word in words:
                word = word.lower()
                word = re.sub("[\W]", "", word) #regex to scrub all non-alphanumeric chars
                word = re.sub("[_]", "", word) #regex to scrub all underscore
                counts = counts + len(words)
                #print word
                terms[word] = terms.get(word, 0) + 1 
            #print word
#calculation()
for key in terms:
    freqs[key] = float(terms.get(key)/counts)
for key in freqs:    
    print "{0} {1}".format(key, freqs[key])        
#print counts
#print terms
#for key in freqs:
                



#import regex
import re

#start process_tweet
def processTweet(tweet):
    # process the tweets

    #Convert to lower case
    tweet = tweet.lower()
    #Convert www.* or https?://* to URL
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','URL',tweet)
    #Convert @username to AT_USER
    tweet = re.sub('@[^\s]+','AT_USER',tweet)
    #Remove additional white spaces
    tweet = re.sub('[\s]+', ' ', tweet)
    #Replace #word with word
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
    #trim
    tweet = tweet.strip('\'"')
    return tweet
#end

#start replaceTwoOrMore
    def replaceTwoOrMore(self, s):
        # pattern to look for three or more repetitions of any character, including
        # newlines.
        pattern = re.compile(r"(.)\1{1,}", re.DOTALL) 
        return pattern.sub(r"\1\1", s)
    #end

#Read the tweets one by one and process it
fp = open('data/weektweets/iphone.txt', 'r')
line = fp.readline()

while line:
    processedTweet = processTweet(line)
    
    
    print processedTweet
    line = fp.readline()

    
#end loop

fp.close()

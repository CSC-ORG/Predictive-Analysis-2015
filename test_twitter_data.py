#!/usr/bin/env python
import get_twitter_data
{
    "consumer_key": "dK1ULqvGUZzS2rM3Kn49h9wtJ",
    "consumer_secret": "dYfQNeuVKg9f7m9spKiS9WBAo5zbwYx1WZAXbyinpM5o8Ptb8n",
    "access_token": "1329206947-77ax3lhzTuiiH9FUToMASiktI5deUpKBJj11coL",
    "access_token_secret": "TdCvKQq6XffXJwP8cF7kJQUqB1gUWKK0LJK95HtqhSxLd"
}
	
keyword = '#iphone'
time = 'lastweek'
twitterData = get_twitter_data.TwitterData()
tweets = twitterData.getTwitterData(keyword, time)
print tweets

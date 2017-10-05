import tweepy

consumer_key = "m8PeFmhSkWmaOviUGckoxvQj9"
consumer_secret = "s3P3SB58UJXtKy0DHVsWOGXkLsZN9opx4IUWFezRS8wIxo3jCI"
access_token = "916044242874699783-fgjHNCDdfbDCetfQz7SsTaCEFPwTH4z"
access_token_secret = "B0I0B5dvmbsgXgUt7b6p4go6kpQOZNrexC96vKnTjxKUJ"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    hashtag = tweet.entities.get('hashtags')
    if len(hashtag) > 0: 
        print (hashtag[0]["text"])
                       

    

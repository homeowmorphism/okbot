import tweepy
# from time import sleep
from creds import *
from random import randint

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

matches = ["tell me it's going to be ok", "going to be ok?","am i going to be ok?"]

phrases = ["It's going to be ok."]
           
class StreamListener(tweepy.StreamListener):


    def on_error(self, status_code):
        if status_code == 420:
            return False


    def on_status(self, status):
        """ Ignore retweets for matching
        """
        if (not status.retweeted) and ('RT @' not in status.text.lower()):
            for match in matches:
                if match in status.text.lower():
                    try:
                        # Add \n escape character to print() to organize tweets
                        print('\nTweet by: @' + status.user.screen_name + ': ' + status.text)

                        # Retweet tweets as they are found
                        # tweet.retweet()
                        # print('Retweeted the tweet')

                        # Retweet with comment by embedding status URL 
                        url = 'https://twitter.com/' + status.user.screen_name + '/status/' + status.id_str
                        pickPhrase = phrases[randint(0, len(phrases)-1)]
                        statusMsg = pickPhrase + ' ' + url
                        api.update_status(status=statusMsg)
                        print(statusMsg)
                        # return to stream, don't look through other matches
                        # to avoid multiple-matches
                        return True

                    except tweepy.TweepError as e:
                        print(e.reason)
                        return True

        return True

print('Listening to Twitter stream')

stream_listener = StreamListener()
stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
stream.filter(track=["ok","ok?"], async=True)

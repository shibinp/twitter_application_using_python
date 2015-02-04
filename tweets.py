import oauth2 as oauth
import json

CONSUMER_KEY = "***************************"
CONSUMER_SECRET = "***********************"
ACCESS_KEY = "***********************"
ACCESS_SECRET = "**********************************"

consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
client = oauth.Client(consumer, access_token)

name= raw_input("enter name:\n")
count=raw_input("enter count of twitter:\n")
timeline_endpoint = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name="+name+"&count="+count
response, data = client.request(timeline_endpoint)

tweets = json.loads(data)
for tweet in tweets:
    print tweet['text']

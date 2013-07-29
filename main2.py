#!/usr/bin/env python



import oauth2 as oauth
import json
import tweetmanconfig as config


consumer = oauth.Consumer(key=config.consumer_key, secret=config.consumer_secret)
access_token = oauth.Token(key=config.access_token, secret=config.access_token_secret)
client = oauth.Client(consumer, access_token)

timeline_endpoint = "http://api.twitter.com/1.1/statuses/home_timeline.json"
response, data = client.request(timeline_endpoint)

tweets = json.loads(data)
for tweet in tweets:
    print tweet['text']

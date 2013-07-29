#!/usr/bin/env python

import sys, os
import getpass
import tweetmanconfig

# require tweepy with twitter API v1.1 support
# I use github version: https://github.com/tweepy/tweepy
import tweepy

print("\nWelcome to tweetman. Copyright by J.A. Nache 2013\n");

#TODO: put it on ~/config/tweetman.conf 
config = ConfigParser.ConfigParser()
config.read('tweetman.cfg')

consumer_key = config.get('oauth', 'consumerkey')
consumer_secret = config.get('oauth', 'consumersecret')
#TODO: do it automatically:
access_token = config.get('oauth', 'accesstoken')
access_token_secret = config.get('oauth', 'accesstokensecret')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
#print api.get_user()
print api.home_timeline()



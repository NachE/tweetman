#!/usr/bin/env python
import ConfigParser

#TODO: put it on ~/config/tweetman.conf
config = ConfigParser.ConfigParser()
config.read('tweetman.cfg')

consumer_key = config.get('oauth', 'consumerkey')
consumer_secret = config.get('oauth', 'consumersecret')
#TODO: do it automatically:
access_token = config.get('oauth', 'accesstoken')
access_token_secret = config.get('oauth', 'accesstokensecret')


#!/usr/bin/env python

import sys, os
import getpass
import tweepy
import ConfigParser


print("\nWelcome to tweetman. Copyright by J.A. Nache 2013\n");

#Basic Authentication is deprecated and no longer supported on Twitter.
#while True:
#	#Basic auth:
#	print("You must login twitter")
#	username = raw_input("Twitter Username: ")
#	password = getpass.getpass()
#
#	print(username, password)
#
#	auth = tweepy.BasicAuthHandler(username, password)
#	api = tweepy.API(auth)
#	if api.verify_credentials() == False:
#		print("\n\tWrong username or password\n");
#	else:
#		print("Logged")
#		break


#TODO: put it on ~/config/tweetman.conf 
config = ConfigParser.ConfigParser()
config.read('tweetman.cfg')

consumerkey = config.get('oauth', 'consumerkey')
consumersecret = config.get('oauth', 'consumersecret')
accesstoken = config.get('oauth', 'accesstoken')
accesstokensecret = config.get('oauth', 'accesstokensecret')






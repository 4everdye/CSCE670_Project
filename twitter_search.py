'''
Created on Mar 30, 2014

@author: ece
'''
import tweepy
import sys
import cjson
import json
import re
import math
from sets import Set
from random import randint
from pprint import pprint


class TwitterCrawler():
    consumer_key = "IeWxjmnvOTPyJM5tyT5Tinrzu"
    consumer_secret = "PIrJ91UUt06YHk0yabYMEqe4uZK7awWbSaYAP60uS9noVuoXKv"
    access_key = "2149706294-7J8n8EkD1PhNw66UCixV1Vb5ldTjPgPSAOssPKl"
    access_secret = "0MbzJVGxcimP5DvwRIyD57HyLS3PxWdSIGzrJ1UTESKrp"

    auth = None
    api = None


    #initialize with authentication and create API
    def __init__(self):
        self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        self.auth.set_access_token(self.access_key, self.access_secret)
        self.api = tweepy.API(self.auth)
    
    def search_single_query(self, query):
        query = tokenize(query)
        print 'Most recent 50 tweets are: \n',
        for tweet in tweepy.Cursor(self.api.search, 
                                       q=query,           
                                       result_type = 'recent', 
                                       include_entities= True, 
                                       lang = 'en').items(50):
                    print  cjson.encode(tweet.text.encode("utf-8")) 

def tokenize(string):    
    string =string.lower()
    string = re.sub(r'http:[\\/.a-z0-9]+\s?', '', string)
    string = re.sub(r'https:[\\/.a-z0-9]+\s?', '', string)
    string = re.findall(r'[a-zA-Z0-9]+',string)
    return string



if __name__ == '__main__':
    tw = TwitterCrawler()
    while True:
        
        input_query = raw_input('Please input a search query, or type "exit" to close \n')
        if input_query.lower() == 'exit':
            break
        else:
            print("Input query is:",input_query)
            tw.search_single_query(input_query)

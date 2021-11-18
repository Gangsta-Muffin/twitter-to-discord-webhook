from typing import Counter
import tweepy
import time

import requests
from discord import Webhook, RequestsWebhookAdapter
from discord.embeds import Embed
import discord
import datetime

import os
from keep_alive import keep_alive


#get "passwords" from within replit's creator-only section
consumer_key = os.environ['consumer_key']
consumer_secret = os.environ['consumer_secret']


access_token = os.environ['access_token']
access_token_secret = os.environ['access_token_secret']

webhook_id = os.environ['webhook_id']
webhook_token = os.environ['webhooktoken']


#Authentication methods to Twitter. Key must be requested at twitter.developer personally
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)





#latest tweet sent by user, exluding retweets and replies
tweet_list = api.user_timeline(screen_name="BattlefieldComm", count=1, include_rts = False, exclude_replies = True)
latest_tweet = tweet_list[0]

#tweet id of latest tweet
tweet_id = tweet_list[0].id
tweet_id_link = str(tweet_list[0].id)

#get the contents of the latest tweets (simply doing "latest_tweet.text" will restrict the recieved tweet message to 140 charakters)
tweet_msg_fetch = api.get_status(tweet_id, tweet_mode="extended")
tweet_msg = tweet_msg_fetch.full_text

#print latest tweets, plus a url to the tweet
print(tweet_msg)
print("https://twitter.com/BattlefieldComm/status/" + tweet_id_link)


#set most recent recorded tweet to tweet id for boot-up and functionality purposes (when starting the programm, latest tweet will not be posted)
last_uploaded_tweet = tweet_id



#webhook link for footer and discord webhook connect
tweet_url = ("https://twitter.com/BattlefieldComm/status/" + tweet_id_link)
webhook = Webhook.partial(webhook_id, webhook_token, adapter = RequestsWebhookAdapter())


#set point for the monitor to keep the code running
keep_alive()


#beging of loop process
while True:


    #get latest tweet contents (view steps above)
    tweet_list = api.user_timeline(screen_name="BattlefieldComm", count=1, include_rts = False, exclude_replies = True)
    latest_tweet = tweet_list[0]


    tweet_id = tweet_list[0].id
    tweet_id_link = str(tweet_list[0].id)


    tweet_msg_fetch = api.get_status(tweet_id, tweet_mode="extended")
    tweet_msg = tweet_msg_fetch.full_text

    #info perposes for creator(tweet id, tweet content, last recorded tweet)
    print(tweet_msg)
    print(tweet_id)
    
    print("")
    
    print(last_uploaded_tweet)
    
    print("")


    time.sleep(1)


    #check if the tweet is new by comparing ids

    if tweet_id == last_uploaded_tweet:
        print("no tweet")
        time.sleep(1)
    
    else:
        print("new tweet")


        #create embedformat and content for webhook message to be sent. Set last recorded tweet-id to newest tweet-id
        embedWebhook = discord.Embed(title="Breaking News", description=tweet_msg, color=0x07877a)
        embedWebhook.set_footer(text=tweet_url)
        embedWebhook.timestamp = datetime.datetime.utcnow()

        webhook.send(username="TWITTER NEWS", embed = embedWebhook)

        
        last_uploaded_tweet = tweet_list[0].id
        time.sleep(1)

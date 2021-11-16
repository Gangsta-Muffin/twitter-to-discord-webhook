from typing import Counter
import tweepy
import time

import requests
from discord import Webhook, RequestsWebhookAdapter
from discord.embeds import Embed
import discord
import datetime



#Authentication methods to Twitter. Key must be requested at twitter.developer personally
auth = tweepy.OAuthHandler("JDBhnKNuHPCXlQW3hY8UnxWgA", "HMfEnREwFkL5abHojl7FHpybCz5ZPfEZWxGGHqu8imqPVVhNoR")
auth.set_access_token("1286728460778471424-05tLVj5ly9ymVPDQKxK3cPhec1BhRC", "4BRMM2ElY5kcsAqM5EmDIEIhMdLhhs7HmiqNOTK9y4n7K")

api = tweepy.API(auth)





#latest tweet
tweet_list = api.user_timeline(screen_name="Battlefield", count=1, include_rts = False, exclude_replies = True)
latest_tweet = tweet_list[0]
tweet_msg = latest_tweet.text

#tweet id of latest tweet
tweet_id = tweet_list[0].id
tweet_id_link = str(tweet_list[0].id)


#print latest tweets, plus a url to the tweet
print(latest_tweet.text)
print("https://twitter.com/Battlefield/status/" + tweet_id_link)


#set most recent recorded tweet to tweet id for boot-up and functionality purposes
last_uploaded_tweet = tweet_id



#webhook link for footer and discord webhook url
tweet_url = ("https://twitter.com/Battlefield/status/" + tweet_id_link)
webhook = Webhook.partial(909927982712365117, "HcRVYteIjRNS4FnwDYMySJ0kDmXIThfRtTWcesZPdY03NHx76iQErKfgpeOqwltbqrlT", adapter = RequestsWebhookAdapter())





#beging of loop process
while True:



    tweet_list = api.user_timeline(screen_name="Battlefield", count=1, include_rts = False, exclude_replies = True)
    latest_tweet = tweet_list[0]
    tweet_msg = latest_tweet.text


    tweet_id = tweet_list[0].id
    tweet_id_link = str(tweet_list[0].id)


    #info perposes for creator(tweet id, tweet content, last recorded tweet)
    print(tweet_msg)
    print(tweet_id)
    
    print("")
    
    print(last_upload_tweet)
    
    print("")


    time.sleep(1)


    #check if the tweet is new by comparing ids

    if tweet_id == last_upload_tweet:
        print("no tweet")
        time.sleep(1)
    
    else:
        print("new tweet")


        #create embedformat and content for webhook message to be snet
        embedWebhook = discord.Embed(title="Breaking News", description=tweet_msg, color=0x07877a)
        embedWebhook.set_footer(text=tweet_url)
        embedWebhook.timestamp = datetime.datetime.utcnow()

        webhook.send(username="A_Team", embed = embedWebhook)

        
        last_upload_tweet = tweet_list[0].id
        time.sleep(1)
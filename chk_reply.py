#!/usr/bin/python
# -*- coding: utf-8 -*-

import tweepy
from datetime import datetime, timedelta
import subprocess
import time
from tweet_temp import now_str

### Import the bot's information
### consumer_key, consumer_secret, access_token, access_token_secret
from password_bot import *


### Air Conditioner Command
ON_CMD = '/home/naoya/c/sendir /home/naoya/c/pon.data 3 24'
OFF_CMD = '/home/naoya/c/sendir /home/naoya/c/poff.data 3 24'

CHK_INTERVAL_MIN = 5

def my_reply(api, reply_to_status, text):
    screen_name = reply_to_status.author.screen_name.encode("UTF-8")
    return api.update_status('@' + screen_name + " " + text + now_str(), \
                             in_reply_to_status_id = reply_to_status.id)

if __name__ == "__main__":

    # Authentication
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    # メンションから "つけて" / "けして" を探し、
    # あればエアコンにコマンドを送る
    # 最新のものから順に20件取得
    # CHK_INTERVAL_MIN 分以上前のものにヒットしたら break
    for status in api.mentions_timeline(count=20):
        
        #print status.id
        if datetime.now() - status.created_at \
           <= timedelta(hours=9, minutes=CHK_INTERVAL_MIN): #GMT+9

            print status.created_at+timedelta(hours=9) #GMT+9
            
            if status.text.find(u'つけて') >= 0 and status.text.find(u'けして') < 0:
                subprocess.call(ON_CMD,shell=True)
                time.sleep(0.5)
                subprocess.call(ON_CMD,shell=True)
                my_reply(api, status, "エアコンを付けました")
                print "ON"
                break
            
            elif status.text.find(u'つけて') < 0 and status.text.find(u'けして') >= 0:
                subprocess.call(OFF_CMD,shell=True)
                time.sleep(0.5)
                subprocess.call(OFF_CMD,shell=True)
                my_reply(api, status, "エアコンを消しました")
                print "OFF"
                break
            
            else:
                my_reply(api, status, "わかりません。")
                print "解釈不能"

#        else:
#            break

    # ユーザのフォローを取得
    # user = api.get_user('eggplant60')
    # print user.screen_name
    # print user.followers_count
    # for friend in user.friends():
    #     print friend.screen_name

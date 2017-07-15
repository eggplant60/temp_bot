#!/usr/bin/python
# -*- coding: utf-8 -*-

import tweepy
from datetime import datetime
import am2320

### Import the bot's information
### consumer_key, consumer_secret, access_token, access_token_secret
from passward_bot import *


def now_str():
    return datetime.now().strftime(' (%Y/%m/%d %H:%M)')


if __name__ == "__main__":

    # Authentication
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    # tweet temparature and humidity
    am_obj = am2320.Thermo()
    tmp = am_obj.getTmp()
    hum = am_obj.getHum()
    body = 'ただいまの室温: ' + str(tmp) \
           + '度、湿度:' + str(hum) + '%' + now_str()
    print body
    api.update_status(body)


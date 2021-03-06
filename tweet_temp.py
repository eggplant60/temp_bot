#!/usr/bin/python
# -*- coding: utf-8 -*-

import tweepy
from datetime import datetime
import am2320
import time

### Import the bot's information
### consumer_key, consumer_secret, access_token, access_token_secret
from password_bot import *


def now_str():
    return datetime.now().strftime(' (%Y/%m/%d %H:%M)')


if __name__ == "__main__":

    # Authentication
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    # tweet temparature and humidity
    am_obj = am2320.Thermo()
    time.sleep(1)

    for i in range(3):  # try third times
        tmp = am_obj.getTmp()
        hum = am_obj.getHum()
        if  tmp == 0.0 and hum == 0.0:
            time.sleep(am2320.READ_INT)
        else:
            break

    body = 'ただいまの室温: ' + str(tmp) \
           + '度、湿度:' + str(hum) + '%' + now_str()
        
    print body
    api.update_status(body)


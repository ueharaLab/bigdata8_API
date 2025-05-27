
#bodyのパラメータは以下参照
#https://webservice.recruit.co.jp/doc/hotpepper/reference.html

import codecs
import pprint
import pandas as pd
import requests
import urllib
URL = 'http://webservice.recruit.co.jp/hotpepper/gourmet/v1/'

API_KEY = 'c5779900dcb068ed'

body = {
    'key':API_KEY,
    'keyword':'東京駅',
    'address':'丸の内',
    'course':1,
    'format':'json',
    'count':100
}

response = requests.get(URL,body)
datum = response.json()

stores = datum['results']['shop']
for store in stores:
    print(store)
    


#bodyのパラメータは以下参照
#https://webservice.recruit.co.jp/doc/hotpepper/reference.html

import codecs
import pprint
import pandas as pd
import requests
URL = 'http://webservice.recruit.co.jp/hotpepper/gourmet/v1/'

API_KEY = 'c5779900dcb068ed'
body = {
    'key':API_KEY,
    'keyword':'東京駅',
    'address':'丸の内',
    'course':1,
    'format':'json',
    'count':5
}

response = requests.get(URL,body)
datum = response.json()
#print(datum)
#pprint.pprint(datum)


stores = datum['results']['shop']
'''
store_info=[]
for store in stores:
    print(store)
    store_info.append(store)

store_df = pd.DataFrame(stores)
print(store_df)
with codecs.open("hotpepper.csv", "w", "ms932", "ignore") as f: 
    #header=Trueで、見出しを書き出す
    store_df.to_csv(f, index=False, encoding="ms932", mode='w', header=True)
'''
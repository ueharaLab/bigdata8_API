import requests
import pprint
import time
import pandas as pd
import codecs

url = 'http://webservice.recruit.co.jp/hotpepper/gourmet/v1/'

API_KEY = ''



start = ####
count = ####

#store_list = []
while True:

    body = {
        'key': API_KEY,
        'genre': '####',
        'format': 'json',
        'start': start,
        'count': count
    }

    response = requests.get(url, params=body)
    
    datum = response.json()

    stores = datum['results']['shop']
    
    for store in stores:
        print(store['name'], store['address'])
        print(store['lat'],store['lng'])
        
        #store_list.append([store['name'], store['address'],store['lat'],store['lng']])
        
    
    start += ####
    print(start)    
    
    time.sleep(1)
    
'''
store_df = pd.DataFrame(store_list, columns=['name','address', 'lat','lng'])
with codecs.open('stores.csv', 'w', 'shift-jis', 'ignore') as f:
    store_df.to_csv(f)
'''
    
    
    


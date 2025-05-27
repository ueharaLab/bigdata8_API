import requests
import pandas as pd
APP_ID = ""


url = 'https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData?'
url += 'appId={0:s}&'.format(APP_ID) 
url += 'statsDataId={0:s}&'.format('0003317356')
url += 'metaGetFlg=Y&'          
url += 'explanationGetFlg=N&'   
url += 'annotationGetFlg=N&'    
url += 'limit=40'

# 統計データ取得
json = requests.get(url).json()
print(json)
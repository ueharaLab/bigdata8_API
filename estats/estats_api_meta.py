import requests
import pandas as pd
APP_ID = ""

url = 'https://api.e-stat.go.jp/rest/3.0/app/json/getMetaInfo?'
url += 'appId={0:s}&'.format(APP_ID) 
url += 'statsDataId={0:s}&'.format('0003317356')
url += 'explanationGetFlg=N&'   # 解説情報有無：無し

# メタ情報取得
json = requests.get(url).json()
print(json)


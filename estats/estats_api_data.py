import requests
import pandas as pd
APP_ID = ""


url = 'https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData?'
url += 'appId={0:s}&'.format(APP_ID) 
url += 'statsDataId={0:s}&'.format('0003317356')
url += 'metaGetFlg=Y&'          # メタ情報有無
url += 'explanationGetFlg=N&'   # 解説情報有無
url += 'annotationGetFlg=N&'    # 注釈情報有無
url += 'limit=100'


# 統計データ取得
json = requests.get(url).json()

# 統計データからデータ部取得
values = json['GET_STATS_DATA']['STATISTICAL_DATA']['DATA_INF']['VALUE']
print(values)

import requests
import pandas as pd
APP_ID = "14060f0bcc7785b450fea7cafb2ef11addf7403f"


url = 'https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData?'
url += 'appId={0:s}&'.format(APP_ID) 
url += 'statsDataId={0:s}&'.format('0003317356')
url += 'metaGetFlg=Y&'          # メタ情報有無
url += 'explanationGetFlg=N&'   # 解説情報有無
url += 'annotationGetFlg=N&'    # 注釈情報有無


# 統計データ取得
json = requests.get(url).json()


def create_metadict(data):
    
    df = pd.DataFrame(data)
    return df


meta = json['GET_STATS_DATA']['STATISTICAL_DATA']['CLASS_INF']['CLASS_OBJ']
for m in meta:
    
    if '都道府県' in m['@name'] :
        print(m['CLASS'])
        area = create_metadict(m['CLASS'])
        #pref_dic = [for k,v in m['CLASS'].items() if k==
    if '国籍' in m['@name'] :
        #print(m['CLASS'])
        cat02 = create_metadict(m['CLASS'])

print(area)
print(cat02)
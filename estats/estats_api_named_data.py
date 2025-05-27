import requests
import pandas as pd
import codecs

APP_ID = ""


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

values = json['GET_STATS_DATA']['STATISTICAL_DATA']['DATA_INF']['VALUE']
data = pd.DataFrame(values)

area = area.set_index('@code')
cat02 = cat02.set_index('@code')
named_data = []
for i,d in data.iterrows():
    
    country_code = d['@cat02']
    country = cat02.loc[country_code,'@name']
    pref_code = d['@area']
    pref = area.loc[pref_code,'@name']
    named_data.append([country_code,country,pref_code,pref,d['@time'],d['@unit'],d['$']])

named_data_df = pd.DataFrame(named_data,columns =['contry code','country name', 'pref code','pref code','time','unit','value'])
with codecs.open("named_data.csv", "w", "ms932", "ignore") as f: 
    #header=Trueで、見出しを書き出す
    named_data_df.to_csv(f, index=False, encoding="ms932", mode='w', header=True)
import pprint
import json
import requests

#Pandasをインポート
import pandas as pd
from pandas.io.json import json_normalize

city = '13120' # 練馬区
from_quarter = '20201' # クオータで指定
to_quarter = '20202' # クオータで指定
baseuri='https://www.land.mlit.go.jp/webland/api/TradeListSearch?'
uri = baseuri + 'city=' + city + "&from=" + from_quarter + "&to=" + to_quarter
headers = {'content-type': 'application/json'}

# API Get Request
response = requests.get(
  uri,
  headers=headers)

#CSV OUTPUT
#変換したいJSONファイルをpandasに流し込む
df = pd.read_json(response.text)
print(df)

#変換+CSV出力
df_json = json_normalize(df['data'])
df_json.to_csv("Nerima.csv", encoding='utf-8')


#ピボット試してみる　APIから取得したjsonだとindexの設定がされていないためCSV再入力
df2 = pd.read_csv("Nerima.csv")
print(df2["DistrictName"].value_counts())

# ピボットはCLIのためちょいみにくし
# print(pd.pivot_table(df2,index=['DistrictName','Period'],columns='Type',aggfunc='count'))



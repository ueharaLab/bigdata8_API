import csv
import requests

URL = 'https://webservice.recruit.co.jp/hotpepper/genre/v1/'
API_KEY = ''  # ここに取得したAPIキーを入力

body = {
    'key': API_KEY,
    'format': 'json'
}

if not API_KEY:
    raise ValueError('API_KEY にホットペッパーのAPIキーを入力してください。')

response = requests.get(URL, params=body, timeout=20)
response.raise_for_status()
datum = response.json()

results = datum.get('results', {})
if 'error' in results:
    raise RuntimeError(f"APIエラー: {results['error']}")

genres = results.get('genre', [])
if isinstance(genres, dict):
    genres = [genres]
if not genres:
    raise RuntimeError(f'ジャンル情報が取得できませんでした: {results}')

with open('hotpepper_genres.csv', 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    writer.writerow(['code', 'name', 'catch'])
    for genre in genres:
        writer.writerow([
            genre.get('code', ''),
            genre.get('name', ''),
            genre.get('catch', '')
        ])
        print(genre.get('code', ''), genre.get('name', ''))

print(f'{len(genres)}件を hotpepper_genres.csv に保存しました。')

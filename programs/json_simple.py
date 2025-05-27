import json


s = {"C": "あ", "A": {"i": 1, "j": 2}, "B": [{"X": 1, "Y": 10}, {"X": 2, "Y": 20}]}

print(s)

print(s['A']['i'])
print(s['B'][0]['Y'])


with open('test.json', 'w',encoding='utf-8') as f:
    json.dump(s, f)
    
with open('test.json',encoding="utf-8") as f:
    t = json.load(f)
print(t)

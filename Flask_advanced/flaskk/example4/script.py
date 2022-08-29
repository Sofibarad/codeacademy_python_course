import requests
import json

payload = {'name': 'Apple', 'price': '500', 'count': "1"}
r = requests.post('http://127.0.0.1:5000/', json=payload)
dictionary = json.loads(r.text)
print(dictionary)

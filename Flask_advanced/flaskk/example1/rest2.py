import requests
import json

r2 = requests.get('http://127.0.0.1:5000/keliamieji/2100')
dictionary2 = json.loads(r2.text)
print(dictionary2['result'])

# NE Keliamieji
import json
import requests


r = requests.post('http://127.0.0.1:8000/uzduotis', json=nauja_uzduotis)
print(json.loads(r.text))
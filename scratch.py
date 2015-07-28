import requests
import json


def getdailyquote():
    resp = requests.get('http://api.theysaidso.com/qod')
    data = json.loads(resp.text)
    quote = data['contents']['quotes'][0]['quote']
    return quote


getdailyquote()
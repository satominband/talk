#!/Users/ykiyoshima/opt/anaconda3/envs/satominband/bin/python
# -*- coding: utf-8 -*-

import sys
import requests
import os
import cgi
from dotenv import load_dotenv
load_dotenv()

storage = cgi.FieldStorage()
data = storage.getvalue('data')
apikey = 'DZZNx6Z5eBHH7qFixKooNc4XRLIZ4Q4V'
talk_url = "https://api.a3rt.recruit.co.jp/talk/v1/smalltalk"
payload = {"apikey": apikey, "query": data}
response = requests.post(talk_url, data=payload)
try:
    print(response.json()["results"][0]["reply"])
except:
    print(response.json())
    print("ごめんなさい。もう一度教えて下さい。")
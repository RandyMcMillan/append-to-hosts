#!/usr/local/bin/python3

# sudo pip3 install json
# sudo pip3 install requests

import json
import requests

response = requests.get("https://hodlister.co/electrum-server-blacklist.json")
response.status_code
print response.status_code


blacklist = json.loads(response.text)


print blacklist[0].strip('"')
#print blacklist[1]


import io, json

with io.open('blacklist.json', 'w', encoding='utf-8') as f:
  f.write(json.dumps(blacklist, ensure_ascii=False, indent=None))
with io.open('hosts', 'w', encoding='utf-8') as f:
  f.write(json.dumps(blacklist, ensure_ascii=False,separators=None, indent=None))

my_iterator = iter(blacklist)

next(my_iterator)

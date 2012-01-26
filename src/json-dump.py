# -*- coding: utf-8 -*-

import codecs
import json

data = {"results":[
  {
    "name": u"国立霞ヶ丘競技場",
    "latitude": 139.714941,
    "longitude": 35.678160,
    "description": "naash.go.jp"
  },
  {
    "name": u"味の素スタジアム",
    "latitude": 139.5272,
    "longitude": 35.6646,
    "description": "http://www.ajinomotostadium.com/\n"
                   u"元の名称: 東京スタジアム"
  }
]}
with codecs.open('out.json','w','utf-8') as writer:
    json.dump(data, writer, indent=4, ensure_ascii=False)
print "Wrote to \"out.json\"."


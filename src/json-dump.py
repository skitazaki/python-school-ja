#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

data = {"results":[
  {
    "name": "国立霞ヶ丘競技場",
    "latitude": 139.714941,
    "longitude": 35.678160,
    "description": "naash.go.jp"
  },
  {
    "name": "味の素スタジアム",
    "latitude": 139.5272,
    "longitude": 35.6646,
    "description": "http://www.ajinomotostadium.com/\n" +
                   "元の名称: 東京スタジアム"
  }
]}
with open('out.json', 'w', encoding='utf-8') as writer:
    json.dump(data, writer, indent=4, sort_keys=True, ensure_ascii=False)
print('Wrote to "out.json".')

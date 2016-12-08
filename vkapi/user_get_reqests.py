#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from my_data import myVkData

response = requests.get(myVkData.API_URL+'users.get',
                        {'user_ids': myVkData.DUROV_USER_ID+','+myVkData.MY_USER_ID+','+myVkData.TOKEN})
result = response.text
print(result)

import json
response = json.loads(result)
users = response['response']

[print(user) for user in users]


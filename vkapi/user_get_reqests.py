# -*- coding: utf-8 -*-

import requests
from my_data import myVkData

response = requests.get(myVkData.API_URL+'user.get',
                        {'user_ids': myVkData.DUROV_USER_ID+','+myVkData.MY_USER_ID})
result = response.text
print(result)

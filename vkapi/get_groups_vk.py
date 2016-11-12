# -*- coding: utf-8 -*-

import vk
from my_data import myVkData

session = vk.AuthSession(app_id=myVkData.APP_ID, user_login=myVkData.LOGIN, user_password=myVkData.GET_PASSWORD())
vkapi = vk.API(session)

groups = vkapi.groups.get(user_id=myVkData.MY_USER_ID, extended=1)

groups_count = groups[0]
print('Количество групп:%d'%(groups_count))

groups = groups[1:]

[print(group) for group in groups]
# -*- coding: utf-8 -*-

import vk
from my_data import myVkData

session = vk.AuthSession(app_id=myVkData.APP_ID,
                         user_login=myVkData.LOGIN,
                         user_password=myVkData.GET_PASSWORD())
vkapi = vk.API(session)

groups = vkapi.groups.search(q='Python', count=36)

groups_count = groups[0]
print('Количество групп по теме:%d'%(groups_count))

groups = groups[1:]

[print(group) for group in groups]


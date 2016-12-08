#!/usr/bin/env python
# -*- coding: utf-8 -*-

import vk
from my_data import myVkData

session = vk.Session()
vkapi = vk.API(session)

friends = vkapi.friends.get(user_id=myVkData.MY_USER_ID,
                            fields='domain,photo')

print('Количество моих друзей: %d'%(len(friends)))

[print(friend) for friend in friends]
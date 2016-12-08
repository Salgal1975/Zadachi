#!/usr/bin/env python
# -*- coding: utf-8 -*-

import vk
from my_data import myVkData

session = vk.AuthSession(app_id=myVkData.APP_ID,
                         user_login=myVkData.LOGIN,
                         user_password=myVkData.GET_PASSWORD(),
                         scope='wall')
vkapi = vk.API(session)

MESSAGE = 'HELLO IS HOME'
vkapi.wall.post(message=MESSAGE)

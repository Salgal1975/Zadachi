# -*- coding: utf-8 -*-

import vk
from my_data import myVkData

session = vk.AuthSession(app_id=myVkData.APP_ID,
                         user_login=myVkData.LOGIN,
                         user_password=myVkData.GET_PASSWORD(),
                         scope='wall')
vkapi = vk.API(session)


INTERESTS = ['Python', 'Программирование', 'Stm32']

AGE_FROM = 18  # возраст
AGE_TO = 20

SEX = 2  # 1-женский, 2-мужской
CITY = 1  # Москва

users = vkapi.users.search(interests=','.join(INTERESTS),
                           city=CITY,
                           sex=SEX,
                           age_from=AGE_FROM,
                           age_to=AGE_TO,
                           fields='photo_big,domain')

users = users[1:]

[print(user) for user in users]

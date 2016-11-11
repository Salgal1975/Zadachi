# -*- coding: utf-8 -*-

class myVkData:
    # идентификатор моего пользователя
    MY_USER_ID = '281430849'
    # идентификатор DUrova
    DUROV_USER_ID = '1'
    # Ссылка для доступа к api
    API_URL = 'https://api.vk.com/method/'
    # идентификатор приложения в контакте
    APP_ID = '5724105'
    # логин пользователя
    LOGIN = '+79825448154'

    # пароль в контакте
    @staticmethod
    def GET_PASSWORD():
        f = open('/Users/GST/Desktop/pass.txt', 'r')
        passw = f.read().rstrip()
        f.close()
        return passw

if __name__ == '__main__':
    passw = myVkData.GET_PASSWORD()
    print(passw)
    #print('end')

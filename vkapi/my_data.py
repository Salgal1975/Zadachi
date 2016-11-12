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
    TOKEN = '+token'

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

#  access_token=79b19648b990b41b6a5ed981753dd5d1bf243d000dae7db000a5d234f437a194f694afb076b966d80a449&expires_in=86400&user_id=281430849&state="kkkk"
#git remote add origin https://github.com/Salgal1975/Zadachi.git
# -*- coding: utf-8 -*-


def vreminaGoda (month):
    god = [(12, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11)]
    if month in god[0]:
        return print('Зима')
    elif month in god[1]:
        return print('Весна')
    elif month in god[2]:
        return print('Лето')
    elif month in god[3]:
        return print('Осень')



if __name__ == '__main__':

   vreminaGoda(int(input('Введите номер месяца:')))

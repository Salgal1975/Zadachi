# -*- coding: utf-8 -*-


def bank(vklad, years):
    for i in 10:
        vklad += vklad/100*10
    return print(vklad)





if __name__ == '__main__':

    bank((int(input('Введите сумму вклада:'))), (input('На сколько лет:')))
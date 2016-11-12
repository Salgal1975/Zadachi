#!/usr/bin/python3
# -*- coding: utf-8 -*-

import math

def square(arg1):
    P = ('Периметр квадрата = {}'.format(arg1*4))
    S = ('Площадь квадрата = {}'.format(arg1**2))
    D = ('Диоганаль квадрата = {}'.format(arg1*math.sqrt(2)))
    res = (P,S,D,)
    return print(res)





if __name__ == '__main__':
    g = input('Введите сторону квадрата:')

    if g == type(int) :

    	square(int(g))

    else:
    	print('Это не число!! Введите число!')
    	


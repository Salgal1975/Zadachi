#!/usr/bin/python3
# -*- coding: utf-8 -*-

import math

def arifmet (a=int(input('Введите чило=')), b=int(input('Введите 2-е чило=')), c=(input('Введите арифметическую операцию(+,-,*,/)='))):




     if c=='+':
         s=('Сумма: {0} + {1} = {2}'.format(a,b,a+b))
     elif c=='-':
         s=('Разность: {0} - {1} = {2}'.format(a,b,a-b))
     elif c=='/':
         s=('Частное: {0} / {1} = {2}'.format(a,b,a/b))
     elif c=='*':
        s=('Произведение: {0} * {1} = {2}'.format(a,b,a*b))
     else: s='Неизвестная операция'


     return  print(s)



if __name__ == '__main__':
    arifmet()
    input()

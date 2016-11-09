#!/usr/bin/python3
# -*- coding: utf-8 -*-

def is_year_leap(a):
    if a % 4 == 0 or (a % 100 != 0 and a % 400 == 0):
        visocos = (print('{} - год высокосный   '.format(a)))
        return visocos
    else:
        novisocos = print('{} - год не высокосный'.format(a))
        return novisocos 

def god(n=int(input('Введите начало:')),k=int(input('Введите конец:'))):
    for count in range(n,k+1):
        is_year_leap(count)


if __name__ == '__main__':
    god()
    input()

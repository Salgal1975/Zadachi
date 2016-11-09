#!/usr/bin/python3
# -*- coding: utf-8 -*-

def is_year_leap(a):
    if (a % 100 != 0 and a % 400 == 0) or a % 4 == 0:
        print('{} - год высокосный   '.format(a))
        return True
    else:
        print('{} - год не высокосный'.format(a))
        return False

def god(n=int(input('Введите начало:')), k=int(input('Введите конец:'))):
    for count in range(n, k+1):
        is_year_leap(count)



import unittest


class YearTestCase(unittest.TestCase):

    def test_year_leap(self):

        for year in (2000, 2016, 1916):
            with self.subTest(year=year):
                self.assertTrue(is_year_leap(year),
                                "{} на самом деле високосный".format(year))

    def test_year_notleap(self):

        for year in (1900, 2014, 2001):
            with self.subTest(year=year):
                self.assertFalse(is_year_leap(year),
                                 "{} на самом деле не високосный".format(year))


if __name__ == '__main__':
    god()
    input()
    unittest.main ()

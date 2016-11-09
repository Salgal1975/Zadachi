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

import unittest

class SeasonTestCase (unittest.TestCase):

    def test_season(self):
        seasons = [None,'зима','зима','весна','весна','весна',
                       'лето','лето','лето','осень','осень','осень','зима']

        for month in range (1,13):
            with self.subTest (month=month):
                    self.assertEqual (season (month).lower (),seasons[month])

    if __name__ == "__main__":

        vreminaGoda(int(input('Введите номер месяца:')))
        unittest.main ()




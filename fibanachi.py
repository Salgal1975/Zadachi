# -*- coding: utf-8 -*-
import math

def is_prime(namber):

     if namber == 1:
         print(False)
         return False

     for i in range(2, namber):
         if namber % i == 0:
             print(False)
             return False
     print(True)
     return True


if __name__ == "__main__":
    is_prime(int(input("Ввидите число:")))

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Number: №37
    Task: Заданы размеры A, B прямоугольного отверстия и размеры x, y, z кирпича.
    Определить пройдёт ли кирпич через отверстие
"""

a, b, x, y, z = int(input()), int(input()), int(input()), int(input()), int(input())

if (a >= x and b >= y) or (a >= y and b >= x) or (a >= x and b >= z) or (a >= z and b >= x) or (a >= z and b >= y) or (a >= y and b >= z):
    print('Да!')
else:
    print('Нет!')

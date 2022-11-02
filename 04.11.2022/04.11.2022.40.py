#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Number: №40
    Task: Небоскрёб
"""

n = int(input('Введите количество этажей '))
flat = int(input('Введите номер нужной квартиры '))

state = (flat + 2) // 3

if state % 2 == 0:
    state -= 1

print(f'Лифт остановится на {state} этаже')

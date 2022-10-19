#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" 
    Number: №2
    Task: Определить, является ли целое число чётным двузначным числом
"""

number = int(input())

if 9 < number < 100 and number % 2 == 0:
    print('Да')
else:
    print('Нет')

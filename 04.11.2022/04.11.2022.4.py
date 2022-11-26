#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Number: №74
    Task: Перевод метров в другие величины
"""

option = input(
    'Выбери, в какую величину перевести метры:\n'
    '1) дециметры\n'
    '2) километры\n'
    '3) метры\n'
    '4) миллиметры\n'
    '5) сантиметры\n'
    '>> '
)

l = int(input('Введите длину в метрах: '))

if option == '1':
    print(f'{l} м. = {l * 10} дм.')

elif option == '2':
    print(f'{l} м. = {l / 1000} км.')

elif option == '3':
    print(f'{l} м. = {l} м.')

elif option == '4':
    print(f'{l} м. = {l * 1000} мм.')

elif option == '5':
    print(f'{l} м. = {l * 100} cм.')

else:
    print('Нет такого варианта!')

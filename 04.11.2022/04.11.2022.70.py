#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Number: №70
    Task: Пусть элементами прямоугольного равнобедренного треугольника являются:
        1) катет a
        2) гипотенуза b
        3) высота опущенная из вершины прямого угла на гипотенузу h
        4) площадь S
"""

option = input(
    'Привет! Выбери один из вариантов, что тебе известно (введи всего одно число):\n'
    '1) Катет a\n'
    '2) Гипотенуза b\n'
    '3) Высота опущенная из вершины прямого угла на гипотенузу h\n'
    '4) Площадь S\n'
    '>> '
)

if option == '1':
    a = int(input('А теперь введи значение катета: '))

    b = (a ** 2 * 2) ** .5
    h = (a * a) / b
    s = (b * h) / 2

    print(f'Гипотенуза равна: {b}')
    print(f'Высота опущенная из вершины прямого угла на гипотенузу равна: {h}')
    print(f'Площадь равна: {s}')

elif option == '2':
    b = int(input('А теперь введи значение гипотенузы: '))

    a = (b ** 2 / 2) ** .5
    h = (a * a) / b
    s = (b * h) / 2

    print(f'Катет равен: {a}')
    print(f'Высота опущенная из вершины прямого угла на гипотенузу равна: {h}')
    print(f'Площадь равна: {s}')

elif option == '3':
    h = int(input('А теперь введи значение высоты опущенной из вершины прямого угла на гипотенузу: '))

    b = 2 * h
    a = (b ** 2 / 2) ** .5
    h = (a * a) / b
    s = (b * h) / 2

    print(f'Катет равен: {a}')
    print(f'Гипотенуза равна: {h}')
    print(f'Площадь равна: {s}')

elif option == '4':
    s = int(input('А теперь введи значение площади: '))
    b = (s * 4) ** .5
    a = (b ** 2 / 2) ** .5
    h = (a * a) / b
    s = (b * h) / 2

    print(f'Катет равен: {a}')
    print(f'Высота опущенная из вершины прямого угла на гипотенузу равна: {h}')
    print(f'Гипотенуза равна: {h}')

else:
    print('Нет такого варианта!')

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Number: 114
    Task: Натуральные числа a, b, c называются числами Пифагора, если выполняется условие a^2 + b^2 = c^2.
    Напечатать все числа Пифагора, меньшие N.
"""

n = int(input())

for a in range(1, n):
    for b in range(a, n):
        d = a * a + b * b
        for c in range(2, n):
            if d == c * c:
                print(f'{a = }, {b = }, {c = }')

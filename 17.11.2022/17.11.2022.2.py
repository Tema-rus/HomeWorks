#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Number: 35
    Task: Дано натуральное число n. Вычислить:
    S = 1! + 2! + 3! + ... + n! (n > 1)
"""

n = int(input())
s = 0
for i in range(2, n + 1):
    fac = 1
    for j in range(2, i + 1):
        fac *= j
    s += fac
print(s)

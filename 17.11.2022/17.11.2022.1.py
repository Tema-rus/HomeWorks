#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Number: 22
    Task: Дано натуральное число N. Вычислить произведение первых N сомножителей.
"""

n = int(input())
p = 1
for i in range(1, n + 1):
    p *= (2 * i) / (2 * i + 1)
print(p)

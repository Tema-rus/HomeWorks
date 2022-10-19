#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Number: №1
    Task: Определить, равен ли квадрат заданного трёхзначного числа кубу суммы цифр этого числа
"""

number = int(input())

trd, snd, fst = number % 10, number // 10 % 10, number // 100

square = number * number
cube = (fst + snd + trd) ** 3

if cube == square:
    print('Да')
else:
    print('Нет')

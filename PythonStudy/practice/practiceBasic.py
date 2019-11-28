# -*- coding:utf-8 -*-
# @Time : 2019/11/14 8:49 下午
# @Author: zhr619151879
# @File : practiceBasic.py
from math import sqrt

def joseph_ring():
    persons = [True] * 30
    counter, index, number = 0, 0, 0
    while counter < 15:
        if persons[index]:
            number += 1
            if number == 9:
                persons[index] = False
                counter += 1
                number = 0
        index += 1
        index %= 30
    for person in persons:
        print('基' if person else '非', end ='')


def verification_code(num = 4):
    verification = ''
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    random_len = len(all_chars)
    for _ in range(num):
        verification += all_chars[random.randint(0, random_len)]
    return verification


def is_palindrome(num):
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == num


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
        yield result


def triangles():
    L = [1]
    while True:
        yield L
        L = [1] + [L[i] + L[i + 1] for i in range(len(L) - 1)] + [1]



def prime():
    for num in range(2, 100):
        for i in range(2, int(sqrt(num) + 1)):
            if num % i == 0:
                return False
    return True

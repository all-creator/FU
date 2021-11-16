from math import *


def first(num):
    print(0.5 * num * (num-1))


def second(n, k):
    print(factorial(n)/(factorial(k)*factorial(n-k)))


def third(n, k):
    print(factorial(n)/(factorial(k)*factorial(n-k)))


first(1)
second(4, 2)
third(8, 3)

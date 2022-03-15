import math

from scipy.stats.distributions import chi2


def calc(n_, s_, y_, type_=False):
    right = chi2.ppf((1 - y_) / 2, df=n_ - 1)
    left = chi2.ppf((1 + y_) / 2, df=n_ - 1)
    if type_:
        print(f"{pow((n_ - 1) * s_ / left, 0.5)} < a < {pow((n_ - 1) * s_ / right, 0.5)}")
    else:
        print(f"{pow(n_ * s_ / left, 0.5)} < a < {pow((n_ - 1) * s_ / right, 0.5)}")


def calc_altr(n_, s_, y_):
    right = ((n_ - 1) * s_) / chi2.ppf((1 - y_) / 2, df=n_ - 1)
    left = ((n_ - 1) * s_) / chi2.ppf((1 + y_) / 2, df=n_ - 1)
    print(f"{left} < a < {right}")


print("Задание 1")

n = 101
s = 16
y = 0.95

calc(n, s, y)

print("Задание 2")

n = 61

calc(n, s, y)

print("Задание 3")

n = 25
s = 9
y = 0.98

calc(n, s, y, True)

print("Задание 4")

n = 20
s = 225
y = 0.90

calc_altr(n, s, y)

n = 101

calc_altr(n, s, y)

print("Задание 5")

n = 16
s = 1
y = 0.95

calc_altr(n, s, y)

print("Задание 6")

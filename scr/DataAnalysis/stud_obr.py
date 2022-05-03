import math

from scipy.stats import t


def f(n, a, x_, u0, s):
    view = (x_-u0)/(s/math.sqrt(n))
    print(f"t крит: {t.ppf(n-1, 1-a) * 100} t наб:{view}")


f(n=16, a=0.01, x_=42, u0=40, s=3.5)  # 4
f(n=10, a=0.05, x_=135, u0=120, s=20)  # 5
f(n=30, a=0.05, x_=18.9, u0=18.2, s=2.18)  # 6

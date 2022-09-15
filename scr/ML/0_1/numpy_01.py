import io

import matplotlib.pyplot as plt
import numpy as np

print("Задание 1")
v = np.array([[i for i in range(j * 1, j * 11, j)] for j in range(1, 11)])

print(v, "\n")

print("Задание 2")


def f(el1, n, d):
    return np.diag([i for i in range(el1, n, d)])


print(f(1, 30, 3), "\n")

print("Задание 3")
f = io.FileIO("0_1/stockholm_td_adj.dat")

data = np.genfromtxt(f)

fig, ax = plt.subplots(figsize=(14, 4))
x = np.linspace(1, 32, 31)
y = np.array([data[i, 5] for i in range(data.shape[0]) if (data[i, 0] == 1970) * (data[i, 1] == 10)])
ax.plot(x, y)
ax.axis('tight')
ax.set_title('temperatures in Stockholm')
ax.set_xlabel('days')
ax.set_ylabel('temperature (C)')

fig.show()

np.savetxt("0_1/oct70.txt", y)
np.savetxt("0_1/oct70.bin", y)

print(np.genfromtxt(io.FileIO("0_1/oct70.txt")))
print(np.genfromtxt(io.FileIO("0_1/oct70.bin")), "\n")

print("Задание 4")
print(np.array([[n + m * 10 for n in range(5)] for m in range(5)])[::, 1::2], "\n")

print("Задание 5")
print(v[v % 3 == 0], "\n")

print("Задание 7")
v = v.reshape((1, len(v) ** 2))
odd = v.copy()
even = v.copy()
odd[v % 2 == 0] = 0
even[v % 2 == 1] = 0
mask = v % 2
print(odd, "\n", even, "\n")
print(np.choose(mask, [even, odd]).reshape((10, 10)), "\n")

print("Задание 8")

vec1 = np.array([0, 1, 2, 3, 4])
vec2 = np.array([5, 6, 7, 8, 9])

print(np.rad2deg(np.arccos(vec1.dot(vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2)))))

print("Задание 9")

A = np.array([i for i in range(1, 26)]).reshape((5, 5))
B = [[i for i in range(j+1, j+6)] for j in range(0, 5)]

B.reverse()
B = np.array(B)

A[A % 2 == 0] = 0
A[A % 2 == 1] = 5
B[B < 5] = 0
B[B > 5] = 5

print("A det: " + str(np.linalg.det(A)))
print("B det: " + str(np.linalg.det(B)))

print("Обратную матрицу A найти нельзя, детерминант = 0")
print(np.linalg.inv(B))

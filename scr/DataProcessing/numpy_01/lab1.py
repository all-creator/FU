import numpy as np

A = np.array(np.loadtxt("minutes_n_ingredients.csv", skiprows=1, dtype="int32", delimiter=","))


def __1():
    print(A[:5:])


def __2():
    print(
        f'Медиана: {np.median(A[:, 1])}, Сред. Знач: {np.average(A[:, 1])}, Мин: {np.min(A[:, 1])}, Макс: {np.max(A[:, 1])}')
    print(
        f'Медиана: {np.median(A[:, 2])}, Сред. Знач: {np.average(A[:, 2])}, Мин: {np.min(A[:, 2])}, Макс: {np.max(A[:, 2])}')


def __3():
    v = np.quantile(A[:, 1:2], 0.75)
    print(A[A[:, 1] <= v].shape)


def __4():
    print(A.shape[0] - np.count_nonzero(A[:, 1]))
    np.place(A[:, 1], A[:, 1] == 0, 1)


def __5():
    print(np.unique(A[:, (1, 2)], axis=0).size)


def __6():
    print(np.unique(A[:, 2]).size)
    print(np.unique(A[:, 2]))


def __7():
    print(A[A[:, 2] <= 5].shape)


def __8():
    np.place(A[:, 1], A[:, 1] == 0, 1)
    av = A[:, 2] / A[:, 1]
    print(av, np.max(av))


def __9():
    mask = np.argsort(A[:, 1])[-100:]
    print(A[mask][:, 2].mean())


def __10():
    print(A[np.random.randint(A.shape[0], size=10), :])


def __11():
    mask = A[:, 2] < np.mean(A[:, 2])
    print(100 * len(A[mask]) / len(A))


def __12():
    mask = (A[:, 1] <= 20) & (A[:, 2] <= 5)
    return np.c_[A, mask]


def __13():
    print(__12())
    print((np.count_nonzero(__12()[:, 3]) / __12()[:, 3].shape[0]) * 100)


def __14():
    short = A[A[:, 1] < 10]
    stand = A[(A[:, 1] >= 10) & (A[:, 1] < 20)]
    long = A[20 <= A[:, 1]]
    maxr = np.min([short.shape[0], stand.shape[0], long.shape[0]])
    res = np.array([short[:maxr], stand[:maxr], long[:maxr]])
    print(res)
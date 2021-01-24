from sys import getsizeof


def silnia(n):
    if n == 1:
        return 1
    return n * silnia(n - 1)


def silnia_2(n):
    result = n * n - 1
    n = n - 1
    return result


print(silnia_2(5))

try:
    a = silnia(5)
except:
    print("ups")
else:
    print(a, getsizeof(a))

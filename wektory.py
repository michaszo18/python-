import math as m

a = [0, 2, -1]
b = [2, -1, 1]
c = [1, 3, 0]


def iloczyn_skalarny(a, b):
    wynik = 0
    for i in range(len(a)):
        wynik += a[i] * b[i]
    return wynik


def dlugosc_wektora(a):
    wynik = 0
    for i in a:
        wynik += m.pow(i, 2)
    return m.sqrt(wynik)


def kat_pmiedzy_wektorami(a, b):
    licznik = iloczyn_skalarny(a, b)
    mianownik = dlugosc_wektora(a) * dlugosc_wektora(b)
    return licznik / mianownik


def suma_wektorow(a, b):
    wynik = [0, 0, 0]
    for i in range(len(a)):
        wynik[i] = a[i] + b[i]
    return wynik


def roznica_wektorow(a, b):
    wynik = [0, 0, 0]
    for i in range(len(a)):
        wynik[i] = a[i] - b[i]
    return wynik


def mnozenie_przez_liczbe(wektor, liczba):
    wynik = [0, 0, 0]
    for i in range(len(wektor)):
        wynik[i] = wektor[i] * liczba
    return wynik


def iloczyn_wektorowy(a, b):
    """
    a[0], a[1], a[2]
    b[0], b[1], b[2]
    """
    return [
        (a[1] * b[2] - b[1] * a[2]),
        -1 * (a[0] * b[2] - b[0] * a[2]),
        (a[0] * b[1]) - (b[0] * a[1]),
    ]


print(f"suma: {suma_wektorow(a, b)}")
print(f"roznica: {roznica_wektorow(a, b)}")
print(f"mnozenie_przez_liczbe: {mnozenie_przez_liczbe(b, 6)}")
print(f"iloczyn wektorowy: {iloczyn_wektorowy(a, b)}")
print(f"iloczyn wektorowy: {iloczyn_wektorowy(b, a)}")
print(f"1.2.a: {iloczyn_skalarny(a, b)}")
print(f"1.2.b: {dlugosc_wektora(c)}")
print(f"1.2.c: {kat_pmiedzy_wektorami(b, c)}")
print(f"1.2.d: {roznica_wektorow(suma_wektorow(a, b), c)}")
print(
    f"1.2.e: {roznica_wektorow(mnozenie_przez_liczbe(b, iloczyn_skalarny(a, c)), mnozenie_przez_liczbe(c, iloczyn_skalarny(a, b)))}")
print(f"1.2.f: {iloczyn_wektorowy(a, b)}")
print(f"1.2.g.1: {iloczyn_skalarny(iloczyn_wektorowy(b, c),a)}")
print(f"1.2.g.2: {iloczyn_skalarny(iloczyn_wektorowy(a, b),c)}")
print(f"1.2.i: {iloczyn_skalarny(a,iloczyn_wektorowy(b,a))}")


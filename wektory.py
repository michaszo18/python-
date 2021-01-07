import math as m

a = [0, 2, -1]
b = [2, -1, 1]
c = [1, 3, 0]


def iloczyn_skalarny(a, b):
    wynik = 0
    for i in range(3):
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
    return licznik/mianownik


def suma_wektorow(a, b):
    wynik = [0,0,0]
    for i in range(len(a)):
        wynik[i] = a[i] + b[i]
    return wynik


def roznica_wektorow(a, b):
    wynik = [0,0,0]
    for i in range(len(a)):
        wynik[i] = a[i] - b[i]
    return wynik


print(f"suma: {suma_wektorow(a, b)}")
print(f"roznica: {roznica_wektorow(a, b)}")
print(f"1.2.a: {iloczyn_skalarny(a, b)}")
print(f"1.2.b: {dlugosc_wektora(c)}")
print(f"1.2.c: {kat_pmiedzy_wektorami(b,c)}")
print(f"1.2.d: {roznica_wektorow(suma_wektorow(a,b), c)}")

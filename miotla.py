import matplotlib.pyplot as plt


# TODO: If odcinki się przecinają
#     return Punkty w których się przecinają
# TODO: If odcinki na siebie nachodzą
#     return punkt początowy częsci wspólnej and punkt końcowy
# TODO: Else
#     return null


# http://matma4u.pl/topic/44302-program-w-c-kt%C3%B3ry-ma-wykry%C4%87-przeci%C4%99cie-si%C4%99-dw%C3%B3ch-odcink%C3%B3w-na-p%C5%82aszczy%C5%BAnie/
def min(x1, x2):
    return x1 if x1 <= x2 else x2


def max(x1, x2):
    return x1 if x1 >= x2 else x2


# https://www.obliczeniowo.com.pl/62
def iloczyn(p1, p2, p3):
    return (p2 - p1) * (p3 - p1) - (p3 - p1) * (p2 - p1)


def lezy_miedzy(p1, p2, p3):
    if min(p1, p2) == max(p1, p2):
        return True
    else:
        return False


def przecinaja_sie(p1, p2, p3, p4):
    s1 = iloczyn(p1, p2, p3)
    s2 = iloczyn(p1, p4, p2)
    s3 = iloczyn(p3, p1, p4)
    s4 = iloczyn(p3, p2, p4)

    if ((s1 > 0 and s2 < 0) or (s1 < 0 and s2 > 0)) and ((s3 < 0 and s4 > 0) or (s3 > 0 and s4 < 0)):
        return True
    elif s1 == 0 and lezy_miedzy(p1, p2, p3):
        return True
    elif s2 == 0 and lezy_miedzy(p1, p2, p4):
        return True
    elif s3 == 0 and lezy_miedzy(p3, p4, p1):
        return True
    elif s4 == 0 and lezy_miedzy(p3, p4, p2):
        return True
    else:
        return False


a1 = 11
a2 = 22
b1 = 1
b2 = 2

print(przecinaja_sie(a1, a2, b1, b2))

data = [(a1, a2), (b1, b2)]

# Wyświetl dane
plt.plot(data[0])
plt.plot(data[1])

plt.show()

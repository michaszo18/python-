import random

try:
    ileLiczb = int(input("Podaj ilość liczb, które chcesz zgadanąć:"))
    maxLiczba = int(input("Podaj maksymalną liczbę do zgadnięcia:"))
    if ileLiczb > maxLiczba:
        print("Nie można wylosować x unikalnych liczb z liczby x-1")
        exit()
except ValueError:
    print("Błędne dane!")
    exit()

# Najczęściej używamy symboli:
#  %s – wartość zostaje zamieniona na napis przez funkcję str();
#  %d – wartość ma być dziesiętną liczbą całkowitą;
#  %f – oczekujemy liczby zmiennoprzecinkowej.
print("Chcesz zgadywać: %s z zakresu (0,%s)" % (ileLiczb, maxLiczba))

liczby = []

i = 0
while i < ileLiczb:
    liczba = random.randint(0, maxLiczba)
    if liczby.count(liczba) == 0:
        liczby.append(liczba)
        i += 1

# print(liczby)
for i in range(3):
    print("**************************")
    print("Próba numer: ", i+1)
    typy = set()
    i = 0
    while i < ileLiczb:
        typ = int(input("Podaj liczbę numer: %s : " % (i + 1)))

        if typ in typy:
            print("Podałeś już liczbę: %d" %(typ))
        if typ not in typy:
            typy.add(typ)
            i = i + 1
    print(typy)

    trafione = set(liczby) & typy
    if trafione:
        print("\nIlość trafień: %s" %(len(trafione)))
        print("Trafione liczby to:", trafione)
    else:
        print("Brak trafionych liczb")

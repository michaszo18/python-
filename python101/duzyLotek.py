import random

ileLiczb = int(input("Podaj ilość liczb, które chcesz zgadanąć:"))
maxLiczba = int(input("Podaj maksymalną liczbę do zgadnięcia:"))

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

print(liczby)
import random

punkty = 0

ang = ['significant', 'native', 'clean up', 'I must talk to him about it', 'obvious as']

pol = ['znaczący', 'ojczysty', 'sprzątać', 'Musze z nim o tym porozmawiać', 'oczywiste jak']

# Losowanie numeru zadania
dlugoscTablicy = len(ang)-1
liczby = []
i = 0
while i < 3:
    liczba = random.randint(0, dlugoscTablicy)
    if liczby.count(liczba) == 0:
        liczby.append(liczba)
        i += 1

for i in liczby:
    print("Zdanie numer %s, zdobytych punktów %s/3" %(i+1, punkty))
    odp = input("%s:" %(pol[i]))
    if odp == ang[i]:
        print("+1 punkt")
        punkty += 1
    else:
        print("-1 punkt")
        punkty -= 1

print("Suma uzyskanych punktów: ", punkty)
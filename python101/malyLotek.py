import random

liczba = random.randint(1,10)
wygrana = 0

for i in range(3):
    print('Próba numer: ', i+1)
    odp = input('O jakiej liczbie myślisz: ')
    if liczba == int(odp):
        wygrana = 1
        break
    else:
        print('Nie zgadłeś')
        if int(odp) < liczba:
            print('Podana liczba jest za mała')
        else:
            print('Podana liczba jest za duża')
    print()

if wygrana ==1:
    print('Zgadłeś, miałem na myśli: ', liczba)
else:
    print('Przegrałes miałem na myśli:', liczba)
from copy import copy

# Inmutable - po zmianie zmienia się również miejsce w pamięci
i = 1
print("i: ", i, id(i))

i = "Hej"
print("i: ", i, id(i))

# Mutable - przy edycji adres w pamięci pozostaje niezmienny
i = [1, 2, 3]
print("i: ", i, id(i))
i.append(4)
print("i: ", i, id(i))

days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
workdays = copy(days)
workdays.remove('sat')
workdays.remove('sun')

print("days: ", days, id(days))
print("workdays: ", workdays, id(workdays))


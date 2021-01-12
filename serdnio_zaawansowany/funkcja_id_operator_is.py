a = "hello world"
b = a
print(a is b)
print(a == b)
print(id(a), id(b))
b += "!"
print(a is b)
print(a == b)
print(id(a), id(b))
b = b[:-1]
print(a is b)
print(a == b)
print(id(a), id(b))

a = 1
b = a
print(a is b)
print(a == b)
print(id(a), id(b))
b += 1
print(a is b)
print(a == b)
print(id(a), id(b))
b -= 1
print(a is b)
print(a == b)
print(id(a), id(b))

# Wniosek - int w pythonie przehowowany są pod tym samym adresem (optymalizator pythona), a string po zmianie


# Zadanie
print("\n\n#################################\n\n")
a = b = c = 10
print(a, id(a))
print(b, id(b))
print(c, id(c))
a = 20
print(a, id(a))
print(b, id(b))
print(c, id(c))

print("\n\n#################################\n\n")
a = b = c = [1, 2, 3]
print(a, id(a))
print(b, id(b))
print(c, id(c))
a.append(4)
print(a, id(a))
print(b, id(b))
print(c, id(c))

"""
W pierwszym przykładzie a, b, c były wskaźnikami do komórki pamięci, w której była zapisana liczba, czyli końcowa wartość.
W drugim przykładzie a, b, c to wskaźnik do komórki pamięci, w której jest lista. Lista jest wskaźnikiem do elementów tej listy. 
Kiedy dodajesz nowy element do listy, nie modyfikujesz podstawowej komórki pamięci z listą, dlatego id się nie zmienił.
"""

print("\n\n#################################\n\n")
x = 10
y = 10
print(x, id(x))
print(y, id(y))
y = y + 1234567890 - 1234567890
print(x, id(x))
print(y, id(y))
list_a = list(range(6))
list_b = list_a.copy()

product = [(a, b) for a in list_a for b in list_b]
print(product)

a = [a for a in list_a if a > 2]
print(a)

product_2 = {a: b for a in list_a for b in list_b}
print(product_2)

ties = ['green tie', 'gray tie', 'red tie']
shirts = ['white shirt', 'blue shirt', 'green shirt']

print([f"noszę {tie} krawat z {shirt} koszulą." for tie in ties for shirt in shirts])

clients = ['A-company', 'B-company']
projects = [300, 400, 1500, 2340, 50]

investments = [(c, p) for c in clients for p in projects if
               c == 'A-company' and p < 1000 or c == 'B-company' and p >= 1000]
print(investments)

print("\n\n#########################\n\n")

ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

flights = [(a, b) for a in ports for b in ports if a != b and (a, b)]
print(flights)
print(len(flights))

routes = [(start, stop) for start in ports for stop in ports if start < stop]
print(routes)
print(len(routes))

abc = ['a', 'b', 'c', 'd', 'e', 'f']
alphabet = [(start, stop) for start in abc for stop in abc if start < stop]
print(alphabet)

print("\n\n#########################\n\n")
generator = ((start, stop) for start in abc for stop in abc if start < stop)
print(generator)
# sprawdzi się tam gdzie będzie dużo danych do przetworzenia
# print(next(generator))
# print(next(generator))
# print(next(generator))

for x in generator:
    print(x)

generator = ((start, stop) for start in abc for stop in abc if start < stop)

while True:
    try:
        print(next(generator))
    except StopIteration:
        print('all values have been generated')
        break
    else:
        print("ło a co tu się...")

ports_gen = ((start, stop) for start in ports for stop in ports if start > stop)

for x in ports_gen:
    print(x)

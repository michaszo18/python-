arr = [1, "string", 10.5, 43.111111111111111111, False]

for i in arr:
    print(type(i))


def get_count(input_str):
    return sum(1 for letters in input_str if letters in 'ąężóźńłć')


# CASTOWANIE
x3 = int(float("1.1"))

# Zwróci str zaczynając go z wielkiej litery
print("michał".title())

printable = f"""
{x3} 
format
"""

text = f"Siema {printable} joł"

print(text)


def greetings(x, y):
    return f"Witaj, {x.title()} {y.title()}"


print(greetings("mike", "szo"))

# Do robienia choinki - wycenruje mike na 25 polach
print("mike".center(25))
print("*".center(25))
print("***".center(25))

print(sum(1 for letter in "Siema tu pythona" if letter is 'a'))

str = """Przykładowo czasami część kodu muszę wyłączyć na pewien czas z "obiegu"
i stąd głównie moje pytanie. Może więc lepsze było by określenie
"remowanie" kodu :) Ale faktycznie widziałem ten sposób komentowania w
źródłach ale jakoś nie skojarzyłem :) W każdym razie każde dodatkowe
uwagi pythonowych kombatantów są zawsze mile widziane :)"""

print(str.find("pytanie"))

if "pytanie" in str:
    print("ok")

print(str.isascii())
print(str.isdigit())
print(str.istitle())
print("Michał".istitle())

a: int = 10
print(type(a))
b: str = "Mike"
print(type(a))

if a > b:
    print(a)

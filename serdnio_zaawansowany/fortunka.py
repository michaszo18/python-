from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


day = input("Podaj datę przydatności do spożycia z etykiety - dzień: ")
month = input("Podaj datę przydatności do spożycia z etykiety - miesiąc: ")
year = input("Podaj datę przydatności do spożycia z etykiety - rok: ")


expiration_date = datetime.strptime(f"{year}-{month}-{day}", '%Y-%m-%d')
production_date = expiration_date - relativedelta(months=+36)
how_old = datetime.now() - production_date
print(f"Data produkcji: {str(production_date).split(' ')[0]}")
print(f"Twój komes ma: {str(how_old).split(',')[0]}")


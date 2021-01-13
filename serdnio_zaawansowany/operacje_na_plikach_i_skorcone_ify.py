import os


def words_counter(path):
    try:
        f = open(path, "r")
        return len(f.read().split())
    except:
        print("Nie ma takiego pliku")
        return False


def words_counter_2(path):
    return os.path.isfile(path) and len(open(path, "r").read().split())


path = r'C:\Users\Mike\Desktop\my_data.txt'

print(words_counter(path))
print(words_counter_2(path))

# os.remove(path)

# alternatywa - sprawdź czy plik istnieje (false) - tworzy plik, true - leci dalej
# result = os.path.isfile(path) or open(path, 'x', encoding='UTF-8')
# result.write("Widzę ciemność")

price = 123
bonus = 23
bonus_granted = True

if bonus_granted:
    price -= bonus

print(price)

price = price - bonus if bonus_granted else price

print(price)

rating = -523542

if rating == 5:
    print('very good')
elif rating == 4:
    print('good')
else:
    print('weak')

print('very good') if rating == 5 else print('good') if rating == 4 else print('week')

import datetime as dt

today_weekday = dt.date.today().strftime("%A")

print(today_weekday)

if today_weekday == 'Monday':
    print("I'm helping my mum")
elif today_weekday == 'Tuesday' or today_weekday == 'Wednesday':
    print("You are doing laundry")
elif today_weekday == 'Thursday':
    print("I'm on duty")
elif today_weekday == 'Friday':
    print("I have two meetings")
elif today_weekday == 'Saturday':
    print("You have lessons")
else:
    print("SUNDAY WILL BE FOR US")

print("I'm helping my mum" if today_weekday == 'Monday' else
      "You are doing laundry" if today_weekday == 'Tuesday' or today_weekday == 'Wednesday' else
      "I'm on duty" if today_weekday == 'Thursday' else
      "I have two meetings" if today_weekday == 'Friday' else
      "You have lessons" if today_weekday == 'Saturday' else
      "SUNDAY WILL BE FOR US")

week = {
    'Monday': "I'm helping my mum",
    'Tuesday': "You are doing laundry",
    'Wednesday': "You are doing laundry",
}

print(week[today_weekday])

print("\n\n###################\n\n")

colors = ["red", "orange", "green", "violet", "blue", "yellow"]

def get_colors_palette(list, number):
    return list[:number]


colors2 = get_colors_palette(colors, 3)
print(colors, colors2, colors is colors2)

for i in range(1,len(colors)+1):
    print(get_colors_palette(colors, i))
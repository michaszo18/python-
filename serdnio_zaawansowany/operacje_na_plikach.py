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

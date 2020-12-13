import json


def sort_by_letter_count(e):
    return len(e)


arr = ['apple', 'banana', 'kiwi', 'pear', 'orange']
# arr.append('cherry')
# arr.append('watermelon')

arr.insert(3, 'lemon')

arr.sort(key=sort_by_letter_count)

# for i in range(0, arr.__len__()):
#     print(f"{i}: {arr[i]}, letters:{len(arr[i])}")

# print("Max: " + max(arr))


europe = {'spain': 'madrid', 'france': 'paris', 'germany': 'berlin', 'norway': 'oslo'}

# europe.clear()
# europe2 = europe.copy()

print(europe.get('france'))
print('spain' in europe)

print(europe.items())
print(europe.keys())
print(europe.values())
print(str(europe))

json_object = json.dumps(europe)
print(json_object)

europe_without_values = ('poland', 'uk')

europe_without_values = dict.fromkeys(europe_without_values, None)


# łączenie słowników
europe2 = europe.copy()
europe2.update(europe_without_values)

print(europe2.setdefault('czech', 'Throw not found'))

for country, capital in europe2.items():
    print(f"{country}: {capital}")

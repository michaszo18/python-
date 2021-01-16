work_days = [19, 21, 22, 21, 20, 22]
print(work_days)

enumerated_days = enumerate(work_days)
print(enumerated_days)

# tuple
enumerated_days = list(enumerated_days)
print(enumerated_days)

for i, j in enumerated_days:
    print(f"Position:{i} - value:{j}")

months = ['st', 'lu', 'mar', 'kw', 'maj', 'cz']
months_days = list(zip(months, work_days))
print(months_days)

for month, days in months_days:
    print(f"Month {month} - {days} days")

projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']
dates = ['2016-06-23', '2016-08-29', '1994-01-01']

for project, leader, date in zip(projects, leaders, dates):
    print(f"The leader of {project} started {date} is {leader}")

print("\n\n##########\n\n")

banknotes_coins = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50, 100, 200, 500]

dict_denominations = dict(zip(banknotes_coins, len(banknotes_coins) * [0]))


dict_denominations[100] += 1
dict_denominations[20] += 1
dict_denominations[5] += 1
dict_denominations[0.5] += 1

dict_denominations[50] += 1
dict_denominations[20] += 2
dict_denominations[5] += 1
dict_denominations[2] += 2

dict_denominations[100] += 1
dict_denominations[50] += 1
dict_denominations[2] += 1

for k in sorted(dict_denominations.keys()):
    print("Denominate: {0:6.2f} - amount {1:5}".format(k, dict_denominations[k]))

isOk = True
print(isOk, type(isOk), id(isOk))

isSpoko = "False"
print(isSpoko, type(isSpoko), id(isSpoko))

if isSpoko is bool and isSpoko == True:
    print("True")

# w pythonie wszystkie niepuste string, niepuste lisy są traktowane jako true

print("\n\n###################\n\n")


def display_options(options):
    for i in range(len(options)):
        print(f"{i + 1}: {options[i]}")

    choice = input('Select option above or press enter to exit: ')
    return choice


choice = 'x'
options = ['load data', 'export data', 'analyze & predict']

while True:
    choice = display_options(options)

    if choice:
        if choice.isnumeric():
            choice = int(choice) - 1
            if choice in [0, 1, 2]:
                print(options[choice])
                exit()
            else:
                print("This is valid number.")
        else:
            print("This is not a number.")
    else:
        print("Goodbye")
        exit()

import random

file = open("czas.txt")

numb = random.randint(0,131)


print(numb)
points = 0

for x in file:
    words = x.split(',')
    # print(words[0])
    if int(words[0]) == numb:
        print(x)
        # print("polish:", words[4])
        # print("infinitive:", words[1])
        infinitive = input("infinitive:")
        tense = input("tense:")
        participle = input("participle:")
        pol = input("pol:")
        if infinitive == words[1] and tense == words[2] and participle == words[3]:
            points += 1
        else:
            points -= 1

        print(points)

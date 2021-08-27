import re

FILE = 'C:/Users/ciotuja1/PycharmProjects/pythonProject/dane.txt'


baza = []
with open(FILE) as file:
    for line in file.readlines():
        # print(line)

        role, id, group, user, size, month, day, year, path = line.split(':')

        baza.append(role)
        baza.append(id)
        baza.append(group)
        baza.append(user)
        baza.append(size)
        baza.append(user)
        baza.append(month)
        baza.append(day)
        baza.append(year)
        baza.append(path)
        print(baza)
        # print(baza[9])




        if len(baza) > 0:
        baza.append(role, id, group, user, size, month, day, year, path)

# print(baza[23])
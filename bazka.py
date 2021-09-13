import sqlite3
import re

FILE = 'C:/Users/ciotuja1/PycharmProjects/pythonProject/dane2.txt'

for line in open(FILE):

    for match in re.finditer(re.compile("Name"), line):

        name = line.strip(':').split()
        # print(name[2])
        idx = name.index(':')
        print(name[idx+1])

    for match in re.finditer(re.compile("Type"), line):

        typ = line.strip('\t').split().pop(2).strip(' ')
        print(typ)

    for match in re.finditer(re.compile("Chassis Topology"), line):

        chassis = line.strip('\t').strip(' ').split()
        idx = chassis.index(':')
        print(chassis[idx + 1])
        # print(chassis)

    for match in re.finditer(re.compile("Location"), line):

        # print(line.strip('  \n'))

        location = line.strip(':').split()
        # print(location[2])
        idx = location.index(':')
        # print(location[idx + 1])

    for match in re.finditer(re.compile("                               "), line):
        typ = line.strip('\n').split()
        adres = location + typ
        idx2 = adres.index(':')
        adres3 = adres[idx2+1:]
        for i in range(len(adres3)):
            print(adres3[i], end=' ')


    for match in re.finditer(re.compile("Coordinates"), line):
        coor = line.strip('\t').split()
        idx = coor.index(':')
        print('\n')
        coor2 = coor[idx+1:]
        print(coor2)

    # for match in re.finditer(re.compile("CLLI code"), line):
    #     type = line.strip('\t').split().pop(2)
    #     print(type)

    # for match in re.finditer(re.compile("Number of slots"), line):
    #     type = line.strip('\t').split().pop(2)
    #     print(type)
    #
    # for match in re.finditer(re.compile("Oper number of slots"), line):
    #     type = line.strip('\t').split().pop(2)
    #     print(type)
    #
    # for match in re.finditer(re.compile("faceplate ports"), line):
    #     type = line.strip('\t').split().pop(2)
    #     print(type)
    #
    # for match in re.finditer(re.compile("physical ports"), line):
    #     type = line.strip('\t').split().pop(2)
    #     print(type)
    #
    # for match in re.finditer(re.compile("Critical LED"), line):
    #     type = line.strip('\t').split().pop(2)
    #     print(type)
    #
    # for match in re.finditer(re.compile("Major LED"), line):
    #     type = line.strip('\t').split().pop(2)
    #     print(type)
    #
    # for match in re.finditer(re.compile("Minor LED"), line):
    #     type = line.strip('\t').split().pop(2)
    #     print(type)
    #
    # for match in re.finditer(re.compile("Over Temperature"), line):
    #     type = line.strip('\t').split().pop(2)
    #     print(type)
    #
    # for match in re.finditer(re.compile("Base MAC address"), line):
    #     type = line.strip('\t').split().pop(2)
    #     print(type)

# con = sqlite3.connect('machines.db')
# cur = con.cursor()
# con.execute("""CREATE TABLE chassis
#                             (name VARCHAR,
#                             type VARCHAR,
#                             chassis_topology VARCHAR,
#                             location VARCHAR,
#                             coordinates VARCHAR,
#                             cli INT,
#                             slots INT,
#                             faceplate_slots INT,
#                             physical_ports INT,
#                             critical_led_state VARCHAR,
#                             major_led_state VARCHAR,
#                             minor_led_state VARACHAR,
#                             over_temperatur_state VARCHAR,
#                             base_mac_address VARCHAR)""")

# for row in cur.execute('SELECT * FROM machines ORDER BY id'):
#         print(row)
# con.commit()

# with open(FILE) as file:
#     for line in file.readlines():
#         role, id, group, user, size, month, day, year, path = line.split(':')
#         cur.execute("INSERT INTO machines (role, id, 'group', user, size, month, day, year, path)"
#                     " VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (role, id, group, user, size, month, day, year, str(path).strip()))

# # for i in range(len(baza)):
#     cur.execute("INSERT INTO machines (role, id, 'group', user, size, month, day, year, path)"
#                 " VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", ((baza[i]), (baza[i]), (baza[i]), (baza[i]), (baza[i]),
#                                                                                        (baza[i]),
#                                                                                        (baza[i]),
#                                                                                         (baza[i]),
#                                                                                         (baza[i])))
# con.commit()
# con.close()
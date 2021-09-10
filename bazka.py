import sqlite3
import re

FILE = 'C:/Users/ciotuja1/PycharmProjects/pythonProject/dane2.txt'

for line in open(FILE):

    for match in re.finditer(re.compile("Name"), line):

        print(line.strip())

    for match in re.finditer(re.compile("Type"), line):

        print(line)

    for match in re.finditer(re.compile("Chassis Topology"), line):

        print(line)

    for match in re.finditer(re.compile("Location"), line):

        print(line.strip())

    for match in re.finditer(re.compile("                           "), line):

        print(line.rstrip())

    for match in re.finditer(re.compile("Coordinates"), line):

        print(line)

    for match in re.finditer(re.compile("CLLI code"), line):

        print(line)

    for match in re.finditer(re.compile("Number of slots"), line):

        print(line)

    for match in re.finditer(re.compile("Oper number of slots"), line):

        print(line)

    for match in re.finditer(re.compile("faceplate ports"), line):

        print(line)

    for match in re.finditer(re.compile("physical ports"), line):

        print(line)

    for match in re.finditer(re.compile("Critical LED"), line):

        print(line)

    for match in re.finditer(re.compile("Major LED"), line):

        print(line)

    for match in re.finditer(re.compile("Minor LED"), line):

        print(line)

    for match in re.finditer(re.compile("Over Temperature"), line):

        print(line)

    for match in re.finditer(re.compile("Base MAC address"), line):

        print(line)

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
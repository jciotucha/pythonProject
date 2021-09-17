import sqlite3
import re

FILE = 'C:/Users/ciotuja1/PycharmProjects/pythonProject/dane2.txt'

for line in open(FILE):

    for match in re.finditer(re.compile("Name"), line):
        zm = line.strip(':').split()
        idx = zm.index(':')
        name1 = (zm[idx + 1])
        print(name1)

    for match in re.finditer(re.compile("Type"), line):
        zm = line.strip(':').split()
        idx = zm.index(':')
        type1 = (zm[idx + 1])
        print(type1)

    for match in re.finditer(re.compile("Chassis Topology"), line):
        zm = line.strip(':').split()
        idx = zm.index(':')
        chassis_topology1 = (zm[idx + 1])
        print(chassis_topology1)

    for match in re.finditer(re.compile("Location"), line):
        location = line.strip(':').split()
        idx = location.index(':')

    for match in re.finditer(re.compile("                               "), line):
        typ = line.strip('\n').split()
        adres = location + typ
        idx2 = adres.index(':')
        adres3 = adres[idx2 + 1:]
        new = ''

        for i in range(len(adres3)):
            new = new + ' ' + str(adres3[i])

        location1 = (new.rstrip('\n'))
        print(location1)

    for match in re.finditer(re.compile("Coordinates"), line):
        idx43 = line.index(':')
        coordinates1 = (line[idx43 + 1:].strip(' '))
        print(coordinates1)

    for match in re.finditer(re.compile("CLLI code"), line):
        zm = line.strip(':').split()
        idx3 = zm.index(':')

        if len(zm) > 3:
            print(idx3)
            cli1 = (zm[idx3 + 1].strip(' '))
            print(cli1)
        else:
            cli1 = ''
            print('else')

    for match in re.finditer(re.compile("Number of slots"), line):
        idx4 = line.index(':')
        slots1 = (line[idx4 + 1:].strip(' '))
        print(slots1)

    for match in re.finditer(re.compile("Oper number of slots"), line):
        idx5 = line.index(':')
        number_of_slots1 = (line[idx5 + 1:].strip(' '))
        print(number_of_slots1)

    for match in re.finditer(re.compile("faceplate ports"), line):
        idx6 = line.index(':')
        faceplate_slots1 = (line[idx6 + 1:].strip(' '))
        print(faceplate_slots1)

    for match in re.finditer(re.compile("physical ports"), line):
        idx7 = line.index(':')
        physical_ports1 = (line[idx7 + 1:].strip(' '))
        print(physical_ports1)

    for match in re.finditer(re.compile("Critical LED"), line):
        idx8 = line.index(':')
        critical_led_state1 = (line[idx8 + 1:].strip(' '))
        print(critical_led_state1)

    for match in re.finditer(re.compile("Major LED"), line):
        idx9 = line.index(':')
        major_led_state1 = (line[idx9 + 1:].strip(' '))
        print(major_led_state1)

    for match in re.finditer(re.compile("Minor LED"), line):
        idx10 = line.index(':')
        minor_led_state1 = (line[idx10 + 1:].strip(' '))
        print(minor_led_state1)

    for match in re.finditer(re.compile("Over Temperature"), line):
        idx11 = line.index(':')
        over_temperatur_state1 = (line[idx11 + 1:].strip(' '))
        print(over_temperatur_state1)

    for match in re.finditer(re.compile("Base MAC address"), line):
        idx12 = line.index(':')
        base_mac_address1 = (line[idx12 + 1:].strip(' '))
        print(base_mac_address1)

con = sqlite3.connect('machines.db')
cur = con.cursor()
# con.execute("""CREATE TABLE chassis
#                             (name VARCHAR,
#                             type VARCHAR,
#                             chassis_topology VARCHAR,
#                             location VARCHAR,
#                             coordinates VARCHAR,
#                             cli INT,
#                             slots INT,
#                             number_of_slots INT,
#                             faceplate_slots INT,
#                             physical_ports INT,
#                             critical_led_state VARCHAR,
#                             major_led_state VARCHAR,
#                             minor_led_state VARACHAR,
#                             over_temperatur_state VARCHAR,
#                             base_mac_address VARCHAR)""")

# for row in cur.execute('SELECT * FROM chassis'):
#         print(row)
# con.commit()

# with open(FILE) as file:
#     for line in file.readlines():
#         role, id, group, user, size, month, day, year, path = line.split(':')
# cur.execute("INSERT INTO chassis (name, type, chassis_topology, location, coordinates, cli, slots, number_of_slots,"
#             "faceplate_slots, physical_ports, critical_led_state, major_led_state, minor_led_state, "
#             "over_temperatur_state, base_mac_address) "
#             " VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
#             (name1, type1, chassis_topology1, location1, coordinates1, cli1, slots1, number_of_slots1,
#              faceplate_slots1, physical_ports1, critical_led_state1, major_led_state1, minor_led_state1,
#              over_temperatur_state1, base_mac_address1))

cur.execute("INSERT INTO chassis (name, type, chassis_topology, location, coordinates, cli, slots, number_of_slots,"
            "faceplate_slots, physical_ports, critical_led_state, major_led_state, minor_led_state, "
            "over_temperatur_state, base_mac_address) "
            " VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (name1.strip(), type1.strip(), chassis_topology1.strip(), location1.strip(), coordinates1.strip(), cli1.strip(), slots1.strip(), number_of_slots1.strip(), faceplate_slots1.strip(), physical_ports1.strip(), critical_led_state1.strip(), major_led_state1.strip(), minor_led_state1.strip(), over_temperatur_state1.strip(), base_mac_address1.strip()))

# # for i in range(len(baza)):
#     cur.execute("INSERT INTO machines (role, id, 'group', user, size, month, day, year, path)"
#                 " VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", ((baza[i]), (baza[i]), (baza[i]), (baza[i]), (baza[i]),
#                                                                                        (baza[i]),
#                                                                                        (baza[i]),
#                                                                                         (baza[i]),
#                                                                                         (baza[i])))
con.commit()
con.close()

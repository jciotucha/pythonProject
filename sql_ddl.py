# import sqlite3
#
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

# cur.execute("INSERT INTO chassis (name, type, chassis_topology, location, coordinates, cli, slots, number_of_slots,"
#             "faceplate_slots, physical_ports, critical_led_state, major_led_state, minor_led_state, "
#             "over_temperatur_state, base_mac_address) "
#             " VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
#             (name1.strip(), type1.strip(), chassis_topology1.strip(), location1.strip(), coordinates1.strip(), cli1.strip(), slots1.strip(), number_of_slots1.strip(), faceplate_slots1.strip(), physical_ports1.strip(), critical_led_state1.strip(), major_led_state1.strip(), minor_led_state1.strip(), over_temperatur_state1.strip(), base_mac_address1.strip()))

# # for i in range(len(baza)):
#     cur.execute("INSERT INTO machines (role, id, 'group', user, size, month, day, year, path)"
#                 " VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", ((baza[i]), (baza[i]), (baza[i]), (baza[i]), (baza[i]),
#                                                                                        (baza[i]),
#                                                                                        (baza[i]),
#                                                                                         (baza[i]),
#                                                                                         (baza[i])))
# con.commit()
# con.close()
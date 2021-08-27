import sqlite3

FILE = 'C:/Users/ciotuja1/PycharmProjects/pythonProject/dane.txt'
con = sqlite3.connect('machines.db')
cur = con.cursor()
# con.execute("""CREATE TABLE machines
#                             (role VARCHAR,
#                             id INT,
#                             'group' VARCHAR,
#                             user VARCHAR,
#                             size INT,
#                             month INT,
#                             day INT,
#                             year INT,
#                             path VARCHAR)""")

# for row in cur.execute('SELECT * FROM stocks ORDER BY price'):
#         print(row)
# con.commit()

with open(FILE) as file:
    for line in file.readlines():
        role, id, group, user, size, month, day, year, path = line.split(':')
        cur.execute("INSERT INTO machines (role, id, 'group', user, size, month, day, year, path)"
                    " VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (role, id, group, user, size, month, day, year, path))

# # for i in range(len(baza)):
#     cur.execute("INSERT INTO machines (role, id, 'group', user, size, month, day, year, path)"
#                 " VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", ((baza[i]), (baza[i]), (baza[i]), (baza[i]), (baza[i]),
#                                                                                        (baza[i]),
#                                                                                        (baza[i]),
#                                                                                         (baza[i]),
#                                                                                         (baza[i])))
con.commit()
con.close()

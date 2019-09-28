import sqlite3

CONN = sqlite3.connect('demo_data.sqlite3')
CURS = CONN.cursor()

s_x_y = {'s':['g', 'v', 'f'],
        'x':[3, 5, 8],
        'y':[9, 7, 7]}
CURS.execute('CREATE TABLE demo (s VARCHAR(1), x INT, y INT);')

CURS.execute("INSERT INTO demo VALUES('g', 3, 9);")
CURS.execute("INSERT INTO demo VALUES('v', 5, 7);")
CURS.execute("INSERT INTO demo VALUES('f', 8, 7);")

CONN.commit()

CURS.execute('SELECT COUNT(*) FROM demo;')
CURS.execute('SELECT COUNT(*) FROM demo WHERE x >= 5 AND y >= 5;')
CURS.execute('SELECT COUNT(DISTINCT(y)) FROM demo;')
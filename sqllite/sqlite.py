# Example of SQLite usage

import sqlite3

connection = sqlite3.connect(r'C:\dbs\test.db')

cur = connection.cursor()

#cur.execute('CREATE TABLE Table1 (Column1 varchar(20), Column2 varchar(20))')
cur.execute("INSERT INTO Table1 (Column1, Column2) VALUES ('test', 'test')")

rows = cur.execute("SELECT * FROM Table1")

for row in rows:
    print(row)

connection.commit()
connection.close()





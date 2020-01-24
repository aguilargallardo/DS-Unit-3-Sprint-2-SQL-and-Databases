import sqlite3

conn = sqlite3.connect('abuddymovesql.db')
curs = conn.cursor()

# curs.execute('CREATE TABLE buddymove(User Id TEXT, Sports INT, Religious INT, Nature INT, Theatre INT, Shopping INT, Picnic INT)')

# curs.execute("INSERT INTO buddymove VALUES('text', 1,2,3,4,5,6)")
# conn.commit()
# curs.close()
# conn.close()

import sqlalchemy

engine = sqlalchemy.create_engine('sqlite///')
engine.connect()
engine.table_names()
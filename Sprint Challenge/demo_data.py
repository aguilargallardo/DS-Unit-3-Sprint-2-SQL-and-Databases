import sqlite3

conn = sqlite3.connect('demo_data.sqlite3')

#cursor
cur = conn.cursor()

"""
PART 1 Making a populating a Database
"""


#dropping  existing table
cur.execute("DROP TABLE IF EXISTS demo")

#making table
cur.execute("""
CREATE TABLE demo
(s SERIAL PRIMARY KEY,
x INT,
y INT);
""")

#inserting data
#execute method
def execute_query(query):
    cur.execute(query)
    results = cur.fetchall()
    print(results)

execute_query("""INSERT INTO demo VALUES
('g',3,9);""")


execute_query("""INSERT INTO demo VALUES
('v',5,7),('f',8,7);""")


execute_query("""SELECT * FROM demo;""")





#commit it
conn.commit()

#close the cursor
cur.close()
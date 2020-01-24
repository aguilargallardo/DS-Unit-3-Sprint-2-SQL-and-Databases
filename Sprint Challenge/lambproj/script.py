import psycopg2 

#connect to the db
conn = psycopg2.connect(
    host = "rajje.db.elephantsql.com",
    database = "bfgfslgk",
    user = "bfgfslgk",
    password = "Ld0Us0EULJPGGQxTWY7W6gq_tfgEU1MI"
)

#cursor
cur = conn.cursor()

cur.execute("INSERT INTO employees (id, name) VALUES (%s, %s)", (3, "Baniel") )
#execute query 
cur.execute("SELECT id, name FROM employees")

rows = cur.fetchall()

for r in rows:
    print (f"id {r[0]} name {r[1]}")

#commit it
conn.commit()

#close the cursor
cur.close()
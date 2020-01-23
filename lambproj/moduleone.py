import sqlite3

conn = sqlite3.connect('rpg_db.sqlite3')

#cursor
cur = conn.cursor()

#execute method
def execute_query(query):
    cur.execute(query)
    results = cur.fetchall()
    print(results)

print("How many charcters are there?")
x = execute_query("SELECT count(character_id) FROM charactercreator_character")
print(x)

print("How many of each specific subclass?")
a = execute_query("SELECT count(*) character_id FROM charactercreator_cleric")
b = execute_query("SELECT count(*) character_id FROM charactercreator_fighter")
c = execute_query("SELECT count(*) character_id FROM charactercreator_mage")
d = execute_query("SELECT count(*) character_id FROM charactercreator_thief")
print(a,b,c,d)

# print("How many total Items?")
# x = execute_query("SELECT DISTINCT character_id FROM charactercreator_character count ORDER BY character_id DESC LIMIT 1")
# print(x)

print("How many of the Items are weapons? How many are not?")
x = execute_query("""SELECT sum(item_ptr_id)
FROM
(SELECT count(armory_weapon.item_ptr_id) AS item_ptr_id, charactercreator_character_inventory.character_id
FROM armory_weapon
INNER JOIN charactercreator_character_inventory ON armory_weapon.item_ptr_id = charactercreator_character_inventory.item_id
GROUP BY character_id);""")
print(x)

print("How many Items does each character have? (Return first 20 rows)")
x = execute_query("""SELECT character_id, count(item_id) AS item_id
FROM charactercreator_character_inventory
GROUP BY character_id LIMIT 20;""")
print(x)

print("How many Weapons does each character have? (Return first 20 rows)")
x = execute_query("""SELECT count(armory_weapon.item_ptr_id) AS item_ptr_id, charactercreator_character_inventory.character_id
FROM armory_weapon
INNER JOIN charactercreator_character_inventory ON armory_weapon.item_ptr_id = charactercreator_character_inventory.item_id
GROUP BY character_id LIMIT 20;""")
print(x)

print("On average, how many Items does each Character have?")
x = execute_query("""SELECT avg(item_id)
FROM
(SELECT character_id, count(item_id) AS item_id
FROM charactercreator_character_inventory
GROUP BY character_id);""")
print(x)

print("On average, how many Weapons does each character have?")
x = execute_query("""SELECT avg(item_ptr_id)
FROM
(SELECT count(armory_weapon.item_ptr_id) AS item_ptr_id, charactercreator_character_inventory.character_id
FROM armory_weapon
INNER JOIN charactercreator_character_inventory ON armory_weapon.item_ptr_id = charactercreator_character_inventory.item_id
GROUP BY character_id);""")
print(x)


#execute query 
#cur.execute("SELECT DISTINCT character_id FROM charactercreator_character count LIMIT 10")

rows = cur.fetchall()

for r in rows:
    print (f"character_id {r[0]}")

#commit it
# conn.commit()

#close the cursor
cur.close()
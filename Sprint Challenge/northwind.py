import sqlite3

conn = sqlite3.connect('northwind_small.sqlite3')

#cursor
cur = conn.cursor()




#inserting data
#execute method
def execute_query(query):
    cur.execute(query)
    results = cur.fetchall()
    print(results)

# Checking if I connected successfully with our northwind database
execute_query("""SELECT * FROM Product LIMIT 5;""")

"""
PART 2 Northwind Database
"""

# Questions 
print("What are the ten most expensive items (per unit price) in the database?")
x = execute_query("""SELECT ProductName, UnitPrice FROM Product ORDER BY UnitPrice DESC LIMIT 10;""")
print(x)

print("What is the average age of an employee at the time of their hiring? (Hint: a lot of arithmetic works with dates.)")
x = execute_query("""SELECT avg(HireDate - BirthDate) AS AverageAge FROM Employee;""")
print(x)

"""
PART 3 Sailing the Northwind Seas
"""
#Questions

# Will return ten most expensive items as CompanyName, ProductName, UnitPrice...
print("What are the ten most expensive items (per unit price) in the database and their suppliers?")
x = execute_query("""SELECT Supplier.CompanyName, Product.ProductName, Product.UnitPrice
FROM Product 
INNER JOIN Supplier ON Product.SupplierId = Supplier.Id
ORDER BY UnitPrice DESC LIMIT 10;""")
print(x)

#Will return largest categories by num of unique products as CategoryID, LargestCat, CategoryName
print("What is the largest category (by number of unique products in it)?")
x = execute_query(""" SELECT CategoryId,COUNT(*) AS `LargestCat`, CategoryName
FROM
(SELECT Category.CategoryName, Product.CategoryId
FROM Product 
INNER JOIN Category ON Product.CategoryId = Category.Id)
GROUP BY CategoryId
ORDER BY LargestCat DESC;""")
print(x)


#commit it
conn.commit()

#close the cursor
cur.close()
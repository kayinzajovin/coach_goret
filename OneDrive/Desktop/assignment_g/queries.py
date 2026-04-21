import sqlite3

conn = sqlite3.connect('nyondo_stock.db')

# Query A - Every column of every product
print("--- Query A ---")
rows = conn.execute('SELECT * FROM products').fetchall()
for r in rows: print(r)

# Query B - Only name and price
print("\n--- Query B ---")
rows = conn.execute('SELECT name, price FROM products').fetchall()
for r in rows: print(r)

# Query C - Product with id = 3
print("\n--- Query C ---")
row = conn.execute('SELECT * FROM products WHERE id = 3').fetchone()
print(row)

# Query D - Name contains 'sheet' (partial match)
print("\n--- Query D ---")
rows = conn.execute("SELECT * FROM products WHERE name LIKE '%sheet%'").fetchall()
for r in rows: print(r)

# Query E - All products sorted by price, highest first
print("\n--- Query E ---")
rows = conn.execute('SELECT * FROM products ORDER BY price DESC').fetchall()
for r in rows: print(r)

# Query F - Only the 2 most expensive products
print("\n--- Query F ---")
rows = conn.execute('SELECT * FROM products ORDER BY price DESC LIMIT 2').fetchall()
for r in rows: print(r)

# Query G - Update Cement price to 38000, then confirm
print("\n--- Query G ---")
conn.execute('UPDATE products SET price = 38000 WHERE id = 1')
conn.commit()
rows = conn.execute('SELECT * FROM products').fetchall()
for r in rows: print(r)
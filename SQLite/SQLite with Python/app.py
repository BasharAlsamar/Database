import sqlite3
from pprint import pprint


# 1. Create a new database and connect to it
conn = sqlite3.connect('./customer.db')

# 2. cursor
cursor = conn.cursor() 


'''3. SQL Statments:
- Create the customer table. 
- Create the product table.
- Create the orders table.
''' 

customer = '''CREATE TABLE customer (
    customer_id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT
);'''

product = '''CREATE TABLE product (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT,
    product_price REAL
);'''

orders = '''CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    product_id INTEGER,
    order_quantity INTEGER,
    FOREIGN KEY (customer_id) REFERENCES customer(customer_id),
    FOREIGN KEY (product_id) REFERENCES product(product_id)
);'''


# 4. Execute the SQL statments to create tables
cursor.execute(customer) 
cursor.execute(product)
cursor.execute(orders)


# 5. Insert some sample data into the tables.

cursor.execute("INSERT INTO customer (first_name, last_name) VALUES (?, ?)", ('John ', 'Doe'))
cursor.execute("INSERT INTO customer (first_name, last_name) VALUES (?, ?)", ('Ahmad', 'Soliman'))
cursor.execute("INSERT INTO customer (first_name, last_name) VALUES (?, ?)", ('Muster', 'Mann'))


cursor.execute("INSERT INTO product (product_name, product_price) VALUES (?, ?)", ('Milk', 10.0))
cursor.execute("INSERT INTO product (product_name, product_price) VALUES (?, ?)", ('Egg', 20.0))
cursor.execute("INSERT INTO product (product_name, product_price) VALUES (?, ?)", ('Apple', 30.0))
cursor.execute("INSERT INTO product (product_name, product_price) VALUES (?, ?)", ('Meat', 20.0))
cursor.execute("INSERT INTO product (product_name, product_price) VALUES (?, ?)", ('Orange', 15.0))


cursor.execute("INSERT INTO orders (customer_id, product_id,  order_quantity) VALUES (?, ?, ?)", (1, 4, 2))
cursor.execute("INSERT INTO orders (customer_id, product_id,  order_quantity) VALUES (?, ?, ?)", (2, 5, 3))
cursor.execute("INSERT INTO orders (customer_id, product_id,  order_quantity) VALUES (?, ?, ?)", (3, 4, 1))


# 6. Commit the changes to the database
conn.commit()


# 7. Query the tables to show the order name  and quantity based on customer name and product.
cursor.execute('''SELECT customer.first_name, customer.last_name, product.product_name,  orders.order_quantity, product.product_price
                         FROM customer
                         INNER JOIN orders ON customer.customer_id = orders.customer_id
                         INNER JOIN product ON orders.product_id = product.product_id''')


# 5. Get the results
rows = cursor.fetchall()


# Print the results
for row in rows:
    pprint(f'{row[0]} {row[1]} ordered a {row[2]} and the order quantity is  {row[3]} with price: {row[4]}')

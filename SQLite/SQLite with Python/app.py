import sqlite3
from pprint import pprint


class Database:
    def __init__(self, db_file) -> None:

        ''' 
        1. create connections to the database.
        2. create the crusor
        3. create the customer, product, and orders tables.
        '''
        self.conn  = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        self.create_tables()
    

    def create_tables(self):

        '''3.  cretae SQL Statments then  then excute them:
            - to create the customer table. 
            - to create the product table.
            - to create the orders table.
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

        self.cursor.execute(customer)
        self.cursor.execute(product)
        self.cursor.execute(orders)
    
    def add_customers(self, first_name, last_name):

        '''
        to insert values into customer table then commit the changes to the database
        '''

        self.cursor.execute("INSERT INTO customer (first_name, last_name) VALUES (?, ?)", (first_name, last_name))
        self.conn.commit()

    
    def add_products(self, product_name, product_price):

        '''
        to insert values into product table then commit the changes to the database
        '''

        self.cursor.execute("INSERT INTO product (product_name, product_price) VALUES (?, ?)", (product_name, product_price))
        self.conn.commit()
    
    def add_orders(self, customer_id, product_id, order_quantity):

        '''
        to insert values into orders table then commit the changes to the database
        '''

        self.cursor.execute("INSERT INTO orders (customer_id, product_id,  order_quantity) VALUES (?, ?, ?)", 
                            (customer_id, product_id, order_quantity))
        self.conn.commit()
    

    def get_queries(self):

        '''
        - Excute the required queries.
        - Get and print the results.
        '''

        self.cursor.execute('''SELECT customer.first_name, customer.last_name, product.product_name,  orders.order_quantity, product.product_price
                         FROM customer
                         INNER JOIN orders ON customer.customer_id = orders.customer_id
                         INNER JOIN product ON orders.product_id = product.product_id''')
        

        rows = self.cursor.fetchall()
        

        results = []
        for row in rows:
            results.append(f'{row[0]} {row[1]} ordered a {row[2]} and the order quantity is  {row[3]} with price: {row[4]}')
        
        return results
    


def main():

    # Create a new database and connect to it
    db = Database('./SQLite/SQLite with Python/database.db')

    # Insert some sample data into the tables.
    db.add_customers('John ', 'Doe')
    db.add_customers('Ahmad', 'Soliman')
    db.add_customers('Muster', 'Mann')

    db.add_products('Milk', 10.0)
    db.add_products('Egg', 20.0)
    db.add_products('Apple', 30.0)
    db.add_products('Meat', 40.0)
    db.add_products('Orange', 15.0)

    db.add_orders(1, 2, 2)
    db.add_orders(2, 5, 3)
    db.add_orders(3, 4, 1)


    # Get the results and store the results into txt file
    orders = db.get_queries()

    with open('./SQLite/SQLite with Python/output.txt', 'w') as f:
        for order in orders:
            f.write(order + '\n')
            pprint(order)


if __name__ == '__main__':
    main()

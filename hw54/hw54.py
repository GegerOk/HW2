import sqlite3

connection = sqlite3.connect('database_2.db')
cursor = connection.cursor()

def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products
    (id INT PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INT)              
''')
    for i in range (4):
        cursor.execute('INSERT INTO Products (title, description, price) VALUES (?,?,?)', (f'title {i}', f'description {i}', f'{i}'))
    
def get_all_products():
    cursor.execute('SELECT id, title, description, price FROM Products')
    res = cursor.fetchall()
    return (res)

#initiate_db()
get_all_products()
connection.commit()
connection.close()
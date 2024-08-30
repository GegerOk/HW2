import sqlite3

connection = sqlite3.connect('database_2.db')
cursor = connection.cursor()
connection_user = sqlite3.connect('users.db')
cursor_user = connection_user.cursor()

def initiate_db():
    connection_user = sqlite3.connect('users.db')
    cursor_user = connection_user.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products
    (id INT PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INT)              
''')
    cursor_user.execute(
'''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER NOT NULL,
balance INTEGER NOT NULL)
''')
    for i in range (4):
        cursor.execute('INSERT INTO Products (title, description, price) VALUES (?,?,?)', (f'title {i}', f'description {i}', f'{i}'))


def is_include(username):
    connection_user = sqlite3.connect('users.db')
    cursor_user = connection_user.cursor()
    cursor_user.execute('SELECT username FROM Users WHERE username = ?', (username,))
    res = cursor_user.fetchall()
    connection_user.commit()
    connection_user.close()

    
    if res:
        print('Yep')
        return True
    else:
        print('Nah')
        return False

def add_user(username, email, age):
    connection_user = sqlite3.connect('users.db')
    cursor_user = connection_user.cursor()
    cursor_user.execute('INSERT INTO Users (username, email, age, balance) VALUES (?,?,?,?)', (f'{username}', f'{email}', f'{age}', '1000'))
    connection_user.commit()

def get_all_products():
    cursor.execute('SELECT id, title, description, price FROM Products')
    res = cursor.fetchall()
    connection.commit()
    return (res)

connection_user.commit()
connection_user.close()

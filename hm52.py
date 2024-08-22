import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

cursor.execute(
    '''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
'''
)

#cursor.execute ('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')
#
#for i in range (10):
#    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?,?,?,?)', (f'newuser{i}', f'ex{i}@mail.ru', f'{(i +1)*10}', '1000'))
#
#for i in range (1, 10, 2):
#    cursor.execute ('UPDATE Users SET balance =? WHERE username = ?',(500, f'newuser{i}'))
#
#for i in range (1, 10, 3):
#    cursor.execute ('DELETE FROM Users WHERE username = ?', (f'newuser{i}',))

#cursor.execute ('DELETE FROM Users WHERE id = ?', (6,))
#
#cursor.execute ('SELECT id, username, email, age, balance FROM Users WHERE age != ?', (60,))
#res = cursor.fetchall()
#for users in res:
#    id, username, email, age, balance = users
#    print (f'Имя: {username} | Почта: {email} | Возраст: {age} | Баланс: {balance}, {id}')

cursor.execute ('SELECT COUNT (*) FROM Users')
zadanie_1 = cursor.fetchone()[0]
print (zadanie_1)

cursor.execute ('SELECT SUM (balance) FROM Users')
zadanie_2 = cursor.fetchone()[0]
print (zadanie_2)

cursor.execute ('SELECT AVG (balance) FROM Users')
zadanie_3 = cursor.fetchone()[0]
print (zadanie_3)


connection.commit()
connection.close()
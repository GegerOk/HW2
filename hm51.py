import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

cursor.execute(
    '''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRINARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
'''
)

cursor.execute ('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')

#for i in range (10):
#    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?,?,?,?)', (f'newuser{i}', f'ex{i}@mail.ru', f'{(i +1)*10}', '1000'))

#for i in range (1, 10, 2):
#    cursor.execute ('UPDATE Users SET balance =? WHERE username = ?',(500, f'newuser{i}'))

#for i in range (1, 10, 3):
#    cursor.execute ('DELETE FROM Users WHERE username = ?', (f'newuser{i}',))

cursor.execute ('SELECT username, email, age, balance FROM Users WHERE age != ?', (60,))
res = cursor.fetchall()
for users in res:
    username, email, age, balance = users
    print (f'Имя: {username} | Почта: {email} | Возраст: {age} | Баланс: {balance}')

connection.commit()
connection.close()
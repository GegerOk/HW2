from fastapi import FastAPI, Path

app = FastAPI()

users = {'1': 'Имя: Example, возраст 18'}

@app.get ('/users')
async def base() -> dict:
    return users

@app.post('/user/{username}/{age}')
async def add_user(username, age) -> str:
    curent_id= str(int(max(users, key=int)) +1)
    users[curent_id] = f'Имя: {username}, возраст: {age}'
    return f'User {curent_id} is registred'

@app.put('/user/{user_id}/{username}/{age}')
async def edit_user(user_id, username, age) -> str:
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'The user {user_id} is registred'

@app.delete('/user/{user_id}')
async def delete_user(user_id) -> str:
    users.pop(user_id)
    return 'User was deleted'
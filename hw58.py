from fastapi import FastAPI, Path, HTTPException
from pydantic import BaseModel
app = FastAPI()

global users
users = []


class User(BaseModel):
    id: int
    username: str 
    age: int 

@app.get ('/users')
async def base() -> list[User]:
    return users

@app.post('/user/{username}/{age}')
async def add_user(username, age) -> dict:
    if users:
        curent_id=(max(users.id for users in users) +1)
    else:
        curent_id = 1
    user = User(id = curent_id, username=username, age=age)
    users.append(user)
    return user.dict()

@app.put('/user/{user_id}/{username}/{age}')
async def edit_user(user_id, username, age) -> dict:
    try:
        user = User(id = user_id, username = username, age = age)
        users[int(user_id) -1] = user
    except IndexError:
        raise HTTPException(status_code= 404, detail= 'User was not found')
    return user.dict()

@app.delete('/user/{user_id}')
async def delete_user(user_id) -> list[User]:
    try:
        users.pop(int(user_id)-1)
    except IndexError:
        raise HTTPException (status_code= 404, detail= 'User was not found')
    return users
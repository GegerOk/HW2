from typing import Annotated
from fastapi import FastAPI, Path, HTTPException
from pydantic import BaseModel
app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


class User(BaseModel):
    id: int
    username: str 
    age: int 

@app.get ('/users')
async def base() -> dict:
    return users

@app.post('/user/{username}/{age}')
async def add_user(username: Annotated [str, Path(min_length=3, max_length=15, description= 'Enter your username', example= 'Gregor')], age: Annotated[int, Path(ge=18, le= 99, description= 'Enter your age', example= 21)]) -> str:
    if users:
        current_id=str(int(max(users, key=int)) +1)
    else:
        current_id = 1
    users[current_id] = f'Имя: {username}, возраст: {age}'
    return f'User {current_id} is registred'

@app.put('/user/{user_id}/{username}/{age}')
async def edit_user(user_id, username: Annotated [str, Path(min_length=3, max_length=15, description= 'Enter your username', example= 'Gregor')], age: Annotated[int, Path(ge=18, le= 99,description= 'Enter your age', example= 21)]) -> str:
    try:
        users[int(user_id)] = f'Имя: {username}, возраст: {age}'
    except IndexError:
        raise HTTPException(status_code= 404, detail= 'User was not found')
    return f'The user {user_id} is registred'

@app.delete('/user/{user_id}')
async def delete_user(user_id) -> str:
    try:
        del users[user_id]
    except IndexError:
        raise HTTPException (status_code= 404, detail= 'User was not found')
    return f'User {user_id} has been deleted'

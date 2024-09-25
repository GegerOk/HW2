from pipes import Template
from fastapi import FastAPI, Path, HTTPException, Body, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates

from DopHw1 import user

app = FastAPI()

templates = Jinja2Templates(directory = 'hw59')

global users
users = []


class User(BaseModel):
    id: int
    username: str 
    age: int 

@app.get('/', response_class=HTMLResponse)
async def get_all_users(request: Request) -> HTMLResponse:
    return templates.TemplateResponse('users.html', {'request': request, 'users': users})


@app.get('/users/{user_id}', response_class=HTMLResponse)
async def get_user(request: Request, user_id: int) -> HTMLResponse:
    user = users[user_id - 1]
    return templates.TemplateResponse('users.html', {'request': request, 'user': user, 'users': None})

@app.post('/user/{username}/{age}')
async def add_user(username, age) -> dict:
    if users:
        curent_id=(max(users.id for users in users) +1)
    else:
        curent_id = 1
    user = User(id = curent_id, username=username, age=age)
    users.append(user)
    return user.dict()
from fastapi import FastAPI
from routers import task, user
from models.user import User
from models.task import Task


app = FastAPI()

app.include_router(task.router_task)
app.include_router(user.router_user)

@app.get('/')
async def base():
    return {'message': 'Welcome to Taskmanager'}
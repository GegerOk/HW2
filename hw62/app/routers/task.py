from fastapi import APIRouter, Depends, status, HTTPException
# Сессия БД
from sqlalchemy.orm import Session
# Функция подключения к БД
from app.backend.db_depends import get_db
# Аннотации, Модели БД и Pydantic.
from typing import Annotated
from app.models import User, Task
from app.schemas import UpdateTask, CreateTask
# Функции работы с записями.
from sqlalchemy import insert, select, update, delete
# Функция создания slug-строки
from slugify import slugify
from routers.user import router_user


router_task = APIRouter(prefix= '/task', tags=['task'])

@router_task.get('/')
async def all_tasks(db: Annotated[Session, Depends(get_db)]):
    query = select(Task)
    result = db.execute(query).scalars().all()
    return result

@router_task.get('/{task_id}')
async def task_by_id(task_id: int, db: Annotated[Session, Depends(get_db)]):
    query = select(Task).where(Task.id == task_id)
    result = db.execute(query).scalar_one_or_none()

    if result is None:
        raise HTTPException(status_code=404, detail="Task was not found")

    return result

@router_task.post('/create')
async def create_task(task: CreateTask, user_id: int, db: Annotated[Session, Depends(get_db)]):
    existing_user = db.execute(select(User).where(User.id == user_id)).scalar_one_or_none()
    if existing_user is None:
        raise HTTPException(status_code=404, detail="User was not found")

    new_task = Task(**task.dict(), user_id=user_id)
    db.add(new_task) 
    db.commit() 
    return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}

@router_task.put('/update/{task_id}')
async def update_task(task_id: int, task: UpdateTask, db: Annotated[Session, Depends(get_db)]):
    query = select(Task).where(Task.id == task_id)
    existing_task = db.execute(query).scalar_one_or_none()

    if existing_task is None:
        raise HTTPException(status_code=404, detail="Task was not found")

    for key, value in task.dict(exclude_unset=True).items():
        setattr(existing_task, key, value)  # Обновляем поля

    db.commit()
    return {'status_code': status.HTTP_200_OK, 'transaction': 'Task update is successful!'}

@router_task.delete('/delete/{task_id}')
async def delete_task(task_id: int, db: Annotated[Session, Depends(get_db)]):
    query = select(Task).where(Task.id == task_id)
    existing_task = db.execute(query).scalar_one_or_none()

    if existing_task is None:
        raise HTTPException(status_code=404, detail="Task was not found")

    db.execute(delete(Task).where(Task.id == task_id))
    db.commit()
    return {'status_code': status.HTTP_200_OK, 'transaction': 'Task deleted successfully!'}

@router_user.get('/{user_id}/tasks')
async def tasks_by_user_id(user_id: int, db: Annotated[Session, Depends(get_db)]):
    query = select(Task).where(Task.user_id == user_id)
    result = db.execute(query).scalars().all()
    return result

@router_user.delete('/delete/{user_id}')
async def delete_user(user_id: int, db: Annotated[Session, Depends(get_db)]):
    query = select(User).where(User.id == user_id)
    existing_user = db.execute(query).scalar_one_or_none()

    if existing_user is None:
        raise HTTPException(status_code=404, detail="User was not found")
    db.execute(delete(Task).where(Task.user_id == user_id))
    db.execute(delete(User).where(User.id == user_id))
    db.commit()
    return {'status_code': status.HTTP_200_OK, 'transaction': 'User and all related tasks deleted successfully!'}
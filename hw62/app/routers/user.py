from fastapi import APIRouter, Depends, status, HTTPException
# Сессия БД
from sqlalchemy.orm import Session
# Функция подключения к БД
from app.backend.db_depends import get_db
# Аннотации, Модели БД и Pydantic.
from typing import Annotated
from app.models import User
from app.schemas import CreateUser, UpdateUser
# Функции работы с записями.
from sqlalchemy import insert, select, update, delete
# Функция создания slug-строки
from slugify import slugify



router_user = APIRouter(prefix= '/user', tags=['user'])

@router_user.get('/')
async def all_users(db: Annotated[Session, Depends(get_db)]):
    query = select(User)
    result = db.execute(query).scalars().all()
    return result

@router_user.get('/{user_id}')
async def user_by_id(user_id: int, db: Annotated[Session, Depends(get_db)]):
    query = select(User).where(User.id == user_id)
    result = db.execute(query).scalar_one_or_none()

    if result is None:
        raise HTTPException(status_code=404, detail="User was not found")
    
    return result

@router_user.post('/create')
async def create_user(user: CreateUser, db: Annotated[Session, Depends(get_db)]):
    new_user = User(**user.dict())
    db.execute(insert(User).values(new_user.__dict__))
    db.commit()
    return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}

@router_user.put('/update/{user_id}')
async def update_user(user_id: int, user: UpdateUser, db: Annotated[Session, Depends(get_db)]):
    query = select(User).where(User.id == user_id)
    existing_user = db.execute(query).scalar_one_or_none()
    
    if existing_user is None:
        raise HTTPException(status_code=404, detail="User was not found")
    
    # Обновляем поля
    for key, value in user.dict(exclude_unset=True).items():
        setattr(existing_user, key, value)

    db.commit()
    return {'status_code': status.HTTP_200_OK, 'transaction': 'User update is successful!'}

@router_user.delete('/delete/{user_id}')
async def delete_user(user_id: int, db: Annotated[Session, Depends(get_db)]):
    query = select(User).where(User.id == user_id)
    existing_user = db.execute(query).scalar_one_or_none()

    if existing_user is None:
        raise HTTPException(status_code=404, detail="User was not found")

    db.execute(delete(User).where(User.id == user_id))
    db.commit()
    return {'status_code': status.HTTP_200_OK, 'transaction': 'User deleted successfully!'}
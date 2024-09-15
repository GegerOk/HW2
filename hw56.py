from fastapi import FastAPI

app = FastAPI()

@app.get ('/')
async def base() -> dict:
    return {'message': "Главная страница"}

@app.get ('/user/admin')
async def base() -> dict:
    return {'message': "Вы вошли как администратор"}

@app.get ('/user/{user_id}')
async def base(user_id: str) -> dict:
    return {'message': f"Вы вошли как {user_id}"}

@app.get ('/user')
async def base(user_name: str, age: int) -> dict:
    return {'message': f"Информация о пользователе имя: {user_name}, возраст: {age}"}

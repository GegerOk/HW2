from fastapi import FastAPI, Path

app = FastAPI()

#@app.get ('/')
#async def base() -> dict:
#    return {'message': "Главная страница"}
#
#@app.get ('/user/admin')
#async def base() -> dict:
#    return {'message': "Вы вошли как администратор"}

@app.get ('/user/{user_id}')
async def base(user_id: int = Path(ge= 1, le= 100, description= 'Enter User ID', examples= 25)) -> dict:
    return {'message': f"Вы вошли как {user_id}"}

@app.get ('/user/{username}/{age}')
async def base(username: str = Path(min_length= 5, max_length= 20, description= 'Enter username', examples= 'Urban user'),
                age: int = Path(ge= 18, le= 120, description= 'Enter age', examples= '24')) -> dict:
    return {'message': f"Информация о пользователе имя: {username}, возраст: {age}"}

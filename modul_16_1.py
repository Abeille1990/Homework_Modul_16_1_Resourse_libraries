from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def welcome() -> dict:
    return {"message": "Главная страница"}


@app.get("/user/admin")
async def welcome_adm() -> dict:
    return {"message": "Вы вошли как администратор"}


@app.get("/user/{userid}")
async def welcome_user(userid: int) -> dict:
    return {"message": f'Вы вошли как пользователь №{userid}'}


@app.get("/user")
async def user_info(user_name: str, user_age: float) -> dict:
    return {"Информация о пользователе": f'Имя: {user_name}. Возраст: {user_age}'}

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Inicia el server: uvicorn users:app --reload

# Entidad user
class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int
    
users_list = [User(id=1, name="Brais", surname="Moure", url="https:// moure.dev", age=35 ), 
              User(id=2, name="Moure", surname="Dev", url="https://mouredev.com", age=27), User(id=3, name="Dashlberg", surname="Haakon", url="https://Hankoon.com", age=35) ]

@app.get("/usersjson")
async def usersjson():
    return [{"name": "Brais", "surname": "Moure", "url": "https://moure.dev", "age": 35},
            {"name": "Moure", "surname": "Dev", "url": "https://mouredev.com", "age": 27},
            {"name": "Haakon", "surname": "Dahlberg", "url": "https://haakon.com", "age": 45}]

   
@app.get("/users")
async def users():
    return users_list

# Path

@app.get("/user/{id}")
async def user(id:int):
    return search_user(id)

# Query

@app.get("/user/")
async def user(id: int):
    return search_user(id)
    
def search_user(id:int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"Error": "no encontrado  el usuario"}
    
# 2:22
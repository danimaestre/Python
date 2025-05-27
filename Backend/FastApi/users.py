from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Inicia el server: uvicorn users:app --reload

# Entidad user
class User(BaseModel):
    name: str
    surname: str
    url: str
    age: int
    
users_list = [User(name="Brais", surname="Moure", url="https:// moure.dev", age=35 ), 
              User(name="Moure", surname="Dev", url="https://mouredev.com", age=27), User(name="Dashlberg", surname="Haakon", url="https://Hankoon.com", age=35) ]

@app.get("/usersjson")
async def usersjson():
    return [{"name": "Brais", "surname": "Moure", "url": "https://moure.dev", "age": 35},
            {"name": "Moure", "surname": "Dev", "url": "https://mouredev.com", "age": 27},
            {"name": "Haakon", "surname": "Dahlberg", "url": "https://haakon.com", "age": 45}]

   
@app.get("/users")
async def users():
    return users_list

# 2:05

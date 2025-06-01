from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool
    
class userDB(User):
    "pasword": str # type: ignore
    
user_db = {
    "mouredev": {
        "username": "mouredev",
        "full_name": "Brais Moure",
        "email": "braismoure@mourede.com",
        "disabled": False,
        "password": "123456",
    },
    "mouredev2": {
        "username": "mouredev2",
        "full_name": "Brais Moure 2",
        "email": "braismoure2@mourede.com",
        "disabled": True,
        "password": "654321",
    }
}

#4:13...
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return  "¡ Hola FastAPI !"

@app.get("/url")
async def url():
    return {"url": "https://mouredev.com/python"}

#Inicia el server: uvicorn main:app --reload
#Detener el server: CTRL+C
#Documentacion con Sawgger: htpps://127.0.0.1:8000/docs
#Documentacion con Redocly: htpps://127.0.0.1:8000/redoc


from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "¡ Hola FastAPI"}

# 1: 15...
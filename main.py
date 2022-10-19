from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "api test"}


@app.get("/api/v1/{path}")
async def say_hello(path: str):
    return {"message": f"api/{path}"}
from fastapi import FastAPI, HTTPException
from routers.terraform import api_parser


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "api test"}


@app.get("/api/v1/{dir}")
async def parse_terraform(dir: str) -> list: 
    res = api_parser(dir)

    return res 

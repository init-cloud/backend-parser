from fastapi import FastAPI, HTTPException
from routers.terraform import api_parser


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "api test"}


@app.get("/api/v1/")
async def parse_terraform():
    res = api_parser()
    return res 

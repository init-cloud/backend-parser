from fastapi import FastAPI, HTTPException
from routers.terraform import api_parser


app = FastAPI()

@app.get("/")
async def root():
    return {"state": "Parser on."}


@app.get("/{provider}/{dir}")
async def parse_terraform(dir: str, provider: str) -> list: 
    res = api_parser(dir, provider=provider)

    return res 

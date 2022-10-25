from fastapi import FastAPI, HTTPException
from service.impl.parser import TFParser
 

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "api test"}


@app.get("/api/v1/")
async def parse_terraform():
    parser = TFParser()
    f = parser.load_file()
    res = parser.get_block_value(f)
    return { "result" : res }
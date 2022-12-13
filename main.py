from fastapi import FastAPI
import uvicorn

from mylib.logic import search_wiki
from mylib.logic import wiki as get_wiki
from mylib.logic import phrase as get_phrase

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Wikipedia API end point. Usage: /search or /wiki or /phrase"}


@app.get("/search/{value}")
async def search(value: str):
    """Search Wikipedia using keywords"""
    result = search_wiki(value)
    return {"result": result}


@app.get("/wiki/{value}")
async def wiki(value: str):
    """Get Wikipedia page using keywords"""
    result = get_wiki(value)
    return {"result": result}


@app.get("/phrase/{value}")
async def phrase(value: str):
    """Get Wikipedia phrases"""
    result = get_phrase(value)
    return {"result": result}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")

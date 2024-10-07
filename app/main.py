from contextlib import asynccontextmanager

from fastapi import FastAPI
from models import init_models
import uvicorn


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_models()
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/")
def index():
    return "Hello World!"


if __name__=="__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

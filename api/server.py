from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(title="ErekeAnime API")


@app.get("/")
def home():

    return {
        "app": "ErekeAnime",
        "version": "0.6"
    }


@app.get("/status")
def status():

    return {
        "status": "running"
    }

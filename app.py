import requests
from fastapi import FastAPI
from uvicorn import run

app = FastAPI()

@app.get('/')
def welcome():
    return {
        'Greeting': 'Hello Ww'
    }

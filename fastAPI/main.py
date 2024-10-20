from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/hello")
def hello():

    x = "hello world ;)"
    return {"message": x}

@app.post("/predict")
    return {"message": "post"}

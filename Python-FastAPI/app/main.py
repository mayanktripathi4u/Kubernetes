# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}



# ----  Modify to use ENV variables ----
import os
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    data = f"ENV: {os.environ.get('ENV', 'DEFAULT_ENV')}, Host: {os.environ.get('HOSTNAME', 'DEFAULT_HOST')}"
    return {"Hello": data}
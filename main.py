from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def greetings():
    return {"message":"Hello"}

@app.get("/methods")
def methods():
    return {"m":"s"}

@app.get("/env")
def env():
    return {"db_url" : os.getenv("Database_URL")}
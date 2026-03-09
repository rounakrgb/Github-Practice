from fastapi import FastAPI
import os


app = FastAPI()
Database_URL = "postgresql://host.docker.internal:pass123@localhost:5432/git_data"
@app.get("/")
def greetings():
    return {"message":"Hello"}



@app.get("/env")
def env():
    return {"db_url" : os.getenv("Database_URL")}
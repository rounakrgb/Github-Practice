from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def greetings():
    return {"message":"Hello"}


@app.get("/june")
def show_june():
    return {"j":"alkjfdlkajlkdfjlkaj"}
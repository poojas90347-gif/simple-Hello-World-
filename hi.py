from fastapi import FastAPI
app= FastAPI()
@app.get("/")
def home():
    return{"message": "Hello FastAPI"}

@app.get("/hi")
def hi():
    return{"message" : "Hi from GET!"}

@app.post("/hi")
def hi_post():
    return{"message": "Hi from POST!"}
    
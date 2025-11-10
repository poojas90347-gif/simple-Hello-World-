from fastapi import FastAPI
from schemas import UserCreate 
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

@app.post("/User")
def create_user(user: UserCreate):
    return{"User": user.name, "age":user.age}  
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def asif():
    Chatgpt = {
"message": "Hello, world",

    }
    return Chatgpt

@app.get("/chatgpt")
def ali():
    Chatgpt = {
"message": "This is a chatgpt message",

    }
    return Chatgpt

@app.get("/gemini")
def dee():
    Gemini = {
"message": "This is a gemini message",

    }
    return Gemini

@app.post("/gemini")
def dee(x,y):
    Gemini = {
"message": int(x)+int(y)

    }
    return Gemini

@app.post("/todo")
def add_todo(name ,message):
    Gemini = {
"message": {"name" :name,"messgae": message}

    }
    return Gemini



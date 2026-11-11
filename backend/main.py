from fastapi import FastAPI
import uvicorn
klu=FastAPI(title="AI Tutor",
            description="AI Tutor PBL project",
            version="1.0.0",)

@klu.get("/")
def home():
    return {"message":"Welcome to AI Tutor project"}

@klu.get("/demo")
def demo():
    return{"message":"KL University"}

@klu.get("/askquestion")
def ask():
    return{"message":"What is LLM","Answer":"Large language model"}
@klu.get("/emp")
def emp():
    return {"id":1,"name":"Ram","Gender":"Male","course":"DSA"}
@klu.get("/students")
def getstudents():
    return [{"id":1,"name":"Ram","Gender":"Male","course":"DSA"},
            {"id":2,"name":"Harthiek","Gender":"Male","course":"DSA"},
            {"id":3,"name":"seetha","Gender":"Female","course":"DSA"}
            ]
if __name__ == "__main__":
    uvicorn.run("main:klu", host="127.0.0.1", port=2027, reload=True)
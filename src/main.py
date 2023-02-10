from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"Key":"Value3"}


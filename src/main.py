import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"Key":"Value"}

if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")

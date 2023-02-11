from flask import Flask

app = Flask(__name__)


@app.route("/", methods='GET')
def home():
    return {"Key":"Value2"}

@app.route("/hello", methods='GET')
def hello():
    return {"Hello":"From container!"}

if __name__ == "__main__":
    app.run()

from flask import Flask

app = Flask(__name__)


@app.route("/", methods=['GET'])
def home():
    return "<h1>Hello FINALLY!!</h1>"

@app.route("/hello", methods=['GET'])
def hello():
    return {"Hello":"From container!"}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port="8080")

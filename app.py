from flask import Flask

PORT = 8085
MESSAGE = "Hello from Aytac!\n"

app = Flask(__name__)


@app.route("/")
def root():
    result = MESSAGE.encode("utf-8")
    return result

@app.route("/<name>")              # at the end point /<name>
def hello_name(name):              # call method hello_name
    return "Hello "+ name          # which returns "hello + name

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=PORT)
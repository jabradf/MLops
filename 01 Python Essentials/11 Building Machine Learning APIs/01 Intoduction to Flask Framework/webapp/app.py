from flask import Flask, abort

app = Flask(__name__)   # name can be anything, this is the common way of doing it by using __name__

@app.route("/")
def two_hundred():
    return "200! all is good in the app."

@app.route("/error")
def error():
    abort(500, "oooh some error!")


if __name__ == "__main__":
    app.run(debug=True, port=8000, host="0.0.0.0")  # use a different port for debugging, not the standard 80
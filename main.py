from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/encode")
def encode():
    pass


@app.route("/decode")
def decode():
    pass



if __name__ == "__main__":
    app.run(debug=True)
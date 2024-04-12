from flask import Flask, request, jsonify
import base64

app = Flask(__name__)


@app.route("/encode")
def encode():
    data = request.data
    encoded = base64.b64encode(data)
    return jsonify({"url": "https://short.est/" + str(encoded)})


@app.route("/decode")
def decode():
    data = request.data
    url = str(data).split("/")[-1]
    decoded = base64.b64decode(url)
    return jsonify({"url": decoded})


if __name__ == "__main__":
    app.run(debug=True)

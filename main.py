from flask import Flask, request, jsonify
import database

app = Flask(__name__)

db = database.database("url.db")


@app.route("/encode")
def encode():
    data = request.data
    shortened = db.store_url(data)
    return jsonify({'url': "https://short.est/" + shortened})


@app.route("/decode")
def decode():
    data = request.data
    url = str(data).split("/")[-1]
    decoded = db.get_url(url)
    if decoded is None:
        return jsonify({'error': ''})
    return jsonify({'url': decoded})


if __name__ == "__main__":
    app.run(debug=True)

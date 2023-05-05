from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/api", methods=["POST"])
def reverse_string():
    data = request.get_json()

    if 'input_string' not in data:
        return jsonify({"message": "Missing input_string"}), 400
    
    reverse_string = data['input_string'][::-1]

    return jsonify({"reverse_string": reverse_string})
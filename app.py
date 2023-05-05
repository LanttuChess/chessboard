from flask import Flask, request, jsonify
import chesslogic_module

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/api", methods=["POST"])
def board_state():
    data = request.get_json()

    if 'board_occupation' not in data:
        return jsonify({"message": "Missing board_occupation"}), 400
    
    return_state = chesslogic_module.reverse(data.get('board_occupation'))

    return jsonify({"return_state": return_state})
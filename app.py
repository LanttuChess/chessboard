from flask import Flask, request, jsonify
import chesslogic_module

app = Flask(__name__)


@app.route("/fen", methods=["GET"])
def board_state_fen():

    return_state = chesslogic_module.current_state_fen

    return jsonify({"return_state": return_state()})


@app.route("/unicode", methods=["GET"])
def board_state_unicode():

    return_state = chesslogic_module.current_state_unicode

    return jsonify({"return_state": return_state()})


@app.route("/raw", methods=["GET"])
def board_state_raw():

    return_state = chesslogic_module.current_state_raw

    return jsonify({"return_state": return_state()})


@app.route("/api", methods=["POST"])
def board_state():
    data = request.get_json()

    if 'board_occupation' not in data:
        return jsonify({"message": "Missing board_occupation"}), 400
    
    return_state = chesslogic_module.legal_moves(data.get('board_occupation'))

    return jsonify({"return_state": return_state})
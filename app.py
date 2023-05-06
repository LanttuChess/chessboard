from flask import Flask, request, jsonify
import chesslogic
import movedetection

app = Flask(__name__)


@app.route("/", methods=["GET"])
def root_message():
    return "Chess validator service for Intelligent Chess Board project. Please use following paths and request types: \n\n \\fen GET \n \\unicode GET \n \\raw GET \n \\api POST \n \\newgame POST \n\n for example."

@app.route("/fen", methods=["GET"])
def board_state_fen():

    return_state = chesslogic.current_state_fen

    return jsonify({"return_state": return_state()})


@app.route("/unicode", methods=["GET"])
def board_state_unicode():

    return_state = chesslogic.current_state_unicode

    return jsonify({"return_state": return_state()})


@app.route("/raw", methods=["GET"])
def board_state_raw():

    return_state = chesslogic.current_state_raw

    return jsonify({"return_state": return_state()})



@app.route("/newgame", methods=["POST"])
def new_game():

    movedetection.reset_physical_state()
    return_state = chesslogic.start_new_game

    return jsonify({"return_state": return_state()})



@app.route("/api", methods=["POST"])
def board_state():
    data = request.get_json()

    if 'board_occupation' not in data:
        return jsonify({"message": "Missing board_occupation"}), 400
    
    return_state = chesslogic.legal_moves(data.get('board_occupation'))

    return jsonify({"return_state": return_state})



@app.route("/change", methods=["POST"])
def state_change():
    data = request.get_json()

    if 'board_occupation' not in data:
        return jsonify({"message": "Missing board_occupation"}), 400
    
    return_state = movedetection.state_change_detector(data.get('board_occupation'))

    return jsonify({"return_state": return_state})
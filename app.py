from flask import Flask, request, jsonify
import chesslogic.chesslogic as chesslogic
from movedetection.MoveDetection import MoveDetection
import services.messaging as messaging


app = Flask(__name__)


initial_state = "1,1,1,1,1,1,1,1/1,1,1,1,1,1,1,1/0,0,0,0,0,0,0,0/0,0,0,0,0,0,0,0/0,0,0,0,0,0,0,0/0,0,0,0,0,0,0,0/1,1,1,1,1,1,1,1/1,1,1,1,1,1,1,1"
m = MoveDetection(8, initial_state)


@app.route("/", methods=["GET"])
def root_message():
    return "Chess validator service for Intelligent Chess Board Sähköpaja project."


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
    return_state = chesslogic.start_new_game
    m.reset(initial_state)

    return jsonify({"return_state": return_state()})


@app.route('/change', methods=['POST'])
def update_matrix():
    data = request.get_json()

    # Error handling
    if data is None:
        rgb_data = messaging.format_legal_moves

        return jsonify({"message": "No data provided. Request was: " + str(request), 'rgb_data': rgb_data}), 400

    input_str = data.get('board_occupation')

    if input_str is None:
        rgb_data = messaging.format_legal_moves

        return jsonify({"message": "No board_occupation data is JSON.", 'rgb_data': rgb_data}), 400

    elif input_str:
        changes, move_results = messaging.make_move(m, input_str)

        rgb_data = messaging.format_legal_moves()

        return jsonify({
            'message': "Matrix updated successfully.",
            'changes': changes,
            'move_results': move_results,
            'rgb_data': rgb_data
        }), 200
    else:
        return {"message": "No board_occupation data provided."}, 400


@app.route('/detect_changes', methods=['GET'])
def detect_changes():
    changes = m.state_change_detector()
    return jsonify({'changes': changes})


@app.route('/get_matrix', methods=['GET'])
def get_matrix():
    current_matrix = m.get_current_matrix()
    return jsonify({'matrix': current_matrix})


@app.route('/get_change_sum', methods=['GET'])
def get_change_sum():
    return jsonify({'change_sum': m.get_change_sum()})


@app.route('/get_positions_with_pieces', methods=['GET'])
def get_positions_with_pieces():
    positions = m.get_positions_with_pieces()
    rgb_data = positions.replace('0', '000000')
    rgb_data = rgb_data.replace('1', 'FFFF00').replace(
        ",", "").replace("/", "")
    return jsonify({'data': positions, 'rgb_data': rgb_data}), 200


@app.route('/pieces_with_legal_moves', methods=['GET'])
def pieces_with_legal_moves():
    pieces = chesslogic.get_pieces_with_legal_moves_coord(chesslogic.board)
    return jsonify({'message': "Fetched pieces with legal moves successfully.", 'data': list(pieces)}), 200


@app.route('/board_with_legal_moves_matrix', methods=['GET'])
def board_with_legal_moves():
    board = chesslogic.get_board_with_legal_moves(chesslogic.board)
    rgb_data = messaging.format_legal_moves()

    return jsonify({'message': "Fetched board with legal moves successfully.", 'matrix_data': board, 'rgb_data': rgb_data}), 200

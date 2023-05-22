from flask import Flask, request, jsonify
import chesslogic.chesslogic as chesslogic
from movedetection.MoveDetection import MoveDetection


# move_detection = MoveDetection()


app = Flask(__name__)


# @app.route("/", methods=["GET"])
# def root_message():
#     return "Chess validator service for Intelligent Chess Board project. Please use following paths and request types: \n\n \\fen GET \n \\unicode GET \n \\raw GET \n \\api POST \n \\newgame POST \n\n for example."

# @app.route("/fen", methods=["GET"])
# def board_state_fen():

#     return_state = chesslogic.current_state_fen

#     return jsonify({"return_state": return_state()})


# @app.route("/unicode", methods=["GET"])
# def board_state_unicode():

#     return_state = chesslogic.current_state_unicode

#     return jsonify({"return_state": return_state()})


# @app.route("/raw", methods=["GET"])
# def board_state_raw():

#     return_state = chesslogic.current_state_raw

#     return jsonify({"return_state": return_state()})



# @app.route("/newgame", methods=["POST"])
# def new_game():

#     #movedetection.reset_physical_state()
#     return_state = chesslogic.start_new_game

#     return jsonify({"return_state": return_state()})



# @app.route("/api", methods=["POST"])
# def board_state():
#     data = request.get_json()

#     if 'board_occupation' not in data:
#         return jsonify({"message": "Missing board_occupation"}), 400
    
#     return_state = chesslogic.legal_moves(data.get('board_occupation'))

#     return jsonify({"return_state": return_state})



# @app.route("/change", methods=["POST"])
# def state_change():
#     data = request.get_json()

#     if 'board_occupation' not in data:
#         return jsonify({"message": "Missing board_occupation"}), 400
    
#     return_state = move_detection.state_change_detector(data.get('board_occupation'))

#     return jsonify({"return_state": return_state})





# ALL THE NEW GLORY
initial_state = "1,1,1,1,1,1,1,1/1,1,1,1,1,1,1,1/0,0,0,0,0,0,0,0/0,0,0,0,0,0,0,0/0,0,0,0,0,0,0,0/0,0,0,0,0,0,0,0/1,1,1,1,1,1,1,1/1,1,1,1,1,1,1,1"
m = MoveDetection(8, initial_state)

@app.route('/update_matrix', methods=['POST'])
def update_matrix():
    data = request.get_json()
    input_str = data.get('board_occupation')
    if input_str:
        m.parse_input(input_str)
        changes = m.state_change_detector()
        return jsonify({'message': "Matrix updated successfully.", 'changes': changes}), 200
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

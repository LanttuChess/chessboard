import chesslogic.chesslogic as chesslogic
from movedetection.MoveDetection import MoveDetection


# Format the list of legal moves to color hex codes for the chessboard to display the legal moves
def format_legal_moves():
    board = chesslogic.get_board_with_legal_moves(chesslogic.board)
    rgb_data = board.replace('0', '000000')
    rgb_data = rgb_data.replace('1', '0000FF').replace(
        ",", "").replace("/", "")

    return rgb_data

# Make a change to the board state. If identified as a move, then ask the chesslogic if it was a legal move, and if it was, make it.


def make_move(m, input_str):
    m.parse_input(input_str)
    changes, special_cases = m.state_change_detector()
    move_results = []
    for case in special_cases:
        (x_source, y_source), (x_dest, y_dest) = case
        result = chesslogic.make_move(x_source, y_source, x_dest, y_dest)
        move_results.append(result)
    return changes, move_results

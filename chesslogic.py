import chess

board = chess.Board()


def start_new_game():
    board.reset()

    return current_state_unicode()

def current_state_fen():
     
    board_state_string = board.fen ()

    return board_state_string


def current_state_unicode():

    board_state_string = str(board)

    return board_state_string


def current_state_raw():

    board_state_string = current_state_unicode()
    binary_board = []

    for i in board_state_string:
        if i == '.':
            binary_board.append('0')
        elif i.isalnum():
            binary_board.append('1')
        else:
            binary_board.append(i)

    return ''.join(binary_board)



def legal_moves(input_string):
     
     legal_moves_list = list(board.legal_moves)

     legal_moves_string = ' '.join(move.uci() for move in legal_moves_list)

     return legal_moves_string
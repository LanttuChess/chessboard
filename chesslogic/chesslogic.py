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



def legal_moves():
     
     legal_moves_list = list(board.legal_moves)

     legal_moves_string = ' '.join(move.uci() for move in legal_moves_list)

     return legal_moves_string




def get_pieces_with_legal_moves_coord(board):
    pieces_with_legal_moves = set()
    for move in board.legal_moves:
        source_square = move.from_square
        coord = (chess.square_rank(source_square), chess.square_file(source_square))
        pieces_with_legal_moves.add(coord)
    return pieces_with_legal_moves


def get_board_with_legal_moves(board):
    # Initialize an empty 8x8 matrix with 2's
    legal_moves_matrix = [[0 for _ in range(8)] for _ in range(8)]
    legal_moves = board.legal_moves

    # Loop through each legal move
    for move in legal_moves:
        # Get the coordinates of the piece that can make the legal move
        piece_x, piece_y = chess.square_file(move.from_square), chess.square_rank(move.from_square)
        # Set the value of that coordinate to 1 in the matrix
        legal_moves_matrix[piece_y][piece_x] = 1

    # Convert the 2D matrix to a string in the required format
    legal_moves_string = "/".join([",".join(map(str, row)) for row in legal_moves_matrix])

    return legal_moves_string






def make_move(y_source, x_source, y_destination, x_destination):
    # Convert coordinates to square indices
    source_square = chess.square(x_source, y_source)
    destination_square = chess.square(x_destination, y_destination)

    # Print the board and legal moves
    print(board)
    print(list(board.legal_moves))

    # Make the move by updating the board state
    move = chess.Move(source_square, destination_square)
    if move in board.legal_moves:
        board.push(move)
        return True
    else:
        print(f"Invalid move: {board.san(move)}")
        print(f"Coords: {x_source, y_source}, {x_destination, y_destination}")
        return False





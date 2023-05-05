import chess

board = chess.Board()

def legal_moves(input_string):
     
     legal_moves_list = list(board.legal_moves)

     legal_moves_string = ' '.join(move.uci() for move in legal_moves_list)

     return legal_moves_string
from enum import Enum, auto

import chess
import chesslogic

class PhysicalState(Enum):
    NO_PIECE_PICKED = auto()
    ONE_PIECE_PICKED = auto()
    TWO_PIECES_PICKED = auto()

class ChangeState(Enum):
    NO_CHANGE = auto()
    ADDED_PIECE = auto()
    REMOVED_PIECE = auto()
    ILLEGAL = auto()


def format_occupancy_data(input_string):
    return [list(map(int, row.split(','))) for row in input_string.split('/')]





current_physical_state = PhysicalState.NO_PIECE_PICKED
current_picked_piece = (None, None, (None, None)) # (piece_type, color, location)
current_occupancy_data = format_occupancy_data("1,1,1,1,1,1,1,1/1,1,1,1,1,1,1,1/0,0,0,0,0,0,0,0/0,0,0,0,0,0,0,0/0,0,0,0,0,0,0,0/0,0,0,0,0,0,0,0/1,1,1,1,1,1,1,1/1,1,1,1,1,1,1,1")



def reset_physical_state():
    current_physical_state = PhysicalState.NO_PIECE_PICKED
    current_occupancy_data = format_occupancy_data("1,1,1,1,1,1,1,1/1,1,1,1,1,1,1,1/0,0,0,0,0,0,0,0/0,0,0,0,0,0,0,0/0,0,0,0,0,0,0,0/0,0,0,0,0,0,0,0/1,1,1,1,1,1,1,1/1,1,1,1,1,1,1,1")



def state_change_detector(input_string):
    new_occupancy_data = format_occupancy_data(input_string)

    comparision, location = compare_occupancy_data(current_occupancy_data, new_occupancy_data)

    print(f"comparision: {comparision}, location: {location}")


    if comparision == ChangeState.NO_CHANGE:
        print("")
        # do nothing
    elif comparision == ChangeState.ADDED_PIECE:
        print("Added piece at: ", location)
        # complete move

        if current_physical_state == PhysicalState.ONE_PIECE_PICKED:
            # complete move
            print("complete move")
        elif current_physical_state == PhysicalState.TWO_PIECES_PICKED:
            # complete move
            print("complete move, with two pieces picked")
        else:
            # error
            print("error")


    elif comparision == ChangeState.REMOVED_PIECE:
        print("Removed piece at: ", location)
        # either begin move, or secondary effect

        if current_physical_state == PhysicalState.NO_PIECE_PICKED:
            # begin move
            print("begin move")

            piece = chesslogic.board.piece_at(chess.square(*location))
            print(piece)

        elif current_physical_state == PhysicalState.ONE_PIECE_PICKED:
            # either capture or castling
            print("capture or castling")
        else:
            # error
            print("error")

    elif comparision == ChangeState.ILLEGAL:
        print("Illegal")
        # do nothing, return error


    return "Pass"



def compare_occupancy_data(current, new):
    added_pieces = []
    removed_pieces = []

    for row in range(8):
        for col in range(8):
            if current[row][col] != new[row][col]:
                if new[row][col] == 1:
                    added_pieces.append((row, col))
                else:
                    removed_pieces.append((row, col))
    
    if not added_pieces and not removed_pieces:
        return (ChangeState.NO_CHANGE, None)
    elif len(added_pieces) == 1 and not removed_pieces:
        location = added_pieces[0]
        return (ChangeState.ADDED_PIECE, location)
    elif len(removed_pieces) == 1 and not added_pieces:
        location = removed_pieces[0]
        return (ChangeState.REMOVED_PIECE, location)
    else:
        return (ChangeState.ILLEGAL, None)
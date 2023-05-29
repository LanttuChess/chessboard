## Chessboard IoT project

This project presents an Intelligent Chessboard IoT project. It uses ESP32 to
connect to a Flask service run atop Digitalocean app platform. ESP32 interacts
with a physical chessboard to retrieve changes in the chess board. The system is
part of Aalto University Sähköpaja freshman course.

ESP32 board reads inputs from a chessboard and sends them to this server, and
then server returns the list of legal positions for a piece.

## Endpoints

Here are the RESTful endpoints exposed by this chess service:

# Method: GET

Path: /

Description: Root endpoint that displays a welcome message.

# Method: GET

Path: /fen

Description: Returns the current state of the chessboard in FEN (Forsyth-Edwards
Notation) format.

# Method: GET

Path: /unicode

Description: Returns the current state of the chessboard in Unicode format.

# Method: GET

Path: /raw

Description: Returns the current state of the chessboard in a binary occupation
format.

# Method: POST

Path: /newgame

Description: Starts a new game on the chessboard and resets both the chessboard
and the MoveDetection instance.

# Method: POST

Path: /change

Description: Updates the current state of the chessboard according to the
received board_occupation data, validates the move, and returns the new state of
the chessboard, along with an RGB data string for the LED display. If no data or
incorrect data is provided, it returns an error message and the current RGB data
string.

# Method: GET

Path: /detect_changes

Description: Returns the detected changes on the chessboard.

# Method: GET

Path: /get_matrix

Description: Returns the current binary state of the chessboard, where the
server thinks the piecis are. This is mostly used for debugging.

# Method: GET

Path: /get_change_sum

Description: Returns the sum of the changes detected on the chessboard. This is
mostly used for debugging.

# Method: GET

Path: /get_positions_with_pieces

Description: Returns the current positions of the pieces on the chessboard along
with the RGB data string for the LED display. Yellow marks the places where
pieces are supposed to be on the physical board.

# Method: GET

Path: /pieces_with_legal_moves

Description: Returns the list of pieces with legal moves, and their coordinates.

# Method: GET

Path: /board_with_legal_moves_matrix

Description: Returns the current state of the chessboard with marked legal
moves, along with the RGB data string for the LED display. Blue marks the places
where is a piece with a possible legal move.

## Forked atop Mason Egger's project

It was originally a code for deploying flask to digitalocean, and this was built
atop his deployment template.

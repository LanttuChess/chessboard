class remove:
    def __init__(self):
        self.previous_state = None
        self.pending_action = None
        self.pending_position = None
        self.capture_position = None

    @staticmethod
    def init_board():
        return [[1]*8 for _ in range(8)] + [[0]*8 for _ in range(4)] + [[1]*8 for _ in range(8)]

    @staticmethod
    def parse_board(board_string):
        return [list(map(int, row.split(','))) for row in board_string.split('/')]

    def state_change_detector(self, board_string):
        current_state = self.parse_board(board_string)

        if self.previous_state is None:
            self.previous_state = current_state
            return 'Initial state set'

        added_pieces = []
        removed_pieces = []

        for i in range(8):
            for j in range(8):
                if current_state[i][j] != self.previous_state[i][j]:
                    if current_state[i][j] == 1:
                        added_pieces.append((i, j))
                    else:
                        removed_pieces.append((i, j))

        if self.pending_action == 'Piece picked up' and len(removed_pieces) == 1 and len(added_pieces) == 1 and removed_pieces == added_pieces:
            self.previous_state = current_state
            self.pending_action = None
            self.pending_position = None
            return 'Move cancelled or promotion made'


        if len(removed_pieces) == 1 and len(added_pieces) == 0:
            self.pending_action = 'Piece picked up'
            self.pending_position = removed_pieces[0]
            return self.pending_action

        if len(removed_pieces) == 2 and len(added_pieces) == 0:
            self.capture_position = removed_pieces[1]  # Store the position of the second removed piece
            return 'Piece captured'

        if len(removed_pieces) == 1 and len(added_pieces) == 1:
            self.pending_action = None
            self.pending_position = None
            return 'Move made'

        if len(removed_pieces) == 1 and len(added_pieces) == 1 and removed_pieces == added_pieces:
            self.pending_action = None
            self.pending_position = None
            return 'Move cancelled or promotion made'

        if len(removed_pieces) == 0 and len(added_pieces) == 0:
            return 'No change detected'

        self.previous_state = self.init_board()  # Reset to the initial state
        return 'Error'



def list_to_string(data):
    return '/'.join(','.join(map(str, row)) for row in data)

class MoveDetection:
    def __init__(self, size, initial_state=None):
        self.size = size
        self.matrix = [[0 for _ in range(size)] for _ in range(size)]
        self.previous_matrix = None
        self.change_sum = 0
        self.minus_position = None
        if initial_state:
            self.parse_input(initial_state)

    def parse_input(self, input_str):
        self.previous_matrix = [row[:] for row in self.matrix]
        rows = input_str.split('/')
        for i, row in enumerate(rows):
            values = row.split(',')
            for j, val in enumerate(values):
                self.matrix[i][j] = int(val)

    def state_change_detector(self):
        if self.previous_matrix is None:
            return None

        changes = [[0 for _ in range(self.size)] for _ in range(self.size)]
        special_cases = []
        for i in range(self.size):
            for j in range(self.size):
                diff = self.matrix[i][j] - self.previous_matrix[i][j]
                if diff > 0:
                    changes[i][j] = 1
                    if self.change_sum < 0:
                        special_cases.append((self.minus_position, (i, j)))
                        self.change_sum = 0
                    else:
                        self.change_sum += 1
                elif diff < 0:
                    changes[i][j] = -1
                    self.change_sum -= 1
                    if self.change_sum == -1:
                        self.minus_position = (i, j)

        return changes, special_cases




    def get_current_matrix(self):
        return self.matrix
    
    def get_positions_with_pieces(self):
        data = self.matrix
        return list_to_string(data)




    def get_change_sum(self):
        return self.change_sum



    def reset(self, initial_state):
        self.matrix = [[0 for _ in range(self.size)] for _ in range(self.size)]
        self.previous_matrix = None
        self.change_sum = 0
        self.minus_position = None
        self.parse_input(initial_state)
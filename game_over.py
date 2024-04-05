class GameOver:
    def __init__(self, field_instance):
        self.field_instance = field_instance

    def is_tie(self):
        for row in self.field_instance.field:
            for value in row:
                if value is None:
                    return False
        message = "Game is a tie"
        print(f"{'*'*len(message)}{message}{'*'*len(message)}")
        return 1

    def check_game(self):
        winning_combinations = [
            # Rows
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            # Columns
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            # Diagonals
            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (1, 1), (2, 0)]
        ]
        # Creates a values list to then check for winning combination
        for combination in winning_combinations:
            values = [self.field_instance.field[row][col] for row, col in combination]
            if all(value == 'X' for value in values):
                return 'Game is won by player'
            elif all(value == 'O' for value in values):
                return 'Game is won by computer'
class Field:
    def __init__(self):
        # the field
        self.field = [[None, None, None],
                      [None, None, None],
                      [None, None, None]]

    # Displays current field in a tic-tac-toe manner
    def show_field(self):
        for row in self.field:
            print('    | '.join([" " if cell is None else cell for cell in row]))
            print("-" * 18)

    # places the symbol when choice is made
    def place_symbol(self, row, col, symbol):
        self.field[row][col] = symbol
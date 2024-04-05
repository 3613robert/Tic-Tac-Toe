class Field:
    def __init__(self):
        self.field = [[None, None, None],
                      [None, None, None],
                      [None, None, None]]

    def show_field(self):
        for row in self.field:
            print('    | '.join([" " if cell is None else cell for cell in row]))
            print("-" * 18)

    def place_symbol(self, row, col, symbol):
        self.field[row][col] = symbol
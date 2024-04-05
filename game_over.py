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
        return True
    def check_game(self):
        if self.field_instance.field[0][0] == 'X' and self.field_instance.field[0][1] == 'X' and self.field_instance.field[0][2] == 'X':
            message = 'Game is won by player'
            print(f"{'*'*len(message)}{message}{'*'*len(message)}")
            return 1
        elif self.field_instance.field[0][0] == 'O' and self.field_instance.field[0][1] == 'O' and self.field_instance.field[0][2] == 'O':
            message = 'Game is won by computer'
            print(f"{'*' * len(message)}{message}{'*' * len(message)}")
            return 1
        if self.field_instance.field[0][0] == 'X' and self.field_instance.field[1][0] == 'X' and self.field_instance.field[2][0] == 'X':
            message = 'Game is won by player'
            print(f"{'*'*len(message)}{message}{'*'*len(message)}")
            return 1
        elif self.field_instance.field[0][0] == 'O' and self.field_instance.field[1][0] == 'O' and self.field_instance.field[2][0] == 'O':
            message = 'Game is won by computer'
            print(f"{'*' * len(message)}{message}{'*' * len(message)}")
            return 1
        if self.field_instance.field[0][0] == 'X' and self.field_instance.field[1][1] == 'X' and self.field_instance.field[2][2] == 'X':
            message = 'Game is won by player'
            print(f"{'*'*len(message)}{message}{'*'*len(message)}")
            return 1
        elif self.field_instance.field[0][0] == 'O' and self.field_instance.field[1][1] == 'O' and self.field_instance.field[2][2] == 'O':
            message = 'Game is won by computer'
            print(f"{'*'*len(message)}{message}{'*'*len(message)}")
            return 1
        if self.field_instance.field[1][0] == 'X' and self.field_instance.field[1][1] == 'X' and self.field_instance.field[1][2] == 'X':
            message = 'Game is won by player'
            print(f"{'*'*len(message)}{message}{'*'*len(message)}")
            return 1
        elif self.field_instance.field[1][0] == 'O' and self.field_instance.field[1][1] == 'O' and self.field_instance.field[1][2] == 'O':
            message = 'Game is won by computer'
            print(f"{'*' * len(message)}{message}{'*' * len(message)}")
            return 1
        if self.field_instance.field[2][0] == 'X' and self.field_instance.field[2][1] == 'X' and self.field_instance.field[2][2] == 'X':
            message = 'Game is won by player'
            print(f"{'*'*len(message)}{message}{'*'*len(message)}")
            return 1
        elif self.field_instance.field[2][0] == 'O' and self.field_instance.field[2][1] == 'O' and self.field_instance.field[2][2] == 'O':
            message = 'Game is won by computer'
            print(f"{'*' * len(message)}{message}{'*' * len(message)}")
            return 1
        if self.field_instance.field[0][2] == 'X' and self.field_instance.field[1][1] == 'X' and self.field_instance.field[2][0] == 'X':
            message = 'Game is won by player'
            print(f"{'*'*len(message)}{message}{'*'*len(message)}")
            return 1
        elif self.field_instance.field[0][2] == 'O' and self.field_instance.field[1][1] == 'O' and self.field_instance.field[2][0] == 'O':
            message = 'Game is won by computer'
            print(f"{'*' * len(message)}{message}{'*' * len(message)}")
            return 1
        if self.field_instance.field[0][1] == 'X' and self.field_instance.field[1][1] == 'X' and self.field_instance.field[2][1] == 'X':
            message = 'Game is won by player'
            print(f"{'*'*len(message)}{message}{'*'*len(message)}")
            return 1
        elif self.field_instance.field[0][1] == 'O' and self.field_instance.field[1][1] == 'O' and self.field_instance.field[2][1] == 'O':
            message = 'Game is won by computer'
            print(f"{'*' * len(message)}{message}{'*' * len(message)}")
            return 1
        if self.field_instance.field[0][2] == 'X' and self.field_instance.field[1][2] == 'X' and self.field_instance.field[2][2] == 'X':
            message = 'Game is won by player'
            print(f"{'*'*len(message)}{message}{'*'*len(message)}")
            return 1
        elif self.field_instance.field[0][2] == 'O' and self.field_instance.field[1][2] == 'O' and self.field_instance.field[2][2] == 'O':
            message = 'Game is won by computer'
            print(f"{'*' * len(message)}{message}{'*' * len(message)}")
            return 1
        self.is_tie()
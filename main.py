from turns import Turns
from field import Field
from game_over import GameOver

field = Field()
game_over = GameOver(field_instance=field)
turns = Turns(field_instance=field)

while True:
    play = input('Do you want to play a game of Tic-Tac-Toe?: \n')
    if play == 'yes':
        for i in range(len(field.field)):
            for j in range(len(field.field[i])):
                field.field[i][j] = None
        while True:
            field.show_field()
            turns.user_turn()
            if game_over.is_tie() == 1:
                break
            else:
                turns.computer_turn()
            winner = game_over.check_game()
            if winner:
                field.show_field()
                print('*' * len(winner), winner, '*' * len(winner))
                break
    if play == 'no':
        break

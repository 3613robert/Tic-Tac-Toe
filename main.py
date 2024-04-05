from turns import Turns
from field import Field
from game_over import GameOver

field = Field()
game_over = GameOver(field_instance=field)
turns = Turns(field_instance=field)

while True:
    field.show_field()
    turns.user_turn()
    if game_over.is_tie() == 1:
        break
    else:
        turns.computer_turn()
    if game_over.check_game() == 1:
        field.show_field()
        break

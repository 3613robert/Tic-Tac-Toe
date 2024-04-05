import random
class Turns:
    def __init__(self, field_instance):
        self.field_instance = field_instance

    # User turn and placement of X based on number corresponding on field
    def user_turn(self):
        while True:
            try:
                user_choice = int(input('Where do you want to place the X? type a number from 1 to 9: \n'))
                if user_choice == 1:
                    if self.field_instance.field[0][0] is None:
                        self.field_instance.place_symbol(0, 0 ,'X')
                        break
                    else:
                        print('Please choose an empty spot')
                elif user_choice == 2:
                    if self.field_instance.field[0][1] is None:
                        self.field_instance.place_symbol(0, 1 ,'X')
                        break
                    else:
                        print('Please choose an empty spot')
                elif user_choice == 3:
                    if self.field_instance.field[0][2] is None:
                        self.field_instance.place_symbol(0, 2 ,'X')
                        break
                    else:
                        print('Please choose an empty spot')
                elif user_choice == 4:
                    if self.field_instance.field[1][0] is None:
                        self.field_instance.place_symbol(1, 0 ,'X')
                        break
                    else:
                        print('Please choose an empty spot')
                elif user_choice == 5:
                    if self.field_instance.field[1][1] is None:
                        self.field_instance.place_symbol(1, 1 ,'X')
                        break
                    else:
                        print('Please choose an empty spot')
                elif user_choice == 6:
                    if self.field_instance.field[1][2] is None:
                        self.field_instance.place_symbol(1, 2 ,'X')
                        break
                    else:
                        print('Please choose an empty spot')
                elif user_choice == 7:
                    if self.field_instance.field[2][0] is None:
                        self.field_instance.place_symbol(2, 0, 'X')
                        break
                    else:
                        print('Please choose an empty spot')
                elif user_choice == 8:
                    if self.field_instance.field[2][1] is None:
                        self.field_instance.place_symbol(2, 1, 'X')
                        break
                    else:
                        print('Please choose an empty spot')
                elif user_choice == 9:
                    if self.field_instance.field[2][2] is None:
                        self.field_instance.place_symbol(2, 2, 'X')
                        break
                    else:
                        print('Please choose an empty spot')
            except ValueError:
                print('Please choose a valid number')

    # Randomly places an O for computer for remaining empty slots
    def computer_turn(self):
        while True:
            user_choice = random.randint(1, 9)
            if user_choice == 1:
                if self.field_instance.field[0][0] is None:
                    self.field_instance.place_symbol(0, 0, 'O')
                    break
            elif user_choice == 2:
                if self.field_instance.field[0][1] is None:
                    self.field_instance.place_symbol(0, 1, 'O')
                    break
            elif user_choice == 3:
                if self.field_instance.field[0][2] is None:
                    self.field_instance.place_symbol(0, 2, 'O')
                    break
            elif user_choice == 4:
                if self.field_instance.field[1][0] is None:
                    self.field_instance.place_symbol(1, 0, 'O')
                    break
            elif user_choice == 5:
                if self.field_instance.field[1][1] is None:
                    self.field_instance.place_symbol(1, 1, 'O')
                    break
            elif user_choice == 6:
                if self.field_instance.field[1][2] is None:
                    self.field_instance.place_symbol(1, 2, 'O')
                    break
            elif user_choice == 7:
                if self.field_instance.field[2][0] is None:
                    self.field_instance.place_symbol(2, 0, 'O')
                    break
            elif user_choice == 8:
                if self.field_instance.field[2][1] is None:
                    self.field_instance.place_symbol(2, 1, 'O')
                    break
            elif user_choice == 9:
                if self.field_instance.field[2][2] is None:
                    self.field_instance.place_symbol(2, 2, 'O')
                    break
            else:
                break

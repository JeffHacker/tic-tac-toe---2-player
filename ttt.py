import os


class Game:
    def __init__(self):
        self.game_board = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
        self.player = 'X'
        self.game_active = True
        self.count = 0
        self.current_play = ''

    def display_board(self):
        os.system("clear")
        print("press 'q' to exit game\n\n  Tic Tac Toe\n")
        print(self.game_board[0:3])
        print(self.game_board[3:6])
        print(self.game_board[6:])

    def x_o_turn(self):
        self.count += 1
        if self.count % 2 == 0:
            self.player = 'O'
        else:
            self.player = 'X'

    def board_update(self):
        self.current_play = input("\nChoose an empty board space (1-9) to place your {}:  ".format(self.player)).lower()
        game.check_input()

    def check_input(self):
        if self.current_play == 'q':
            game.game_exit()
        try:
            if int(self.current_play) in range(1, 10):
                self.current_play = int(self.current_play)
                game.check_play()
            else:
                game.input_error()
        except:
            game.input_error()

    def check_play(self):
        if self.game_board[self.current_play - 1] == '_':
            self.game_board[self.current_play - 1] = self.player
        else:
            game.display_board()
            print('\n!!! That play is already taken !!!')
            game.board_update()

    def input_error(self):
        os.system("clear")
        game.display_board()
        print("\n!!! You may only enter a digit from 1-9 !!!")
        game.board_update()

    def check_board(self):
        win_test = self.player * 3
        if game.game_board[0] + game.game_board[3] + game.game_board[6] == win_test:
            game.game_over()
        elif game.game_board[1] + game.game_board[4] + game.game_board[7] == win_test:
            game.game_over()
        elif game.game_board[2] + game.game_board[5] + game.game_board[8] == win_test:
            game.game_over()
        elif game.game_board[0] + game.game_board[1] + game.game_board[2] == win_test:
            game.game_over()
        elif game.game_board[3] + game.game_board[4] + game.game_board[5] == win_test:
            game.game_over()
        elif game.game_board[6] + game.game_board[7] + game.game_board[8] == win_test:
            game.game_over()
        elif game.game_board[0] + game.game_board[4] + game.game_board[8] == win_test:
            game.game_over()
        elif game.game_board[2] + game.game_board[4] + game.game_board[6] == win_test:
            game.game_over()
        temp = 0
        for _ in game.game_board:
            if _ == "_":
                temp += 1
        if temp == 0:
            self.player = "Cat"
            game.game_over()

    def play_game(self):
        while self.game_active == True:
            game.display_board()
            game.x_o_turn()
            game.board_update()
            game.check_board()

    def game_over(self):
        self.game_active = False
        game.display_board()
        print("\nGAME OVER")
        print("\n{} wins the game".format(self.player))
        input("\nenter to continue")
        os.system("clear")
        game.play_again()

    def play_again(self):
        again = input("Play again? Enter 'Y'es or just Enter to quit:  ").lower()
        if again[0] == 'y':
            self.game_board = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
            self.player = 'X'
            self.game_active = True
            self.count = 0
            game.play_game()
        else:
            os.system("clear")

    def game_exit(self):
        os.system("clear")
        input("Game cancelled. Enter")
        os.system("clear")
        os.system(exit())

game = Game()
game.play_game()

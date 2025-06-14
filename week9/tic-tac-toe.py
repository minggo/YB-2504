class TicTacToe:
    def __init__(self):
        self.board = ['', '', '',
         '', '', '',
         '', '', '']

        # 0: X
        # 1: O
        self.current_player = 0
        self.input_time = 0

    def new_game(self):
        for i in range(9):
            self.board[i] = ''

        self.input_time = 0

    def print_line(self, line):
        base = line * 3
        for i in range(base, base + 3):
            if (self.board[i] == ''):
                print(' ', end=" ")
            else:
                print(self.board[i], end=" ")

        print('')

    def print_board(self):
        self.print_line(0)
        self.print_line(1)
        self.print_line(2)

    def change_player(self):
        self.current_player = 1 - self.current_player

    def get_player_symbol(self):
        return 'X' if self.current_player == 0 else 'O'


    def check_same(self, pos0, pos1, pos2):
        return (self.board[pos0] != '' and
                self.board[pos0] == self.board[pos1] == self.board[pos2])

    def check_winner(self) -> bool:
        return (
            self.check_same(0, 1, 2) or
            self.check_same(3, 4, 5) or
            self.check_same(6, 7, 8) or
            self.check_same(0, 3, 6) or
            self.check_same(1, 4, 7) or
            self.check_same(2, 5, 8) or
            self.check_same(0, 4, 8) or
            self.check_same(2, 4, 6)
        )

    def get_input(self):
        while(True):
            try:
                pos = int(input('Where to place the piece(0 to 8): '))
                if pos < 0 or pos > 8 or self.board[pos] != '':
                    print('invalid input')
                    continue
                
                self.board[pos] = self.get_player_symbol()
                self.input_time += 1
                self.print_board()
                self.change_player()
                return
            except Exception as e:
                print('invalid input ', e)

    def start(self):
        while (True):
          self.get_input()
          if (self.check_winner()):
              print(f'The winner is {self.get_player_symbol()}')
              print('Start a new game.')
              self.new_game()

          if (self.input_time == 9):
              print('no one win')
              print('Start a new game.')
              self.new_game()

if __name__ == "__main__":
    game = TicTacToe()
    game.start()
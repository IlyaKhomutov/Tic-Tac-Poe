import sys


# Model
class Board:
    def __init__(self):
        self.size = int(input("Введите размерность вашего поля(одно число): "))
        self.field = []
        self.horizontal_check = []
        self.vertical_check = []
        self.first_diagonal_check = []
        self.second_diagonal_check = []
        for i in range(self.size):
            self.field.append(['*'] * self.size)
        self.win = [['0'] * self.size, ['x'] * self.size]

    def check(self):
        self.first_diagonal_check = []
        self.second_diagonal_check = []

        for i in range(self.size):
            self.horizontal_check = []
            self.vertical_check = []
            self.second_diagonal_check.append(self.field[i][-i-1])

            for j in range(self.size):
                self.horizontal_check.append(self.field[i][j])
                self.vertical_check.append(self.field[j][i])
                if i == j:
                    self.first_diagonal_check.append(self.field[i][j])
            if (self.horizontal_check in self.win) or (self.vertical_check in self.win) or \
                    (self.first_diagonal_check in self.win) or \
                    (self.second_diagonal_check in self.win):
                print("Игра закончена!")
                sys.exit()


# View
class BoardView:
    @staticmethod
    def show_board(board):
        for line in board.field:
            print(line, end='\n')


# Controller
class Turn:

    def __init__(self, board):
        self.board = board
        self.symbol = None
        self.goryzontal_coord = None
        self.vertical_coord = None
        self.count_turns = 0
        self.all_turns = []

    def play(self):
        if self.count_turns % 2 == 0:
            self.symbol = 'x'
        elif self.count_turns % 2 != 0:
            self.symbol = '0'
        print(f"Сейчас ходит {self.symbol}:")
        self.goryzontal_coord = input("Введите ряд: ")
        self.vertical_coord = input("Введите столбец: ")
        if [str(int(self.goryzontal_coord) - 1), str(int(self.vertical_coord) - 1)] in self.all_turns:
            print("Вы нарушили правила игра! Игра закончена")
            return False
        self.all_turns.append([str(int(self.goryzontal_coord) - 1), str(int(self.vertical_coord) - 1)])
        self.count_turns += 1
        try:
            self.board.field[int(self.goryzontal_coord) - 1][int(self.vertical_coord) - 1] = self.symbol
        except IndexError:
            print("Вы ввели неправильные данные! ")
            self.count_turns -= 1

        BoardView.show_board(self.board)
        self.board.check()

        test_lst = []
        for lst in self.board.field:
            for symbol in lst:
                test_lst.append(symbol)
        if '*' not in test_lst:
            print("Ничья!")
            sys.exit()


if __name__ == "__main__":
    my_board = Board()
    BoardView.show_board(my_board)
    my_turn = Turn(my_board)
    while True:
        my_turn.play()

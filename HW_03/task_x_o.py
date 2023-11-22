"""
Задача:
Написать игру в “Крестики-нолики”. Можете использовать
любые парадигмы, которые посчитаете наиболее
подходящими. 
"""

"""
При решении данной задачи использовалась объектно-ориентированная парадигма
Методы классов реализованы с помощью структурной парадигмы
Вызов программы для проверки работы кода (if __name__ == '__main__'), реализован в процедурной парадигме
"""


class Board:
    def __init__(self):
        self._cells = [' ' for _ in range(9)]
    
    def display(self):
        print(f'{self._cells[0]} | {self._cells[1]} | {self._cells[2]}')
        print('---------')
        print(f'{self._cells[3]} | {self._cells[4]} | {self._cells[5]}')
        print('---------')
        print(f'{self._cells[6]} | {self._cells[7]} | {self._cells[8]}')

    def get_cell(self, n):
        return self._cells[n]
    
    def set_cell(self, n, symbol):
        self._cells[n] = symbol

    def get_board(self):
        return self._cells

class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
 
    def make_move(self, board: Board):
        while True:
            cell = input(f'{self.name}, введите номер клетки (1-9): ')
            if cell.isdigit() and 1 <= int(cell) <= 9:
                cell = int(cell) - 1
                if board.get_cell(cell) == ' ':
                    board.set_cell(cell, self.symbol)
                    break
                else:
                    print('Клетка занята. Попробуйте другую.')
            else:
                print('Некорректный ввод. Попробуйте еще раз.')

class TicTacToe:
    def __init__(self, name_1, name_2):
        self.player_1 = Player(name_1, 'X')
        self.player_2 = Player(name_2, 'O')
        self.board = Board()
 
    def play(self):
        current_player = self.player_1
        self.board.display()
        while True:
            current_player.make_move(self.board)
            self.board.display()
            if self.check_winner(current_player):
                print(f'{current_player.name} победил!')
                break
            elif self.check_draw():
                print('Ничья!')
                break
            current_player = self.player_2 if current_player == self.player_1 else self.player_1
 
    def check_winner(self, player: Player):
        winning_combinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        for combination in winning_combinations:
            if all(self.board.get_cell(cell) == player.symbol for cell in combination):
                return True
        return False
 
    def check_draw(self):
        return all(cell != ' ' for cell in self.board.get_board())
    
if __name__ == '__main__':
    flag = True
    while flag:
        print("Начать игру? для ответа введите число: да - 1, нет - 0")
        answer = input()
        if answer.isdigit():
            if int(answer) == 1:
                name_1 = input('Введите имя 1 игрока ')
                name_2 = input('Введите имя 2 игрока ')
                print('Игра началась!')
                game = TicTacToe(name_1, name_2)
                game.play()
            elif int(answer) == 0:
                flag = False
            else:
                print('Введите 1 или 0')
        else:
            print('Введите 1 или 0')
        
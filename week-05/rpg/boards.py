import floor
import wall

class Boards(object):

    def __init__(self):
        self.level = 1
        self.input = 'level{}.txt'
        self.board = []
        self.set_board()

    def get_file_name(self):
        return self.input.format(str(self.level).zfill(3))

    def get_pattern(self):
        pattern = []
        try:
            with open(self.get_file_name()) as file:
                pattern = file.read().split('\n')
        except FileNotFoundError:
            pattern.append('')
        return pattern

    def set_board(self):
        pattern = self.get_pattern()
        for i in range(len(pattern)):
            self.board.append([])
            for j in range(len(pattern[0])):
                if pattern[i][j] == '0':
                    self.board[i].append(floor.Floor(i, j))
                elif pattern[i][j] == '1':
                    self.board[i].append(wall.Wall(i, j))
    
    def get_board(self):
        return self.board

    def get_max_col(self):
        return len(self.board[0])
    
    def get_max_row(self):
        return len(self.board)  



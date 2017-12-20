class Boards(object):

    def __init__(self):
        self.level = 1
        self.input = 'level{}.txt'
        self.board = []
        self.set_board()

    def get_file_name(self):
        return self.input.format(str(self.level).zfill(3))

    def set_board(self):
        try:
            with open(self.get_file_name()) as file:
                self.board = file.read().split('\n')
        except FileNotFound:
            self.board.append('')
    
    def get_board(self):
        return self.board

    def get_max_col(self):
        return len(self.board[0])
    
    def get_max_row(self):
        return len(self.board)  



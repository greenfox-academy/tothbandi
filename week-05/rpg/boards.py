class Boards(object):

    def __init__(self):
        self.level = 1
        self.input = 'level{}.txt'
        self.board = []
        self.get_board()

    def get_file_name(self):
        return self.input.format(str(self.level).zfill(3))

    def get_board(self):
        try:
            with open(self.get_file_name()) as file:
                self.board = file.read().split('\n')
            # return board
        except FileNotFound:
            return ''

    def get_row(self): # boardba
        return len(self.board[0])
    
    def get_col(self): # boardba
        return len(self.board)    

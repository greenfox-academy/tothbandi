class Boards(object):

    def __init__(self):
        self.level = 1
        self.input = 'level{}.txt'

    def get_file_name(self):
        return self.input.format(str(self.level).zfill(3))

    def get_board(self):
        board = []
        try:
            with open(self.get_file_name()) as file:
                board = file.read().split('\n')
            return board
        except FileNotFound:
            return ''
        

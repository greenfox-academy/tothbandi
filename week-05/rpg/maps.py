class Maps(object):

    def __init__(self):
        self.level = 1
        self.input = 'level{}.txt'

    def get_level(self):
        return self.input.format(str(self.level).zfill(3))

    def get_map(self):
        a_map = []
        try:
            with open(self.get_level()) as file:
                a_map = file.read().split('\n')
            return a_map
        except FileNotFound:
            return ''
        

class Map(object):

    def __init__(self):
        self.level = 1
        self.input = 'level{}.txt'

        def get_level(self):
            return self.input.format(str(self.level).zfill(3))

        def get_map(self):
            self.get_level()
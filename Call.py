class Call:
    def __init__(self, name, time, src, dest, status, index):
        self.name = name
        self.time = time
        self.src = src
        self.dest = dest
        self.status = status
        self.index = index

    def setIndex(self, index):
        self.index = index

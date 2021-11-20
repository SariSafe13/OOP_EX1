class Building:
    def __init__(self, _minFloor, _maxFloor, eles):
        self._minFloor = _minFloor
        self._maxFloor = _maxFloor
        self.eles = eles

    def getlist(self):
        return self.eles

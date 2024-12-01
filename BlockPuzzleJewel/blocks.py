from block import Block
from position import Position


class LBlock(Block):
    def __init__(self, cell_size):
        super().__init__(id=1, cell_size=cell_size)
        self.cells = [Position(0, 2), Position(1, 0), Position(1, 1), Position(1, 2)]

    def __repr__(self):
        return str(self.id)


class JBlock(Block):
    def __init__(self, cell_size):
        super().__init__(id=2, cell_size=cell_size)
        self.cells = [Position(0, 0), Position(1, 0), Position(1, 1), Position(1, 2)]

    def __repr__(self):
        return str(self.id)


class IBlock(Block):
    def __init__(self, cell_size):
        super().__init__(id=3, cell_size=cell_size)
        self.cells = [Position(0, 0), Position(0, 1), Position(0, 2), Position(0, 3)]

    def __repr__(self):
        return str(self.id)


class OBlock(Block):
    def __init__(self, cell_size):
        super().__init__(id=4, cell_size=cell_size)
        self.cells = [Position(0, 0), Position(0, 1), Position(1, 0), Position(1, 1)]

    def __repr__(self):
        return str(self.id)


class SBlock(Block):
    def __init__(self, cell_size):
        super().__init__(id=5, cell_size=cell_size)
        self.cells = [Position(0, 1), Position(0, 2), Position(1, 0), Position(1, 1)]

    def __repr__(self):
        return str(self.id)


class TBlock(Block):
    def __init__(self, cell_size):
        super().__init__(id=6, cell_size=cell_size)
        self.cells = [Position(0, 1), Position(1, 0), Position(1, 1), Position(1, 2)]

    def __repr__(self):
        return str(self.id)


class ZBlock(Block):
    def __init__(self, cell_size):
        super().__init__(id=7, cell_size=cell_size)
        self.cells = [Position(0, 0), Position(0, 1), Position(1, 1), Position(1, 2)]

    def __repr__(self):
        return str(self.id)


class FullBlock(Block):
    def __init__(self, cell_size):
        super().__init__(id=8, cell_size=cell_size)
        self.cells = [Position(0, 0), Position(0, 1), Position(0, 2), Position(1, 0),
                      Position(1, 1), Position(1, 2), Position(2, 0), Position(2, 1),
                      Position(2, 2)]

    def __repr__(self):
        return str(self.id)


class CornerBlock(Block):
    def __init__(self, cell_size):
        super().__init__(id=9, cell_size=cell_size)
        self.cells = [Position(0, 0), Position(0, 1), Position(1, 0)]

    def __repr__(self):
        return str(self.id)


class BigCornerBlock(Block):
    def __init__(self, cell_size):
        super().__init__(id=10, cell_size=cell_size)
        self.cells = [Position(0, 0), Position(0, 1), Position(0, 2), Position(1, 0), Position(2, 0)]

    def __repr__(self):
        return str(self.id)


class ThreeBlock(Block):
    def __init__(self, cell_size):
        super().__init__(id=11, cell_size=cell_size)
        self.cells = [Position(0, 0), Position(0, 1), Position(0, 2)]

    def __repr__(self):
        return str(self.id)


class TwoBlock(Block):
    def __init__(self, cell_size):
        super().__init__(id=12, cell_size=cell_size)
        self.cells = [Position(0, 0), Position(1, 0)]

    def __repr__(self):
        return str(self.id)


class OneBlock(Block):
    def __init__(self, cell_size):
        super().__init__(id=13, cell_size=cell_size)
        self.cells = [Position(0, 0)]

    def __repr__(self):
        return str(self.id)

from figures.figure import Color


class Game:
    @staticmethod
    def _init_figures():
        return []

    def __init__(self):
        self.figures = []
        self.is_black_did_castling = self._init_figures()
        self.is_white_did_castling = False
        self.move_color = Color.white
        self.has_check = False
        self.has_mate = False

    def show(self):
        pass
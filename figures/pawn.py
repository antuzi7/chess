from figures.figure import Figure



class Pawn(Figure):

    def _check_board(self, x, y):
        if x > 8 or x < 1 or y > 8 or y < 8:
            return False
        return True

    def _check_pawn_moves(self, x, y):
        if y - self.y == 1 and self.x == x:
            return True
        return False

    def _check_other_figures(self, x, y):
        pass

    def _check(self, x, y):
        if self._check_board(x, y) and self._check_other_figures(x, y) and self._check_pawn_moves(x, y):
            return True
        return False

    def move(self, x, y):
        self.x = x
        self.y = y
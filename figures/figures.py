from abc import ABC
from enum import Enum


class Color(Enum):
    white = 1
    black = 2


class Figure(ABC):
    def __int__(self, x, y):
        self.x = x
        self.y = y


    @abstactmethod
    def move(self, x, y):
        pass
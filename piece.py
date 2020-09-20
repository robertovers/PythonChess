
from abc import ABC, abstractmethod
import pygame


class Piece(ABC):
    # 0 = white, 1 = black

    def __init__(self, colour, x, y):
        self.colour = colour
        self.x = x
        self.y = y

        self.type = None
        self.sprite = None
        self.sprite_ld = None

    def get_sprite(self):
        sprite_file = open(self.sprite)
        sprite = pygame.image.load(sprite_file)
        sprite = pygame.transform.scale(sprite, (60, 60))
        sprite_file.close()
        return sprite


class Pawn(Piece):

    def __init__(self, colour, x, y):
        Piece.__init__(self, colour, x, y)

        if self.colour == 0:
            self.sprite = "pieces/w_pawn.png"
        elif self.colour == 1:
            self.sprite = "pieces/b_pawn.png"

        self.sprite_ld = self.get_sprite()
        self.type = Pawn


class Rook(Piece):

    def __init__(self, colour, x, y):
        Piece.__init__(self, colour, x, y)

        if self.colour == 0:
            self.sprite = "pieces/w_rook.png"
        elif self.colour == 1:
            self.sprite = "pieces/b_rook.png"

        self.sprite_ld = self.get_sprite()
        self.type = Rook


class Knight(Piece):

    def __init__(self, colour, x, y):
        Piece.__init__(self, colour, x, y)

        if self.colour == 0:
            self.sprite = "pieces/w_knight.png"
        elif self.colour == 1:
            self.sprite = "pieces/b_knight.png"

        self.sprite_ld = self.get_sprite()
        self.type = Knight


class Bishop(Piece):

    def __init__(self, colour, x, y):
        Piece.__init__(self, colour, x, y)

        if self.colour == 0:
            self.sprite = "pieces/w_bishop.png"
        elif self.colour == 1:
            self.sprite = "pieces/b_bishop.png"

        self.sprite_ld = self.get_sprite()
        self.type = Bishop


class Queen(Piece):

    def __init__(self, colour, x, y):
        Piece.__init__(self, colour, x, y)

        if self.colour == 0:
            self.sprite = "pieces/w_queen.png"
        elif self.colour == 1:
            self.sprite = "pieces/b_queen.png"

        self.sprite_ld = self.get_sprite()
        self.type = Queen


class King(Piece):

    def __init__(self, colour, x, y):
        Piece.__init__(self, colour, x, y)

        if self.colour == 0:
            self.sprite = "pieces/w_king.png"
        elif self.colour == 1:
            self.sprite = "pieces/b_king.png"

        self.sprite_ld = self.get_sprite()
        self.type = King

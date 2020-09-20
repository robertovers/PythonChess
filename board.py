
import pygame
from piece import Pawn, Rook, Knight, Bishop, Queen, King


class Board:

    def __init__(self, display):
        self.display = display
        self.last_move = None
        self.w_king = None, None
        self.b_king = None, None

        self.squares = [[None, None, None, None, None, None, None, None],
                        [None, None, None, None, None, None, None, None],
                        [None, None, None, None, None, None, None, None],
                        [None, None, None, None, None, None, None, None],
                        [None, None, None, None, None, None, None, None],
                        [None, None, None, None, None, None, None, None],
                        [None, None, None, None, None, None, None, None],
                        [None, None, None, None, None, None, None, None]]

        self.create_board()

    def piece_setup(self):
        for i in [0, 1]:
            for k in range(8):
                self.place(Pawn(0, k, 6))
                self.place(Pawn(1, k, 1))

            if i == 0:
                j = 7
            else:
                j = 0

            self.place(Rook(i, 0, j))
            self.place(Rook(i, 7, j))

            self.place(Knight(i, 1, j))
            self.place(Knight(i, 6, j))

            self.place(Bishop(i, 2, j))
            self.place(Bishop(i, 5, j))

            self.place(Queen(i, 3, j))
            self.place(King(i, 4, j))

            self.move_stack = []

    def place(self, piece):

        if type(piece) == Pawn:
            if piece.colour == 0 and piece.y == 0:
                self.squares[piece.x][piece.y] = Queen(0, piece.x, piece.y)
            elif piece.colour == 1 and piece.y == 7:
                self.squares[piece.x][piece.y] = Queen(1, piece.x, piece.y)
            else:
                self.squares[piece.x][piece.y] = piece
        elif type(piece) == King:
            if piece.colour == 0:
                self.w_king = piece.x, piece.y
            else:
                self.b_king = piece.x, piece.y
            self.squares[piece.x][piece.y] = piece
        else:
            self.squares[piece.x][piece.y] = piece

    def print(self, piece):
        self.display.blit(piece.sprite_ld, (56 * piece.x - 2, 56 * piece.y - 2))

    def clear(self, x, y):
        self.squares[x][y] = None

    def print_pieces(self):
        for row in self.squares:
            for piece in row:
                if piece:
                    self.print(piece)

    def create_board(self):
        for i in range(8):
            for j in range(8):
                if i % 2 == 0 and j % 2 == 1 or j % 2 == 0 and i % 2 == 1:
                    display_square(self.display, "dark", i, j)
                else:
                    display_square(self.display, "light", i, j)

    def print_moves(self, piece):
        for move in self.get_moves(piece):
            pygame.draw.circle(self.display, [0, 100, 250], (move[0] * 56 + 56//2, move[1] * 56 + 56//2), 4)

    def get_moves(self, piece):
        moves = []

        if type(piece) == Pawn:

            if piece.colour == 0:
                if 0 <= (piece.y - 1) < 8 and self.squares[piece.x][piece.y - 1] is None:
                    moves += [(piece.x, piece.y - 1)]
                if piece.y == 6 and self.squares[piece.x][piece.y - 1] is None and self.squares[piece.x][piece.y - 2] is None:
                    moves += [(piece.x, piece.y - 2)]
                if 0 <= (piece.y - 1) < 8:
                    for i in [-1, 1]:
                        if 0 <= (piece.x + i) < 8:
                            if self.squares[piece.x + i][piece.y - 1] and self.squares[piece.x + i][piece.y - 1].colour == 1:
                                moves += [(piece.x + i, piece.y - 1)]

            else:
                if 0 <= (piece.y + 1) < 8 and self.squares[piece.x][piece.y + 1] is None:
                    moves += [(piece.x, piece.y + 1)]
                if piece.y == 1 and self.squares[piece.x][piece.y + 1] is None and self.squares[piece.x][piece.y + 2] is None:
                    moves += [(piece.x, piece.y + 2)]
                if 0 <= (piece.y + 1) < 8:
                    for i in [-1, 1]:
                        if 0 <= (piece.x + i) < 8:
                            if self.squares[piece.x + i][piece.y + 1] and self.squares[piece.x + i][piece.y + 1].colour == 0:
                                moves += [(piece.x + i, piece.y + 1)]

        elif type(piece) == Rook:

            i = 1
            while 0 <= (piece.y + i) < 8 and self.squares[piece.x][piece.y + i] is None:
                moves += [(piece.x, piece.y + i)]
                i += 1

            if 0 <= (piece.y + i) < 8:
                blocker = self.squares[piece.x][piece.y + i]
                if blocker:
                    if piece.colour == 0:
                        if blocker.colour == 1:
                            moves += [(blocker.x, blocker.y)]
                    elif piece.colour == 1:
                        if blocker.colour == 0:
                            moves += [(blocker.x, blocker.y)]

            i = 1
            while 0 <= (piece.y - i) < 8 and self.squares[piece.x][piece.y - i] is None:
                moves += [(piece.x, piece.y - i)]
                i += 1

            if 0 <= (piece.y - i) < 8:
                blocker = self.squares[piece.x][piece.y - i]
                if blocker:
                    if piece.colour == 0:
                        if blocker.colour == 1:
                            moves += [(blocker.x, blocker.y)]
                    elif piece.colour == 1:
                        if blocker.colour == 0:
                            moves += [(blocker.x, blocker.y)]

            i = 1
            while 0 <= (piece.x + i) < 8 and self.squares[piece.x + i][piece.y] is None:
                moves += [(piece.x + i, piece.y)]
                i += 1

            if 0 <= (piece.x + i) < 8:
                blocker = self.squares[piece.x + i][piece.y]
                if blocker:
                    if piece.colour == 0:
                        if blocker.colour == 1:
                            moves += [(blocker.x, blocker.y)]
                    elif piece.colour == 1:
                        if blocker.colour == 0:
                            moves += [(blocker.x, blocker.y)]

            i = 1
            while 0 <= (piece.x - i) < 8 and self.squares[piece.x - i][piece.y] is None:
                moves += [(piece.x - i, piece.y)]
                i += 1

            if 0 <= (piece.x - i) < 8:
                blocker = self.squares[piece.x - i][piece.y]
                if blocker:
                    if piece.colour == 0:
                        if blocker.colour == 1:
                            moves += [(blocker.x, blocker.y)]
                    elif piece.colour == 1:
                        if blocker.colour == 0:
                            moves += [(blocker.x, blocker.y)]

        elif type(piece) == Knight:

            for i in [2, -2]:
                for j in [1, -1]:

                    if 0 <= (piece.x + i) < 8 and 0 <= (piece.y + j) < 8 and self.squares[piece.x + i][piece.y + j] is None:
                        moves += [(piece.x + i, piece.y + j)]

                    if 0 <= (piece.x + i) < 8 and 0 <= (piece.y + j) < 8:
                        blocker = self.squares[piece.x + i][piece.y + j]
                        if blocker:
                            if piece.colour == 0:
                                if blocker.colour == 1:
                                    moves += [(blocker.x, blocker.y)]
                            elif piece.colour == 1:
                                if blocker.colour == 0:
                                    moves += [(blocker.x, blocker.y)]

                    if 0 <= (piece.x + j) < 8 and 0 <= (piece.y + i) < 8 and self.squares[piece.x + j][piece.y + i] is None:
                        moves += [(piece.x + j, piece.y + i)]

                    if 0 <= (piece.x + j) < 8 and 0 <= (piece.y + i) < 8:
                        blocker = self.squares[piece.x + j][piece.y + i]
                        if blocker:
                            if piece.colour == 0:
                                if blocker.colour == 1:
                                    moves += [(blocker.x, blocker.y)]
                            elif piece.colour == 1:
                                if blocker.colour == 0:
                                    moves += [(blocker.x, blocker.y)]

        elif type(piece) == Bishop:

            i = 1
            while 0 <= (piece.y + i) < 8 and 0 <= (piece.x + i) < 8 and self.squares[piece.x + i][piece.y + i] is None:
                moves += [(piece.x + i, piece.y + i)]
                i += 1

            if 0 <= (piece.y + i) < 8 and 0 <= (piece.x + i) < 8:
                blocker = self.squares[piece.x + i][piece.y + i]
                if blocker:
                    if piece.colour == 0:
                        if blocker.colour == 1:
                            moves += [(blocker.x, blocker.y)]
                    elif piece.colour == 1:
                        if blocker.colour == 0:
                            moves += [(blocker.x, blocker.y)]

            i = 1
            while 0 <= (piece.y - i) < 8 and 0 <= (piece.x - i) < 8 and self.squares[piece.x - i][piece.y - i] is None:
                moves += [(piece.x - i, piece.y - i)]
                i += 1

            if 0 <= (piece.y - i) < 8 and 0 <= (piece.x - i) < 8:
                blocker = self.squares[piece.x - i][piece.y - i]
                if blocker:
                    if piece.colour == 0:
                        if blocker.colour == 1:
                            moves += [(blocker.x, blocker.y)]
                    elif piece.colour == 1:
                        if blocker.colour == 0:
                            moves += [(blocker.x, blocker.y)]

            i = 1
            while 0 <= (piece.x + i) < 8 and 0 <= (piece.y - i) < 8 and self.squares[piece.x + i][piece.y - i] is None:
                moves += [(piece.x + i, piece.y - i)]
                i += 1

            if 0 <= (piece.x + i) < 8 and 0 <= (piece.y - i) < 8:
                blocker = self.squares[piece.x + i][piece.y - i]
                if blocker:
                    if piece.colour == 0:
                        if blocker.colour == 1:
                            moves += [(blocker.x, blocker.y)]
                    elif piece.colour == 1:
                        if blocker.colour == 0:
                            moves += [(blocker.x, blocker.y)]

            i = 1
            while 0 <= (piece.x - i) < 8 and 0 <= (piece.y + i) < 8 and self.squares[piece.x - i][piece.y + i] is None:
                moves += [(piece.x - i, piece.y + i)]
                i += 1

            if 0 <= (piece.x - i) < 8 and 0 <= (piece.y + i) < 8:
                blocker = self.squares[piece.x - i][piece.y + i]
                if blocker:
                    if piece.colour == 0:
                        if blocker.colour == 1:
                            moves += [(blocker.x, blocker.y)]
                    elif piece.colour == 1:
                        if blocker.colour == 0:
                            moves += [(blocker.x, blocker.y)]

        elif type(piece) == Queen:

            i = 1
            while 0 <= (piece.y + i) < 8 and self.squares[piece.x][piece.y + i] is None:
                moves += [(piece.x, piece.y + i)]
                i += 1

            if 0 <= (piece.y + i) < 8:
                blocker = self.squares[piece.x][piece.y + i]
                if blocker:
                    if piece.colour == 0:
                        if blocker.colour == 1:
                            moves += [(blocker.x, blocker.y)]
                    elif piece.colour == 1:
                        if blocker.colour == 0:
                            moves += [(blocker.x, blocker.y)]

            i = 1
            while 0 <= (piece.y - i) < 8 and self.squares[piece.x][piece.y - i] is None:
                moves += [(piece.x, piece.y - i)]
                i += 1

            if 0 <= (piece.y - i) < 8:
                blocker = self.squares[piece.x][piece.y - i]
                if blocker:
                    if piece.colour == 0:
                        if blocker.colour == 1:
                            moves += [(blocker.x, blocker.y)]
                    elif piece.colour == 1:
                        if blocker.colour == 0:
                            moves += [(blocker.x, blocker.y)]

            i = 1
            while 0 <= (piece.x + i) < 8 and self.squares[piece.x + i][piece.y] is None:
                moves += [(piece.x + i, piece.y)]
                i += 1

            if 0 <= (piece.x + i) < 8:
                blocker = self.squares[piece.x + i][piece.y]
                if blocker:
                    if piece.colour == 0:
                        if blocker.colour == 1:
                            moves += [(blocker.x, blocker.y)]
                    elif piece.colour == 1:
                        if blocker.colour == 0:
                            moves += [(blocker.x, blocker.y)]

            i = 1
            while 0 <= (piece.x - i) < 8 and self.squares[piece.x - i][piece.y] is None:
                moves += [(piece.x - i, piece.y)]
                i += 1

            if 0 <= (piece.x - i) < 8:
                blocker = self.squares[piece.x - i][piece.y]
                if blocker:
                    if piece.colour == 0:
                        if blocker.colour == 1:
                            moves += [(blocker.x, blocker.y)]
                    elif piece.colour == 1:
                        if blocker.colour == 0:
                            moves += [(blocker.x, blocker.y)]

            i = 1
            while 0 <= (piece.y + i) < 8 and 0 <= (piece.x + i) < 8 and self.squares[piece.x + i][piece.y + i] is None:
                moves += [(piece.x + i, piece.y + i)]
                i += 1

            if 0 <= (piece.y + i) < 8 and 0 <= (piece.x + i) < 8:
                blocker = self.squares[piece.x + i][piece.y + i]
                if blocker:
                    if piece.colour == 0:
                        if blocker.colour == 1:
                            moves += [(blocker.x, blocker.y)]
                    elif piece.colour == 1:
                        if blocker.colour == 0:
                            moves += [(blocker.x, blocker.y)]

            i = 1
            while 0 <= (piece.y - i) < 8 and 0 <= (piece.x - i) < 8 and self.squares[piece.x - i][piece.y - i] is None:
                moves += [(piece.x - i, piece.y - i)]
                i += 1

            if 0 <= (piece.y - i) < 8 and 0 <= (piece.x - i) < 8:
                blocker = self.squares[piece.x - i][piece.y - i]
                if blocker:
                    if piece.colour == 0:
                        if blocker.colour == 1:
                            moves += [(blocker.x, blocker.y)]
                    elif piece.colour == 1:
                        if blocker.colour == 0:
                            moves += [(blocker.x, blocker.y)]

            i = 1
            while 0 <= (piece.x + i) < 8 and 0 <= (piece.y - i) < 8 and self.squares[piece.x + i][piece.y - i] is None:
                moves += [(piece.x + i, piece.y - i)]
                i += 1

            if 0 <= (piece.x + i) < 8 and 0 <= (piece.y - i) < 8:
                blocker = self.squares[piece.x + i][piece.y - i]
                if blocker:
                    if piece.colour == 0:
                        if blocker.colour == 1:
                            moves += [(blocker.x, blocker.y)]
                    elif piece.colour == 1:
                        if blocker.colour == 0:
                            moves += [(blocker.x, blocker.y)]

            i = 1
            while 0 <= (piece.x - i) < 8 and 0 <= (piece.y + i) < 8 and self.squares[piece.x - i][piece.y + i] is None:
                moves += [(piece.x - i, piece.y + i)]
                i += 1

            if 0 <= (piece.x - i) < 8 and 0 <= (piece.y + i) < 8:
                blocker = self.squares[piece.x - i][piece.y + i]
                if blocker:
                    if piece.colour == 0:
                        if blocker.colour == 1:
                            moves += [(blocker.x, blocker.y)]
                    elif piece.colour == 1:
                        if blocker.colour == 0:
                            moves += [(blocker.x, blocker.y)]

        elif type(piece) == King:

            for i in [-1, 1]:
                for j in [-1, 1]:
                    if 0 <= (piece.x + i) < 8 and 0 <= (piece.y + j) < 8 and self.squares[piece.x + i][piece.y + j] is None:
                        moves += [(piece.x + i, piece.y + j)]

                    if 0 <= (piece.x + i) < 8 and 0 <= (piece.y + j) < 8:
                        blocker = self.squares[piece.x + i][piece.y + j]
                        if blocker:
                            if piece.colour == 0:
                                if blocker.colour == 1:
                                    moves += [(blocker.x, blocker.y)]
                            elif piece.colour == 1:
                                if blocker.colour == 0:
                                    moves += [(blocker.x, blocker.y)]

                if 0 <= (piece.x + i) < 8 and self.squares[piece.x + i][piece.y] is None:
                    moves += [(piece.x + i, piece.y)]

                if 0 <= (piece.x + i) < 8:
                    blocker = self.squares[piece.x + i][piece.y]
                    if blocker:
                        if piece.colour == 0:
                            if blocker.colour == 1:
                                moves += [(blocker.x, blocker.y)]
                        elif piece.colour == 1:
                            if blocker.colour == 0:
                                moves += [(blocker.x, blocker.y)]

                if 0 <= (piece.y + i) < 8 and self.squares[piece.x][piece.y + i] is None:
                    moves += [(piece.x, piece.y + i)]

                if 0 <= (piece.y + i) < 8:
                    blocker = self.squares[piece.x][piece.y + i]
                    if blocker:
                        if piece.colour == 0:
                            if blocker.colour == 1:
                                moves += [(blocker.x, blocker.y)]
                        elif piece.colour == 1:
                            if blocker.colour == 0:
                                moves += [(blocker.x, blocker.y)]

        return moves

    def check(self):
        for row in self.squares:
            for piece in row:
                moves = self.get_moves(piece)
                for m in moves:
                    mx, my = m
                    if type(self.squares[mx][my]) == King:
                        return True
        return False

    def show_check(self, colour):
        if colour == 0:
            sprite_file = open("pieces/w_check.png")
            piece = self.w_king
        else:
            sprite_file = open("pieces/b_check.png")
            piece = self.b_king
        sprite = pygame.image.load(sprite_file)
        sprite = pygame.transform.scale(sprite, (60, 60))
        sprite_file.close()

        self.display.blit(sprite, (56 * piece[0] - 2, 56 * piece[1] - 2))

    def create_copy(self, board):
        new_board = [[None, None, None, None, None, None, None, None],
                     [None, None, None, None, None, None, None, None],
                     [None, None, None, None, None, None, None, None],
                     [None, None, None, None, None, None, None, None],
                     [None, None, None, None, None, None, None, None],
                     [None, None, None, None, None, None, None, None],
                     [None, None, None, None, None, None, None, None],
                     [None, None, None, None, None, None, None, None]]

        for i in range(8):
            for j in range(8):
                piece = board[i][j]

                if piece is not None:
                    new_board[i][j] = piece.type(piece.colour, i, j)

        return new_board

    def undo_move(self):
        prev = self.last_move
        moved, home, took = prev[0], prev[1], prev[2]

        self.place(type(moved)(moved.colour, home[0], home[1]))
        if took:
            self.place(type(took)(took.colour, moved.x, moved.y))
        else:
            self.clear(moved.x, moved.y)


def display_square(display, shade, x, y):
    if shade == "dark":
        colour = [180, 110, 60]
    else:
        colour = [215, 148, 80]

    pygame.draw.rect(display, colour, (x * 56, y * 56, 56, 56))

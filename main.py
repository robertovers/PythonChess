"""
=====
CHESS
=====
"""

import pygame
from board import Board


class Chess:

    def __init__(self):

        pygame.init()
        pygame.display.set_caption("Chess")

        self.win = pygame.display.set_mode((448, 448))
        self.clicked = None
        self.target = None
        self.run = False
        self.check = False
        self.move = 0

    def play(self):

        self.run = True
        b1 = Board(self.win)
        b1.piece_setup()

        while self.run:
            pygame.time.delay(50)
            b1.create_board()
            b1.print_pieces()

            if self.check is True:
                if self.move % 2 == 0:
                    b1.show_check(0)
                else:
                    b1.show_check(1)

            if self.clicked:
                b1.print_moves(self.clicked)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.clicked:
                        pos = pygame.mouse.get_pos()
                        pos = pos[0] // 56, pos[1] // 56

                        self.target = b1.squares[pos[0]][pos[1]]

                        if pos in b1.get_moves(self.clicked):
                            taken = b1.squares[pos[0]][pos[1]]
                            b1.last_move = (self.clicked, (self.clicked.x, self.clicked.y), taken)

                            b1.clear(self.clicked.x, self.clicked.y)

                            self.clicked.x = pos[0]
                            self.clicked.y = pos[1]

                            b1.place(self.clicked)
                            self.clicked, self.target = None, None

                            if b1.check():
                                if self.check:
                                    b1.undo_move()
                                    self.move -= 1
                                else:
                                    self.check = True
                            else:
                                self.check = False

                            self.move += 1

                        else:
                            self.clicked, self.target = None, None
                    
                    else:
                        pos = pygame.mouse.get_pos()
                        pos = pos[0]//56, pos[1]//56
                        self.clicked = b1.squares[pos[0]][pos[1]]

                        if self.clicked:
                            if self.clicked.colour == 0 and (self.move % 2 == 1):
                                self.clicked = None
                            elif self.clicked.colour == 1 and (self.move % 2 == 0):
                                self.clicked = None

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        if len(b1.last_move) > 0:
                            b1.undo_move()
                            self.move -= 1

                pygame.display.update()

        pygame.quit()


if __name__ == '__main__':

    chess = Chess()
    chess.play()

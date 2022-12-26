import pygame
from pygame import *
import sys
import helper_functions

from pieces import pawn, rook, knight, bishop, queen, king


class Board():
    def change_turns(self):
        if self.turn == "WHITE": self.turn = "BLACK"
        else: self.turn = "WHITE"
    
    def display_ending(self, winner):
        self.screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 75)
        text = font.render(f"{winner} WINS!", True, (255, 0, 0))
        
        self.screen.blit(text, ((self.screen.get_rect().width / 2) - (text.get_rect().width / 2), (self.screen.get_rect().height / 2) - (text.get_rect().height / 2)))
        pygame.display.flip()
        pygame.time.wait(2000)
        pygame.quit()
        sys.exit()
    
    def display_stalemate(self):
        self.screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 75)
        text = font.render(f"STALEMATE", True, (255, 0, 0))
        
        self.screen.blit(text, ((self.screen.get_rect().width / 2) - (text.get_rect().width / 2), (self.screen.get_rect().height / 2) - (text.get_rect().height / 2)))
        pygame.display.flip()
        pygame.time.wait(2000)
        pygame.quit()
        sys.exit()

    def __init__(self, piece_size=100):
        # Setup the screen
        self.screen = pygame.display.set_mode(flags=pygame.FULLSCREEN)
        pygame.display.set_caption("Chess")

        self.piece_size = piece_size

        # Setup Squares
        self.white_square = pygame.surface.Surface((self.piece_size, self.piece_size))
        self.green_square = pygame.surface.Surface((self.piece_size, self.piece_size))
        self.yellow_square = pygame.surface.Surface((self.piece_size, self.piece_size))
        self.white_square.fill((200, 200, 200))
        self.green_square.fill((50, 100, 50))
        self.yellow_square.fill((200, 200, 0))

        # Setup turns and pieces
        self.turn = "WHITE"
        self.is_piece_selected = False
        self.selected_piece = "None"
        self.available_moves = []
    
    #Set up the board
        self.board = []
        # Top side
        # POSITIONS SHOULD BE (ROW, COL), COORDINATES ARE (X,Y)
        self.board.append([rook.Rook(False, size=piece_size, pos=(0,0)),
                           knight.Knight(False, size=piece_size, pos=(0,1)), 
                           bishop.Bishop(False, size=piece_size, pos=(0,2)), 
                           queen.Queen(False, size=piece_size, pos=(0,3)), 
                           king.King(False, size=piece_size, pos=(0,4)), 
                           bishop.Bishop(False, size=piece_size, pos=(0,5)), 
                           knight.Knight(False, size=piece_size, pos=(0,6)), 
                           rook.Rook(False, size=piece_size, pos=(0,7))])
        self.board.append([pawn.Pawn(False, size=piece_size, pos=(1,i)) for i in range(8)])

        # Spaces
        for i in range(4):
            self.board.append([None for j in range(8)])

        # Bottom side
        self.board.append([pawn.Pawn(True, size=piece_size, pos=(6,i)) for i in range(8)])
        self.board.append([rook.Rook(True, size=piece_size, pos=(7,0)),
                           knight.Knight(True, size=piece_size, pos=(7,1)), 
                           bishop.Bishop(True, size=piece_size, pos=(7,2)), 
                           queen.Queen(True, size=piece_size, pos=(7,3)), 
                           king.King(True, size=piece_size, pos=(7,4)), 
                           bishop.Bishop(True, size=piece_size, pos=(7,5)), 
                           knight.Knight(True, size=piece_size, pos=(7,6)), 
                           rook.Rook(True, size=piece_size, pos=(7,7))])


    def update(self):
        # Check inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                coords = pygame.mouse.get_pos()
                row, col = helper_functions.screen_to_board_coordinates(coords, self.screen, self.board, self.piece_size)
                
                if self.is_piece_selected:
                    # Disselect pieces
                    if self.selected_piece == (row,col):
                        self.is_piece_selected = False
                        self.selected_piece = []
                        self.available_moves = []

                    # Make a move
                    elif (row,col) in self.available_moves:

                        # Remove the piece's current position
                        piece = self.board[self.selected_piece[0]][self.selected_piece[1]]
                        self.board[row][col] = piece
                        piece.pos = (row,col)

                        print(self.selected_piece)

                        self.board[self.selected_piece[0]][self.selected_piece[1]] = None

                        # Update the game
                        self.change_turns()
                        self.is_piece_selected = False
                        self.available_moves = []
                        self.selected_piece = "None"


                        # # Check game endings
                        if helper_functions.is_checkmate(self.board, True):
                            self.display_ending("Black")
                        elif helper_functions.is_checkmate(self.board, False):
                            self.display_ending("White")
                        # elif helper_functions.is_stalemate(self.board):
                        #     self.display_stalemate()

                        
                else:
                    # Select a piece
                    if self.board[row][col] != None:
                        if ((self.board[row][col].is_white and self.turn == "WHITE") or (not self.board[row][col].is_white and self.turn == "BLACK")):
                            self.selected_piece = (row,col)
                            self.is_piece_selected = True
                            self.available_moves = self.board[row][col].get_moves(self.board)
    
    def draw(self):

        # Draw the board
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                # White squares
                if (((row % 2 == 0) and (col % 2 == 0)) or ((row % 2 != 0) and (col % 2 != 0))):
                    if (row,col) == self.selected_piece:
                        self.screen.blit(self.yellow_square, helper_functions.board_to_screen_coordinates((row, col), self.screen, self.board, self.piece_size))  
                    else:
                        self.screen.blit(self.white_square, helper_functions.board_to_screen_coordinates((row, col), self.screen, self.board, self.piece_size))  
                # Black squares 
                else:
                    if [row,col] == self.selected_piece:
                        self.screen.blit(self.yellow_square, helper_functions.board_to_screen_coordinates((row, col), self.screen, self.board, self.piece_size))   
                    else:
                        self.screen.blit(self.green_square, helper_functions.board_to_screen_coordinates((row, col), self.screen, self.board, self.piece_size))
                    
        # Draw pieces
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] != None:
                        self.board[row][col].draw(self.screen, self.board) 
        
        # Draw available moves
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if (row, col) in self.available_moves:
                    pygame.draw.circle(self.screen, (100, 100, 255), helper_functions.board_to_screen_coordinates((row, col), self.screen, self.board, self.piece_size, centered=True), self.piece_size / 4)
        
        pygame.display.update()

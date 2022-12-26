import pygame
import sys
sys.path.append('../chess')
import helper_functions

class Piece(pygame.sprite.Sprite):
    def __init__(self, is_white, whitePath, blackPath, pos=(0,0), size=100):
        pygame.sprite.Sprite.__init__(self)
        self.is_white = is_white
        self.size = size

        if is_white:
            self.image = pygame.transform.smoothscale( pygame.image.load(whitePath) , (size, size))
        else:
            self.image = pygame.transform.smoothscale( pygame.image.load(blackPath) , (size, size))

        self.rect = self.image.get_rect()
        self.pos = pos

    def draw(self, screen, board):
        screen.blit(self.image, helper_functions.board_to_screen_coordinates(self.pos, screen, board, self.size))
    
    def get_moves(self, board):
        raise RuntimeError("Get moves function not implemented")
    
    def pos_out_of_bounds(self, pos):
        if ((pos[0] > 7) or (pos[0] < 0) or (pos[1] < 0) or (pos[1] > 7)): return True
        return False
    
    def check_turn(self, pos, board, moves):
        if self.pos_out_of_bounds(pos): return moves

        if board[pos[0]][pos[1]] == None: 
            moves.append((pos[0], pos[1]))
        elif board[pos[0]][pos[1]].is_white != self.is_white:
            moves.append((pos[0], pos[1]))
        return moves
    
    def check_move(self, pos, board, moves):
        if self.pos_out_of_bounds(pos): return moves

        if board[pos[0]][pos[1]] == None:
            moves.append((pos[0], pos[1]))
        return moves
    
    def check_take(self, pos, board, moves):
        if self.pos_out_of_bounds(pos): return moves

        if board[pos[0]][pos[1]] != None:
            if board[pos[0]][pos[1]].is_white != self.is_white: 
                moves.append((pos[0], pos[1]))
        return moves



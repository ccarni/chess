import pygame
import board

pygame.init()

board = board.Board()
while True: 
    board.update()
    board.draw()

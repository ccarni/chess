import piece

class Knight(piece.Piece):
    def __init__(self, is_white, pos=(0,0), size=100):
        white_path = "D:\Software\Scripts\Python_Files\chess\\assets\white\white_knight.png"
        black_path = "D:\Software\Scripts\Python_Files\chess\\assets\\black\\black_knight.png"
        self.type = "Knight"
        super().__init__(is_white, white_path, black_path, pos, size)

    def get_moves(self, board):
        moves = []
        row, col = self.pos
        # Check da horse jumps
        moves = self.check_turn((row - 1, col + 2), board, moves)
        moves = self.check_turn((row - 2, col + 1), board, moves)
        moves = self.check_turn((row - 2, col - 1), board, moves)
        moves = self.check_turn((row - 1, col - 2), board, moves)
        moves = self.check_turn((row + 1, col - 2), board, moves)
        moves = self.check_turn((row + 2, col - 1), board, moves)
        moves = self.check_turn((row + 2, col + 1), board, moves)
        moves = self.check_turn((row + 1, col + 2), board, moves)

        return moves


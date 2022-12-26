import sys
sys.path.append("pieces")
import piece

class Pawn(piece.Piece):
    def __init__(self, is_white, pos=(0,0), size=100):
        white_path = "D:\Software\Scripts\Python_Files\chess\\assets\white\white_pawn.png"
        black_path = "D:\Software\Scripts\Python_Files\chess\\assets\\black\\black_pawn.png"
        self.type = "Pawn"
        super().__init__(is_white, white_path, black_path, pos, size)
    
    def get_moves(self, board):
        moves = []
        row, col = self.pos

        if self.is_white:
            # Check aheads
            moves = self.check_move((row-1, col), board, moves)
            if not moves == []:
                if row == 6:
                    moves = self.check_move((row-2, col), board, moves)
            # Check diagonals
            moves = self.check_take((row-1, col-1), board, moves)
            moves = self.check_take((row-1, col+1), board, moves)

        else:
            # Check aheads
            moves = self.check_move((row+1, col), board, moves)
            if not moves == []:
                if row == 1:
                    moves = self.check_move((row+2, col), board, moves)
            # Check diagonals
            moves = self.check_take((row+1, col-1), board, moves)
            moves = self.check_take((row+1, col+1), board, moves)

        return moves

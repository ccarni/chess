import piece


class King(piece.Piece):
    def __init__(self, is_white, pos=(0,0), size=100):
        white_path = "D:\Software\Scripts\Python_Files\chess\\assets\white\white_king.png"
        black_path = "D:\Software\Scripts\Python_Files\chess\\assets\\black\\black_king.png"
        self.type = "King"
        self.initial_pos = pos
        super().__init__(is_white, white_path, black_path, pos, size)

    def get_moves(self, board):
        moves = []
        row, col = self.pos

        # Check basic moves
        moves = self.check_turn((row, col + 1), board, moves)
        moves = self.check_turn((row - 1, col + 1), board, moves)
        moves = self.check_turn((row - 1, col), board, moves)
        moves = self.check_turn((row - 1, col - 1), board, moves)
        moves = self.check_turn((row, col - 1), board, moves)
        moves = self.check_turn((row + 1, col - 1), board, moves)
        moves = self.check_turn((row + 1, col), board, moves)
        moves = self.check_turn((row + 1, col + 1), board, moves)


        return moves
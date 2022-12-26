import piece

class Rook(piece.Piece):
    def __init__(self, is_white, pos=(0,0), size=100):
        white_path = "D:\Software\Scripts\Python_Files\chess\\assets\white\white_rook.png"
        black_path = "D:\Software\Scripts\Python_Files\chess\\assets\\black\\black_rook.png"
        self.type = "Rook"
        self.initial_pos = pos
        super().__init__(is_white, white_path, black_path, pos, size)
    
    def get_moves(self, board):
        moves = []
        edge = len(board)
        row, col = self.pos

        # Check above
        for i in range(row - 1, -1, -1):
            if board[i][col] is None:
                moves.append((i, col))
            elif board[i][col].is_white is not self.is_white:
                moves.append((i, col))
                break
            else:
                break
        
        # Check below
        for i in range(row + 1, edge):
            if board[i][col] is None:
                moves.append((i, col))
            elif board[i][col].is_white is not self.is_white:
                moves.append((i, col))
                break
            else:
                break
        
        # Check left
        for j in range(col - 1, -1, -1):
            if board[row][j] is None:
                moves.append((row, j))
            elif board[row][j].is_white is not self.is_white:
                moves.append((row, j))
                break
            else:
                break
        
        # Check right
        for j in range(col + 1, edge):
            if board[row][j] is None:
                moves.append((row, j))
            elif board[row][j].is_white is not self.is_white:
                moves.append((row, j))
                break
            else:
                break

        return moves

import math

def screen_to_board_coordinates(coords, screen, board, piece_size):
    x_center = (screen.get_rect().width / 2) - (len(board)*piece_size/2)
    y_center = (screen.get_rect().height / 2) - (len(board[0])*piece_size/2)

    row = math.floor((coords[1] - y_center)/piece_size)
    col = math.floor((coords[0] - x_center)/piece_size)
    
    return row, col

def board_to_screen_coordinates(pos, screen, board, piece_size, centered=False):
    x_center = (screen.get_rect().width / 2) - (len(board)*piece_size/2)
    y_center = (screen.get_rect().height / 2) - (len(board[0])*piece_size/2)

    if centered:
        row = x_center + (pos[1] + 0.5)*piece_size
        col = y_center + (pos[0] + 0.5)*piece_size
    else:
        row = x_center + pos[1]*piece_size
        col = y_center + pos[0]*piece_size

    return row, col

def find_piece_location(board, type, is_color_white):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] != None:
                if (board[row][col].type == type) and (board[row][col].is_white == is_color_white):
                    return (row, col)


def is_square_attacked(board, pos, is_color_white, return_piece=False):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] != None:
                if board[row][col].is_white != is_color_white:
                    if pos in board[row][col].get_moves(board):
                        if return_piece:
                            return board[pos[0]][pos[1]]
                        else:
                            return True
    if return_piece:
        return None
    return False

def is_square_attacked_after_move(board, pos, original_pos, moved_pos, is_color_white):
    # Make the move
    new_board = board
    moved_piece = new_board[original_pos[0]][original_pos[1]]
    new_board[moved_pos[0]][moved_pos[1]] = moved_piece
    new_board[original_pos[0]][original_pos[1]] = None

    # If we move the attacked piece, update its position
    if pos == original_pos:
        pos = moved_pos

    # Check attack
    return is_square_attacked(new_board, pos, is_color_white)

def is_checkmate(board, is_color_white) -> bool:
    original_board = board
    # Find the king
    king_pos = find_piece_location(board, "King", is_color_white)

    if is_square_attacked(board, king_pos, is_color_white, return_piece=False):
        attacking_piece = is_square_attacked(board, king_pos, is_color_white, return_piece=True)
        
    #     # Check for blocking moves

        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] != None:
                    if board[row][col].is_white == is_color_white:

                        legal_moves = board[row][col].get_moves(board)
                        original_pos = (row, col)

                        # for i, j in enumerate(original_board):
                        #     print(j)
                        #     print("- "*25)

                        for move in legal_moves:

                            # for i, j in enumerate(original_board):
                            #     print(j)
                            #     print("- "*25)
                            # print("-"*200)

                            print ( is_square_attacked_after_move(board, king_pos, original_pos, move, is_color_white), move )

                            if (not is_square_attacked_after_move(board, king_pos, original_pos, move, is_color_white)):
                                return False

        # Check for attacking moves

        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] != None:
                    if board[row][col].is_white == is_color_white:

                        legal_moves = board[row][col].get_moves(board)

                        for move in legal_moves:
                            if move == attacking_piece.pos:
                                return False
        return True
    return False


def is_stalemate(board):
    white = True
    king_pos = find_piece_location(board, "King", white)
     # Iterate through the board
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] != None:
                if board[row][col].is_white == white:
                    legal_moves = board[row][col].get_moves(board)
                    original_pos = [row, col]

                    for move in legal_moves:
                        if not is_square_attacked_after_move(board, king_pos, original_pos, move, white):
                            return False

    white = False
    king_pos = find_piece_location(board, "King", white)
     # Iterate through the board
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] != None:
                if board[row][col].is_white == white:
                    legal_moves = board[row][col].get_moves(board)
                    original_pos = (row, col)

                    for move in legal_moves:
                        if not is_square_attacked_after_move(board, king_pos, original_pos, move, white):
                            return False
    return True


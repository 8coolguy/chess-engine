import chess

def apply_move(board,move_str) -> chess.Board:
    """
    Applies a move in UCI/long algebraic notation (e.g. 'e2e4', 'e7e8q') 
    to the global chess.Board() instance.
    move_str: str, move in long algebraic/UCI notation
    Returns the updated board.
    """
    move = chess.Move.from_uci(move_str)  # parse the move
    if move in board.legal_moves:
        board.push(move)  # apply it
    else:
        raise ValueError(f"Illegal move: {move_str}")
    return board
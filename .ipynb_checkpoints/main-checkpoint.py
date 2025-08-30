import chess
import chess.svg

from chessboard import display

#store current board state into a global variable
chess_board = chess.Board("8/8/8/8/4N3/8/8/8 w - - 0 1")
#calcultae board state

#determine if the board is in the end game or opening

#minimax algorithm


#alpha beta pruning to get rif of branches using move ordering
def display_board():
    chess.svg.board(chess_board)
def main():
    display(chess_board.fen())

if __name__ == "__main__":
    main()

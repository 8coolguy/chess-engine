from abc import ABC, abstractmethod
import chess 
import sys

NAME = "BOT"
AUTHOR = "8coolguy"
class ChessEngineBase(ABC):
    def __init__(self):
        self.board = chess.Board() 
    def handleInput(self,command:str):
        parsedCommand = command.split()
        n = len(parsedCommand)
        if command == "quit":
            sys.exit(0)
        elif command == "isready":
            print("readyok")
        elif command == "uci":
            if NAME: print("id name " + NAME)
            if AUTHOR: print("id author " + AUTHOR)
            print("uciok")
        elif parsedCommand[0] == "go":
            print(self.determineBestMove())
        elif parsedCommand[0] == "position":
            i = 1
            if parsedCommand[i] == "fen":
                fen = " ".join(parsedCommand[i+1:i+7])
                chess_board = chess.Board(fen)
                i += 7
            elif parsedCommand[i] == "startpos":
                chess_board = chess.Board()
                i += 1
            if parsedCommand[i] == "moves":
                i+=1
                while i < n:
                    chess_board = self.apply_move(chess_board,parsedCommand[i])
                    i+=1
        elif parsedCommand[0] == "option":
            pass
    def apply_move(self,move_str):
        """
        Applies a move in UCI/long algebraic notation (e.g. 'e2e4', 'e7e8q') 
        to the global chess.Board() instance.
        move_str: str, move in long algebraic/UCI notation
        Returns the updated board.
        """
        move = chess.Move.from_uci(move_str)  # parse the move
        if move in self.board.legal_moves:
            self.board.push(move)  # apply it
        else:
            raise ValueError(f"Illegal move: {move_str}")
        return self.board
    @abstractmethod
    def determineBestMove(self):
        pass
    @abstractmethod
    def analyze(self):
        pass
    @abstractmethod
    def info(self):
        pass



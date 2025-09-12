from abc import ABC, abstractmethod
from helper import apply_move
import chess 
import sys

NAME = "BOT"
AUTHOR = "8coolguy"
class ChessEngineBase(ABC):
    def __init__(self, time_limit, verbose):
        self.board = chess.Board() 
        self.verbose = verbose
        self.time_limit = time_limit
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
            print("bestmove " + self.determineBestMove().uci())
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
                    chess_board = apply_move(chess_board,parsedCommand[i])
                    i+=1
            self.board = chess_board
        elif parsedCommand[0] == "option":
            pass
    def setPosition(self, fen:str):
        self.handleInput("position fen " + fen + " moves ")

    @abstractmethod
    def determineBestMove(self):
        pass
    @abstractmethod
    def analyze(self):
        pass
    @abstractmethod
    def info(self):
        pass



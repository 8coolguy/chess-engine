from ChessEngineBase import ChessEngineBase

import chess
from tqdm import tqdm
piece_values = {
    chess.PAWN: 100,
    chess.ROOK: 500,
    chess.KNIGHT: 320,
    chess.BISHOP: 330,
    chess.QUEEN: 900,
    chess.KING: 20000
}
class MinMaxEngine(ChessEngineBase):
    def __init__(self,time_limit, verbose, depth):
        super().__init__(time_limit, verbose)
        self.depth = depth

    def minimax_root(self) -> chess.Move: 
        moves = list(self.board.legal_moves)
        bestMove, evaluation = moves[0], float("inf")
        for move in tqdm(moves, disable = not self.verbose):
            self.board.push(move)
            score = self.minimax(0)
            if score < evaluation:
                evaluation = score
                bestMove = move
            self.board.pop()
        return bestMove
        
    
    #uses the minimax algorithm at depth 5 to determine the best move on the chess board
    #used the point system example on the blog: https://healeycodes.com/building-my-own-chess-engine
    def minimax(self, depth = 0) -> float:
        moves = list(self.board.legal_moves)
        if depth == self.depth or self.board.is_game_over(): 
            return self.calculate_score()
        #pick best score for the opponent
        if depth % 2:
            value = float("-inf")
            for move in moves:
                self.board.push(move)
                temp = self.minimax(depth+1)
                value = max(value,temp)
                self.board.pop()
            return value
        else:
            value = float("inf")
            for move in moves:
                self.board.push(move)
                temp = self.minimax(depth+1)
                value = min(value,temp)
                self.board.pop()
            return value
    def calculate_score(self):
        black_score,white_score = 0,0
        for square in chess.SQUARES:
            at_square = self.board.piece_at(square)
            if not at_square: continue
            if at_square.color == chess.WHITE:
                white_score += piece_values[at_square.piece_type]
            else:
                black_score += piece_values[at_square.piece_type]
        if self.board.turn == chess.WHITE: return white_score
        else: return black_score
    
    def determineBestMove(self):
        return self.minimax_root()
        
    def analyze(self):
        pass

    def info(self):
        pass
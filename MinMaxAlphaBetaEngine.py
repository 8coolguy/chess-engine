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
class MinMaxAlphaBetaEngine(ChessEngineBase):
    def __init__(self,time_limit, verbose, depth):
        super().__init__(time_limit, verbose)
        self.depth = depth

    def minimax_root(self) -> chess.Move: 
        moves = list(self.board.legal_moves)
        bestMove, evaluation = moves[0], float("inf")
        for move in tqdm(moves, disable = not self.verbose):
            self.board.push(move)
            score = self.minimax(depth = 1)
            self.board.pop()
            if score < evaluation:
                evaluation = score
                bestMove = move
        return bestMove
        
    
    #uses the minimax algorithm at depth 5 to determine the best move on the chess board
    #used the point system example on the blog: https://healeycodes.com/building-my-own-chess-engine
    def minimax(self, alpha=float("-inf"), beta=float("inf"), depth = 0) -> float:
        moves = list(self.board.legal_moves)
        self.stattrack += 1
        if depth == self.depth:
            return self.calculate_score((depth % 2) ^ self.board.turn)
        if self.board.is_game_over(): 
            result = self.board.outcome()
            if result != True or result != False:
                return 0
            if result == self.board.turn:
                return float("inf")
            elif result != self.board.turn:
                return float("-inf")

        #pick best score for the opponent
        if depth % 2:
            #maximizing player
            value = float("-inf")
            for move in moves:
                self.board.push(move)
                temp = self.minimax(alpha, beta, depth = depth + 1)
                self.board.pop()
                value = max(value,temp)
                alpha = max(alpha, value)
                if beta <= alpha:
                    break
            return value
        else:
            #minimizing player
            value = float("inf")
            for move in moves:
                self.board.push(move)
                temp = self.minimax(alpha, beta, depth = depth + 1)
                self.board.pop()
                value = min(value,temp)
                beta = min(beta, value)
                if beta <= alpha:
                    break
            return value
    def calculate_score(self, turn ):
        black_score,white_score = 0,0
        for square in chess.SQUARES:
            at_square = self.board.piece_at(square)
            if not at_square: continue
            if at_square.color == chess.WHITE:
                white_score += piece_values[at_square.piece_type]
            else:
                black_score += piece_values[at_square.piece_type]
        if turn == chess.WHITE: return white_score - black_score
        else: return black_score - white_score
    
    def determineBestMove(self):
        self.stattrack = 0
        bestMove = self.minimax_root()
        print("Moves Calculated", self.stattrack)
        return bestMove
        
    def analyze(self):
        pass

    def info(self):
        pass
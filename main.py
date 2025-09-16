import argparse
from MinMaxEngine import MinMaxEngine
from MinMaxAlphaBetaEngine import MinMaxAlphaBetaEngine
import chess
import time
import sys
from helper import apply_move
def main():
    parser = argparse.ArgumentParser(prog="Chess Engine Player", description="Play against different types of engines.")
    parser.add_argument("engine",type=str, default="MinMax") 
    parser.add_argument("-d", "--depth", type=int, default=5)
    parser.add_argument("-v", "--verbose", type=bool, default=False)
    parser.add_argument("-T", "--time_limit", type=bool, default=1.0)  
    parser.add_argument("-t", "--type", type=str, default="player")
    #parser.add_argumen
    args = parser.parse_args()
    run_engine(args.engine, verbose=args.verbose, depth=args.depth, time_limit=args.time_limit,type=args.type)

def run_engine(engine_type, verbose, depth, time_limit, type):
        #init engine
        engine = None
        if engine_type == "MinMax":
            engine = MinMaxEngine(verbose = verbose, depth = depth, time_limit = time_limit)
        elif engine_type =="MinMaxAlphaBeta":
            engine = MinMaxAlphaBetaEngine(verbose=verbose, depth = depth, time_limit=time_limit)
            
        if type == "player":
            game_vs_human(engine)
        elif type == "engine":
            game_with_uci(engine)            
def game_vs_human(engine):
    isWhite = input("White?(y/n)") 
    isWhite = isWhite == "y"
    helpString = ""
    if isWhite: helpString = "You are White."
    else: helpString = "You are Black."
    game = chess.Board()
    if not isWhite:
        engine.setPosition(game.fen())
        start = time.perf_counter()
        bestMove = engine.determineBestMove().uci()
        end = time.perf_counter()
        elapsed = end - start
        print("Time", round(elapsed))
        print("Moves/sec Analyzed",float(engine.stattrack)//round(elapsed,2))
        game = apply_move(game, bestMove)
    print(game)
    print("A B C D E F G H")
    while not game.is_checkmate():
        move = ""
        while True:
            move = input("What is your move in algebraic long notation? " + helpString)
            if move == "quit":
                sys.exit(0)
            elif move == help:
                continue
            try:
                if chess.Move.from_uci(move) in game.legal_moves:
                    break
            except Exception as e:
                print(e)
            print("Try Again")
        game = apply_move(game, move)
        print(game)
        print("A B C D E F G H")
        engine.setPosition(game.fen())
        start = time.perf_counter()
        bestMove = engine.determineBestMove().uci()
        end = time.perf_counter()
        elapsed = end - start
        print("Time", round(elapsed))
        print("Moves/sec Analyzed",float(engine.stattrack)//round(elapsed,2))
        print(bestMove)
        game = apply_move(game, bestMove)
        print(game)
        print("A B C D E F G H")


def game_with_uci():
    pass
    
    

    

    
    
    
if __name__ == "__main__":
    main()






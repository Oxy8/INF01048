import random
import time
from typing import Tuple, Callable



def minimax_move(state, max_depth:int, eval_func:Callable) -> Tuple[int, int]:
    
    """
    Returns a move computed by the minimax algorithm with alpha-beta pruning for the given game state.
    :param state: state to make the move (instance of GameState)
    :param max_depth: maximum depth of search (-1 = unlimited)
    :param eval_func: the function to evaluate a terminal or leaf state (when search is interrupted at max_depth)
                    This function should take a GameState object and a string identifying the player,
                    and should return a float value representing the utility of the state for the player.
    :return: (int, int) tuple with x, y coordinates of the move (remember: 0 is the first row/column)
    """

    #raise NotImplementedError()

    start_time = time.time()
    best_move_so_far = None
    time_limit = 4.5

    def time_exceeded():
        return time.time() - start_time >= time_limit
    
    def alphabeta(node, depth, alpha, beta, maximizing_player):
        if node.is_terminal() or (max_depth != -1 and depth == 0) or time_exceeded():
            # (max_depth != -1 and depth == 0) não deve ocorrer normalmente, pois se max_depth = 1, chamada recursiva tem depth como float(inf) sempre.
            return eval_func(node, state.player), None


    
        best_move = None
        if maximizing_player:
            value = float('-inf')
            for move in node.legal_moves():
                child = node.next_state(move)
                child_value, _ = alphabeta(child, depth - 1, alpha, beta, False)
                if child_value > value:
                    value = child_value
                    best_move = move

                alpha = max(alpha, value)
                if beta <= alpha:
                    break  
            return value, best_move
        else:
            value = float('inf')
            for move in node.legal_moves():
                child = node.next_state(move)
                child_value, _ = alphabeta(child, depth - 1, alpha, beta, True)
                if child_value < value:
                    value = child_value
                    best_move = move

                beta = min(beta, value)
                if beta <= alpha:
                    break  

            return value, best_move


    depth = 1
    while max_depth == -1 or depth <= max_depth:
        if time_exceeded():
            break

        _, move = alphabeta(state, depth, float('-inf'), float('inf'), True)
        if not time_exceeded() and move is not None:
            best_move_so_far = move
        else:
            break

        depth += 1

    return best_move_so_far


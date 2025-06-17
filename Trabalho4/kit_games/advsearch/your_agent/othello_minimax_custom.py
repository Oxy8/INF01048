import random
from typing import Tuple
from ..othello.gamestate import GameState
from ..othello.board import Board
from .minimax import minimax_move

# Voce pode criar funcoes auxiliares neste arquivo
# e tambem modulos auxiliares neste pacote.
#
# Nao esqueca de renomear 'your_agent' com o nome
# do seu agente.

EVAL_TEMPLATE = [
    [100, -30, 6, 2, 2, 6, -30, 100],
    [-30, -50, 1, 1, 1, 1, -50, -30],
    [  6,   1, 1, 1, 1, 1,   1,   6],
    [  2,   1, 1, 3, 3, 1,   1,   2],
    [  2,   1, 1, 3, 3, 1,   1,   2],
    [  6,   1, 1, 1, 1, 1,   1,   6],
    [-30, -50, 1, 1, 1, 1, -50, -30],
    [100, -30, 6, 2, 2, 6, -30, 100]
]

def make_move(state) -> Tuple[int, int]:
    """
    Returns a move for the given game state
    :param state: state to make the move
    :return: (int, int) tuple with x, y coordinates of the move (remember: 0 is the first row/column)
    """

    # o codigo abaixo apenas retorna um movimento aleatorio valido para
    # a primeira jogada 
    # Remova-o e coloque uma chamada para o minimax_move (que vc implementara' no modulo minimax).
    # A chamada a minimax_move deve receber sua funcao evaluate como parametro.

    return minimax_move(state, 4, evaluate_custom)




def count_stable_discs(state, player):
    """
    Conta discos estáveis do jogador.
    Um disco é considerado estável se estiver conectado a um canto
    e todos os discos entre ele e o canto forem do mesmo jogador.
    """
    board = state.board.tiles
    size = 8
    stable = [[False]*size for _ in range(size)]
    directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]

    corners = [(0, 0), (0, size-1), (size-1, 0), (size-1, size-1)]
    total_stable = 0

    for cx, cy in corners:
        if board[cx][cy] != player:
            continue
        stable[cx][cy] = True
        total_stable += 1

        for dx, dy in directions:
            # Percorre em duas direções simétricas a partir do canto
            for sign in [1, -1]:
                x, y = cx + sign*dx, cy + sign*dy
                while 0 <= x < size and 0 <= y < size:
                    if board[x][y] != player:
                        break
                    # Marca como estável se todos anteriores nessa linha forem do jogador
                    prev_x, prev_y = x - sign*dx, y - sign*dy
                    if not stable[prev_x][prev_y]:
                        break
                    stable[x][y] = True
                    total_stable += 1
                    x += sign*dx
                    y += sign*dy

    return total_stable




def evaluate_custom(state, player:str) -> float:
    """
    Evaluates an othello state from the point of view of the given player. 
    If the state is terminal, returns its utility. 
    If non-terminal, returns an estimate of its value based on your custom heuristic
    :param state: state to evaluate (instance of GameState)
    :param player: player to evaluate the state for (B or W)
    """

    if state.is_terminal():
        winner = state.winner()

        if winner == player:
            return 1
        if winner is not None:
            return -1
        else:
            return 0

    opponent = 'W' if player == 'B' else 'B'


# 1. Mobilidade (número de jogadas legais)
    player_moves = len(state.board.legal_moves(player))
    opponent_moves = len(state.board.legal_moves(opponent))
    mobility = (player_moves - opponent_moves) / (player_moves + opponent_moves + 1)

# 2. Estabilidade (peças que nunca podem ser viradas)
    stable_player = count_stable_discs(state, player)
    stable_opponent = count_stable_discs(state, opponent)
    stability = (stable_player - stable_opponent) / (stable_player + stable_opponent + 1)


# Combinação ponderada (os pesos podem ser ajustados por teste empírico)
    total_score = (
        0.6 * mobility +
        0.4 * stability
    )

    return total_score
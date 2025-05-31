#------------------------------------------------------------------------#
from typing    import Iterable, Set, Tuple, Callable
from heapq     import heappush, heappop
from itertools import count
#------------------------------------------------------------------------#

objetivo = "12345678_"
OBJETIVO_POS = {v: i for i, v in enumerate("12345678_")}

class Nodo:
    """
    Implemente a classe Nodo com os atributos descritos na funcao init
    """
    def __init__(self, estado, pai=None, acao=None, custo=0):
        """
        Inicializa o nodo com os atributos recebidos
        :param estado:str, representacao do estado do 8-puzzle
        :param pai:Nodo, referencia ao nodo pai, (None no caso do nó raiz)
        :param acao:str, acao a partir do pai que leva a este nodo (None no caso do nó raiz)
        :param custo:int, custo do caminho da raiz até este nó
        """
        self.estado = estado
        self.pai    = pai
        self.acao   = acao
        self.custo  = custo

    def __hash__(self):
        return hash(self.estado)

    def __eq__(self, other):
        return isinstance(other, Nodo) and self.estado == other.estado
    
#------------------------------------------------------------------------#
#------------------------------------------------------------------------#
def sucessor(estado:str)->Set[Tuple[str,str]]:
    """
    Recebe um estado (string) e retorna um conjunto de tuplas (ação,estado atingido)
    para cada ação possível no estado recebido.
    Tanto a ação quanto o estado atingido são strings também.
    :param estado:
    :return:
    """
    sucessores = set()
    index  = estado.index('_')
    
    linha  = index // 3
    coluna = index %  3
    
    def troca(string, i, j):
        lista = list(string)
        lista[i], lista[j] = lista[j], lista[i]
        return ''.join(lista)
    
    if linha  != 0:
        sucessores.add(("acima", troca(estado, index, index-3)))
    if linha  != 2:
        sucessores.add(("abaixo", troca(estado, index, index+3)))
    if coluna != 0:
        sucessores.add(("esquerda", troca(estado, index, index-1)))
    if coluna != 2:
        sucessores.add(("direita", troca(estado, index, index+1)))
    
    return sucessores
#------------------------------------------------------------------------#
#------------------------------------------------------------------------#
def expande(nodo:Nodo)->Set[Nodo]:
    """
    Recebe um nodo (objeto da classe Nodo) e retorna um conjunto de nodos.
    Cada nodo do conjunto é contém um estado sucessor do nó recebido.
    :param nodo: objeto da classe Nodo
    :return:
    """
    sucessores = sucessor(nodo.estado)
    filhos     = set()
    
    for(acao, novo_estado) in sucessores:
        filho = Nodo(novo_estado, nodo, acao, nodo.custo + 1)
        filhos.add(filho)
    
    return filhos
#------------------------------------------------------------------------
#------------------------------------------------------------------------
def hamming(estado:str)->int:
    """
    Recebe um estado (string), compara-o com '12345678_', e retorna o número de
    caracteres de mesmo índice que são diferentes entre si ("peças fora do lugar")
    :param estado:
    :return:
    """
    return sum(1 for i in range(9) if estado[i] != '_' and estado[i] != objetivo[i])
#------------------------------------------------------------------------
def manhattan(estado:str)->int:
    """
    Recebe um estado (string), compara-o com '12345678_', calcula a distância Manhattan
    de cada peça ao seu lugar correto, e retorna a soma de todas essas distâncias.
    :param estado:
    :return:
    """

    soma = 0
    
    for i in range(9):
        peca = estado[i]
        
        if peca != '_':
            pos_obj = OBJETIVO_POS[peca]
            linha_estado  = i // 3
            coluna_estado = i %  3
            linha_objetivo  = pos_obj // 3
            coluna_objetivo = pos_obj %  3
            
            soma += abs(linha_objetivo-linha_estado) + abs(coluna_objetivo-coluna_estado)
    
    return soma
#------------------------------------------------------------------------
#------------------------------------------------------------------------
def astar(estado:str, heuristica:Callable[[str], int])->list[str]:
    contador = count()
    
    def f(nodo:Nodo):
        return nodo.custo + heuristica(nodo.estado)
    
    inicial    = Nodo(estado)
    fronteira  = []
    explorados = set()
    
    heappush(fronteira, (f(inicial), next(contador), inicial))
    
    while fronteira:
        _, _, atual = heappop(fronteira)
        
        if atual.estado == objetivo:
            caminho = []
            while atual.pai:
                caminho.append(atual.acao)

                atual = atual.pai
            

            return list(reversed(caminho))
        
        if atual in explorados:
            continue
        
        explorados.add(atual)
        
        for vizinho in expande(atual):
            if vizinho not in explorados:
                heappush(fronteira, (f(vizinho), next(contador), vizinho))
        
    return None
#------------------------------------------------------------------------
#------------------------------------------------------------------------
def astar_hamming(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Hamming e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    return astar(estado, hamming)
#------------------------------------------------------------------------
def astar_manhattan(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Manhattan e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    return astar(estado, manhattan)
#------------------------------------------------------------------------
#------------------------------------------------------------------------

#opcional,extra
def bfs(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca em LARGURA e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError

#opcional,extra
def dfs(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca em PROFUNDIDADE e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError

#opcional,extra
def astar_new_heuristic(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = sua nova heurística e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError
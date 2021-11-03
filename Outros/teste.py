import argparse
import time
import timeit
from collections import deque


# Information *****************************************************
class estado_puzzle:
    def __init__(self, estado, vizinho, direcao, profundidade, custo, key):
        self.estado = estado
        self.vizinho = vizinho
        self.direcao = direcao
        self.profundidade = profundidade
        self.custo = custo
        self.key = key
        if self.estado:
            self.map = ''.join(str(e) for e in self.estado)

    def __eq__(self, other):
        return self.map == other.map

    def __lt__(self, other):
        return self.map < other.map

    def __str__(self):
        return str(self.map)

    # Global variables***********************************************


objetivoestado = [0, 1, 2, 3, 4, 5, 6, 7, 8]
objetivoNo = None  # at finding solution
NosVisitados = 0  # total Nos visited
ProfundidadeMaxima = 0  # max deep
Fronteira = 0  # max frontier


# BFS**************************************************************
def bfs(estado_inicial):
    global Fronteira, objetivoNo, ProfundidadeMaxima

    boardVisited = set()
    Fila = deque([estado_puzzle(estado_inicial, None, None, 0, 0, 0)])

    while Fila:
        No = Fila.popleft()
        boardVisited.add(No.map)
        if No.estado == objetivoestado:
            objetivoNo = No
            return Fila
        posiblePaths = subNos(No)
        for path in posiblePaths:
            if path.map not in boardVisited:
                Fila.append(path)
                boardVisited.add(path.map)
                if path.profundidade > ProfundidadeMaxima:
                    ProfundidadeMaxima = ProfundidadeMaxima + 1
        if len(Fila) > Fronteira:
            FilaSize = len(Fila)
            Fronteira = FilaSize


# DFS**************************************************************
def dfs(estado_inicial):
    global Fronteira, objetivoNo, ProfundidadeMaxima

    boardVisited = set()
    pilha = list([estado_puzzle(estado_inicial, None, None, 0, 0, 0)])
    while pilha:
        No = pilha.pop()
        boardVisited.add(No.map)
        if No.estado == objetivoestado:
            objetivoNo = No
            return pilha
        # inverse the order of next paths for execution porpuses
        posiblePaths = reversed(subNos(No))
        for path in posiblePaths:
            if path.map not in boardVisited:
                pilha.append(path)
                boardVisited.add(path.map)
                if path.profundidade > ProfundidadeMaxima:
                    ProfundidadeMaxima = 1 + ProfundidadeMaxima
        if len(pilha) > Fronteira:
            Fronteira = len(pilha)


# AST**************************************************************
def ast(estado_inicial):
    global Fronteira, ProfundidadeMaxima, objetivoNo

    # transform initial estado to calculate Heuritic
    No1 = ""
    for poss in estado_inicial:
        No1 = No1 + str(poss)

    # calculate Heuristic and set initial No
    key = Heuristic(No1)
    boardVisited = set()
    Fila = []
    Fila.append(estado_puzzle(estado_inicial, None, None, 0, 0, key))
    boardVisited.add(No1)

    while Fila:
        Fila.sort(key=lambda o: o.key)
        No = Fila.pop(0)
        if No.estado == objetivoestado:
            objetivoNo = No
            return Fila
        posiblePaths = subNos(No)
        for path in posiblePaths:
            thisPath = path.map[:]
            if thisPath not in boardVisited:
                key = Heuristic(path.map)
                path.key = key + path.profundidade
                Fila.append(path)
                boardVisited.add(path.map[:])
                if path.profundidade > ProfundidadeMaxima:
                    ProfundidadeMaxima = 1 + ProfundidadeMaxima


# Heuristic: distance to root numbers
valores_heuristico_0 = [0, 1, 2, 1, 2, 3, 2, 3, 4]
valores_heuristico_1 = [1, 0, 1, 2, 1, 2, 3, 2, 3]
valores_heuristico_2 = [2, 1, 0, 3, 2, 1, 4, 3, 2]
valores_heuristico_3 = [1, 2, 3, 0, 1, 2, 1, 2, 3]
valores_heuristico_4 = [2, 1, 2, 1, 0, 1, 2, 1, 2]
valores_heuristico_5 = [3, 2, 1, 2, 1, 0, 3, 2, 1]
valores_heuristico_6 = [2, 3, 4, 1, 2, 3, 0, 1, 2]
valores_heuristico_7 = [3, 2, 3, 2, 1, 2, 1, 0, 1]
valores_heuristico_8 = [4, 3, 2, 3, 2, 1, 2, 1, 0]


def Heuristic(No):
    global valores_heuristico_0, valores_heuristico_1, valores_heuristico_2, valores_heuristico_3, valores_heuristico_4, valores_heuristico_5, valores_heuristico_6, valores_heuristico_7, valores_heuristico_8
    v0 = valores_heuristico_0[No.index("0")]
    v1 = valores_heuristico_1[No.index("1")]
    v2 = valores_heuristico_2[No.index("2")]
    v3 = valores_heuristico_3[No.index("3")]
    v4 = valores_heuristico_4[No.index("4")]
    v5 = valores_heuristico_5[No.index("5")]
    v6 = valores_heuristico_6[No.index("6")]
    v7 = valores_heuristico_7[No.index("7")]
    v8 = valores_heuristico_8[No.index("8")]
    valorTotal = v0 + v1 + v2 + v3 + v4 + v5 + v6 + v7 + v8
    return valorTotal


# Obtain Sub Nos********************************************************
def subNos(No):
    global NosVisitados
    NosVisitados = NosVisitados + 1

    nextPaths = []
    nextPaths.append(estado_puzzle(direcao(No.estado, 1), No, 1, No.profundidade + 1, No.custo + 1, 0))
    nextPaths.append(estado_puzzle(direcao(No.estado, 2), No, 2, No.profundidade + 1, No.custo + 1, 0))
    nextPaths.append(estado_puzzle(direcao(No.estado, 3), No, 3, No.profundidade + 1, No.custo + 1, 0))
    nextPaths.append(estado_puzzle(direcao(No.estado, 4), No, 4, No.profundidade + 1, No.custo + 1, 0))
    Nos = []
    for procPaths in nextPaths:
        if (procPaths.estado != None):
            Nos.append(procPaths)
    return Nos


# Next step**************************************************************
def direcao(estado, direcao):
    # generate a copy
    novoEstado = estado[:]

    # obtain poss of 0
    index = novoEstado.index(0)

    if (index == 0):
        if (direcao == 1):
            return None
        if (direcao == 2):
            temp = novoEstado[0]
            novoEstado[0] = novoEstado[3]
            novoEstado[3] = temp
        if (direcao == 3):
            return None
        if (direcao == 4):
            temp = novoEstado[0]
            novoEstado[0] = novoEstado[1]
            novoEstado[1] = temp
        return novoEstado
    if (index == 1):
        if (direcao == 1):
            return None
        if (direcao == 2):
            temp = novoEstado[1]
            novoEstado[1] = novoEstado[4]
            novoEstado[4] = temp
        if (direcao == 3):
            temp = novoEstado[1]
            novoEstado[1] = novoEstado[0]
            novoEstado[0] = temp
        if (direcao == 4):
            temp = novoEstado[1]
            novoEstado[1] = novoEstado[2]
            novoEstado[2] = temp
        return novoEstado
    if (index == 2):
        if (direcao == 1):
            return None
        if (direcao == 2):
            temp = novoEstado[2]
            novoEstado[2] = novoEstado[5]
            novoEstado[5] = temp
        if (direcao == 3):
            temp = novoEstado[2]
            novoEstado[2] = novoEstado[1]
            novoEstado[1] = temp
        if (direcao == 4):
            return None
        return novoEstado
    if (index == 3):
        if (direcao == 1):
            temp = novoEstado[3]
            novoEstado[3] = novoEstado[0]
            novoEstado[0] = temp
        if (direcao == 2):
            temp = novoEstado[3]
            novoEstado[3] = novoEstado[6]
            novoEstado[6] = temp
        if (direcao == 3):
            return None
        if (direcao == 4):
            temp = novoEstado[3]
            novoEstado[3] = novoEstado[4]
            novoEstado[4] = temp
        return novoEstado
    if (index == 4):
        if (direcao == 1):
            temp = novoEstado[4]
            novoEstado[4] = novoEstado[1]
            novoEstado[1] = temp
        if (direcao == 2):
            temp = novoEstado[4]
            novoEstado[4] = novoEstado[7]
            novoEstado[7] = temp
        if (direcao == 3):
            temp = novoEstado[4]
            novoEstado[4] = novoEstado[3]
            novoEstado[3] = temp
        if (direcao == 4):
            temp = novoEstado[4]
            novoEstado[4] = novoEstado[5]
            novoEstado[5] = temp
        return novoEstado
    if (index == 5):
        if (direcao == 1):
            temp = novoEstado[5]
            novoEstado[5] = novoEstado[2]
            novoEstado[2] = temp
        if (direcao == 2):
            temp = novoEstado[5]
            novoEstado[5] = novoEstado[8]
            novoEstado[8] = temp
        if (direcao == 3):
            temp = novoEstado[5]
            novoEstado[5] = novoEstado[4]
            novoEstado[4] = temp
        if (direcao == 4):
            return None
        return novoEstado
    if (index == 6):
        if (direcao == 1):
            temp = novoEstado[6]
            novoEstado[6] = novoEstado[3]
            novoEstado[3] = temp
        if (direcao == 2):
            return None
        if (direcao == 3):
            return None
        if (direcao == 4):
            temp = novoEstado[6]
            novoEstado[6] = novoEstado[7]
            novoEstado[7] = temp
        return novoEstado
    if (index == 7):
        if (direcao == 1):
            temp = novoEstado[7]
            novoEstado[7] = novoEstado[4]
            novoEstado[4] = temp
        if (direcao == 2):
            return None
        if (direcao == 3):
            temp = novoEstado[7]
            novoEstado[7] = novoEstado[6]
            novoEstado[6] = temp
        if (direcao == 4):
            temp = novoEstado[7]
            novoEstado[7] = novoEstado[8]
            novoEstado[8] = temp
        return novoEstado
    if (index == 8):
        if (direcao == 1):
            temp = novoEstado[8]
            novoEstado[8] = novoEstado[5]
            novoEstado[5] = temp
        if (direcao == 2):
            return None
        if (direcao == 3):
            temp = novoEstado[8]
            novoEstado[8] = novoEstado[7]
            novoEstado[7] = temp
        if (direcao == 4):
            return None
        return novoEstado


# MAIN**************************************************************
def main():
    global objetivoNo

    # a = [1,8,2,3,4,5,6,7,0]
    # point=Heuristic(a)
    # print(point)
    # return

    # info = "6,1,8,4,0,2,7,3,5" #20
    # info = "8,6,4,2,1,3,5,7,0" #26

    # Obtain information from calling parameters
    parser = argparse.ArgumentParser()
    parser.add_argument('method')
    parser.add_argument('initialBoard')
    args = parser.parse_args()
    data = args.initialBoard.split(",")

    # Build initial board estado
    EstadoInicial = []
    EstadoInicial.append(int(data[0]))
    EstadoInicial.append(int(data[1]))
    EstadoInicial.append(int(data[2]))
    EstadoInicial.append(int(data[3]))
    EstadoInicial.append(int(data[4]))
    EstadoInicial.append(int(data[5]))
    EstadoInicial.append(int(data[6]))
    EstadoInicial.append(int(data[7]))
    EstadoInicial.append(int(data[8]))

    # Start operation
    start = timeit.default_timer()

    function = args.method
    if (function == "bfs"):
        bfs(EstadoInicial)
    if (function == "dfs"):
        dfs(EstadoInicial)
    if (function == "ast"):
        ast(EstadoInicial)

    stop = timeit.default_timer()
    time = stop - start

    # Save total path result
    deep = objetivoNo.profundidade
    direcoes = []
    while EstadoInicial != objetivoNo.estado:
        if objetivoNo.direcao == 1:
            path = 'Up'
        if objetivoNo.direcao == 2:
            path = 'Down'
        if objetivoNo.direcao == 3:
            path = 'Left'
        if objetivoNo.direcao == 4:
            path = 'Right'
        direcoes.insert(0, path)
        objetivoNo = objetivoNo.vizinho

    # '''
    # Print results
    print("path: ", direcoes)
    print("custo: ", len(direcoes))
    print("Nos Visitados: ", str(NosVisitados))
    print("search_profundidade: ", str(deep))
    print("ProfundidadeMaxima: ", str(ProfundidadeMaxima))
    print("running_time: ", format(time, '.8f'))
    # '''

if __name__ == '__main__':
    main()
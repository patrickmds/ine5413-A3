from collections import deque
from itertools import combinations
from grafo import Grafo

def edmonds_karp(grafo, v_inicial, v_sorvedouro):
    
    rede_residual = [[None for x in range(grafo.qtd_vertices())] for y in range(grafo.qtd_vertices())]
    
    for u in range(len(grafo.arestas)):
        for v in range(len(grafo.arestas[u])):
            if grafo.arestas[u][v] != None:
                rede_residual[u][v] = 0


    caminho_aumentante = busca_em_largura_fluxo(grafo,v_inicial, v_sorvedouro, rede_residual)

    total_caminhos = 0
    fluxo_maximo = 0
    while caminho_aumentante != None:
        fluxos = []
        # print("Fluxo do caminho:", end=" ")
        for i in range(len(caminho_aumentante)-1):
            IN = caminho_aumentante[i+1]
            OUT = caminho_aumentante[i]
            fluxo = grafo.arestas[IN][OUT] - rede_residual[IN][OUT]
            # print(f"{fluxo}", end="-")
            fluxos.append(fluxo)

        fluxo_caminho = minimo(fluxos)
        # print(f"= {fluxo_caminho}")
        fluxo_maximo += fluxo_caminho

        for i in range(len(caminho_aumentante)-1):
            IN = caminho_aumentante[i+1]
            OUT = caminho_aumentante[i]

            rede_residual[IN][OUT] += fluxo_caminho
        
        total_caminhos += 1
        caminho_aumentante = busca_em_largura_fluxo(grafo,v_inicial, v_sorvedouro, rede_residual)
        
    # print(f"Total de caminhos: {total_caminhos}")
    # print(f"Fluxo máximo: {fluxo_maximo}")
    return fluxo_maximo

def hopcroft_karp(grafo):
    distancias = [float("inf") for x in range(len(grafo.vertices))]
    mates = [None for x in range(len(grafo.vertices))]
    distNone = [0]

    X = (int)(grafo.qtd_vertices()/2 - 1)
    m = 0
    while(busca_em_largura_emparelhamento(grafo, mates, distancias, distNone)):
        for x in range(X+1):
            if mates[x] == None:
                if busca_em_profundidade_emparelhamento(grafo, mates, x, distancias, distNone):
                    m += 1

    print(f"Emparelhamento máximo: {m}")
    return mates

def busca_em_largura_fluxo(grafo, v_inicial, v_sorvedouro, rede_residual):
    visitados = [False for x in range(len(grafo.vertices))]
    antecessores = [None for x in range(len(grafo.vertices))]

    visitados[v_inicial] = True

    fila = []
    fila.append(v_inicial)

    while(len(fila) > 0):
        u = fila.pop()
        for v in range(len(grafo.arestas[u])):
            if grafo.arestas[u][v] is None or v == u or (grafo.arestas[u][v] - rede_residual[u][v] <= 0):
                continue
            elif visitados[v] == False:
                visitados[v] = True
                antecessores[v] = u
                
                if v == v_sorvedouro:
                    caminho_aumentante = []
                    while v != None:
                        caminho_aumentante.append(v)
                        v = antecessores[v]
                    return caminho_aumentante
                
                fila.append(v)
                

    return None

def minimo(valores):
    if valores == None or len(valores)<1:
        print("Erro ao retornar valor mínimo")
        return None

    resultado = valores[0]
    for valor in valores:
        if valor < resultado:
            resultado = valor

    return resultado


def busca_em_largura_emparelhamento(grafo, mates, distancias, distNone):
    Q = []
    X = (int)(grafo.qtd_vertices()/2 - 1)

    INF = float("inf")

    for x in range(X+1):
        if mates[x]== None:
            distancias[x] = 0
            Q.append(x)
        else:
            distancias[x] = INF

    distNone[0] = INF
    while len(Q) > 0:
        x = Q.pop()
        if distancias[x] < distNone[0]: 
            for y in grafo.vizinhos(x):
                if mates[y] == None:
                    if distNone[0] == INF:
                        distNone[0] = distancias[x] + 1
                else:
                    if distancias[mates[y]] == INF:
                        distancias[mates[y]] = distancias[x] + 1
                        Q.append(mates[y])

    return distNone[0] != INF      

def busca_em_profundidade_emparelhamento(grafo, mates, x, distancias, distNone):
    INF = float("inf")
    
    if x != None:
        for y in grafo.vizinhos(x):
            if mates[y] == None:
                if distNone[0] == distancias[x] + 1:
                    if busca_em_profundidade_emparelhamento(grafo, mates, mates[y], distancias, distNone):
                        # mates[y] = x
                        mates[x] = y
                        return True
            else:
                if distancias[mates[y]] == distancias[x] + 1:
                    if busca_em_profundidade_emparelhamento(grafo, mates, mates[y], distancias, distNone):
                        mates[y] = x
                        mates[x] = y
                        return True
        distancias[x] = INF
        return False

    return True

def lawler(grafo):
    X = [n for n in range(2**grafo.qtd_vertices())]

    S = conjunto_potencia_ordenado(list(grafo.vertices.keys()))
    #for x in S:
    #    print(x)

    for indice, s in enumerate(S):
        if indice == 0:
            X[0] = 0
            continue
        X[indice] = float('inf')
        G = sub_grafo(grafo, s)

        for I in conjuntos_independentes_maximais(G):
            s_copy = s.copy()
            for v in I:
                if v in s_copy:
                    s_copy.remove(v)
            i = S.index(s_copy)

            if X[i] +1 < X[indice]:
                X[indice] = X[i] + 1

    #    X[indice] = float("inf")
    #    print(indice)
    #    print(X)
    #    pass
    return X[-1]

def conjunto_potencia_ordenado(valores):
    entradas = (list(y) for n in range(len(valores) + 1) for y in combinations(valores, n))
    def indice_binario(s):
        return sum(2 ** list(reversed(valores)).index(y) for y in s)

    return sorted(entradas, key=indice_binario)

def sub_grafo(grafo, entradas):
    vertices = {chave: grafo.vertices[chave] for chave in entradas}
    indice_vertices = {grafo.vertices[chave]: chave for chave in entradas}
    arestas = [[grafo.arestas[x][y] if x in entradas and y in entradas else None for x in range(max(vertices)+1)] for y in range(max(vertices)+1)]

    return Grafo(vertices, indice_vertices, arestas, grafo.dirigido)

def conjuntos_independentes_maximais(grafo):

    conjuntos = list()
    for v in grafo.vertices:
        conj_max = set()

        for u in grafo.vertices:
            if grafo.arestas[v][u] is None:
                conj_max.add(u)

        to_remove = list()
        for x in conj_max:
            for y in conj_max:
                if x == y:
                    continue
                if x in to_remove:
                    continue
                if grafo.arestas[x][y] is not None:
                    to_remove.append(y)

        for x in to_remove:
            conj_max.discard(x)

        is_subset = False
        for c in conjuntos:
            if conj_max.issubset(c):
                is_subset = True
                break


        if is_subset:
            continue

        conjuntos.append(conj_max)
    return conjuntos
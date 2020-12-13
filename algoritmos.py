from collections import deque
from itertools import combinations
from grafo import Grafo

def edmonds_karp(grafo):
    return

def hopkroft_karp(grafo):
    return

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

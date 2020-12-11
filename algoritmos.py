from collections import deque
from itertools import combinations
from grafo import Grafo

def edmonds_karp(grafo):
    return

def hopkroft_karp(grafo):
    return

def coloracao(grafo):
    X = [n for n in range(2**grafo.qtd_vertices())]

    S = conjunto_potencia_ordenado(list(grafo.vertices.keys()))
    #for x in S:
    #    print(x)

    for indice, s in enumerate(S):
        if indice == 0:
            X[0] = 0
            continue
        G = sub_grafo(grafo, s)
        print(G)
    #    X[indice] = float("inf")
    #    print(indice)
    #    print(X)
    #    pass
    return

def conjunto_potencia_ordenado(valores):
    entradas = (list(y) for n in range(len(valores) + 1) for y in combinations(valores, n))
    def indice_binario(s):
        return sum(2 ** list(reversed(valores)).index(y) for y in s)

    return sorted(entradas, key=indice_binario)

def sub_grafo(grafo, entradas):
    vertices = {chave: grafo.vertices[chave] for chave in entradas}
    indice_vertices = {grafo.vertices[chave]: chave for chave in entradas}
    arestas = [[grafo.arestas[x][y] if x in entradas and y in entradas else None for x in range(len(vertices))] for y in range(len(vertices))]

    return Grafo(vertices, indice_vertices, arestas, grafo.dirigido)

def subconjunto_independentes_maximais(grafo):
    return

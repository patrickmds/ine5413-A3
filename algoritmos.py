from collections import deque
from grafo import Grafo

def edmonds_karp(grafo, v_inicial, v_sorvedouro):
    
    rede_residual = [[None for x in range(grafo.qtd_vertices())] for y in range(grafo.qtd_vertices())]
    
    for u in range(len(grafo.arestas)):
        for v in range(len(grafo.arestas[u])):
            if grafo.arestas[u][v] != None:
                rede_residual[u][v] = 0


    busca_em_largura_alt(grafo,v_inicial, v_sorvedouro, rede_residual)
    return

def hopcroft_karp(grafo):
    return

def coloracao(grafo):
    return

def busca_em_largura_alt(grafo, v_inicial, v_sorvedouro, rede_residual):
    visitados = [False for x in range(len(grafo.vertices))]
    antecessores = [None for x in range(len(grafo.vertices))]

    visitados[v_inicial] = True

    fila = []
    fila.append(v_inicial)

    while(len(fila) > 0):
        u = fila.pop()
        print(f"Visitando {u}")
        for v in range(len(grafo.arestas[u])):
            if grafo.arestas[u][v] is None:
                # print(f"Aresta[{u}][{v}] não existente...[]")
                continue
            elif v == u:
                print("v==u")
            elif (grafo.arestas[u][v] - rede_residual[u][v] <= 0):
                print("Bagulhos sinistros")
            elif visitados[v] == False:
                visitados[v] = True
                antecessores[v] = u
                
                if v == v_sorvedouro:
                    print("Sorvedouro encontrado. Criando caminho aumentante...")
                    caminho_aumentante = []
                    while v != None:
                        caminho_aumentante.append(v)
                        print(f"{v}", end=" -> ")
                        v = antecessores[v]
                    print("end")
                    return caminho_aumentante
                
                print(f"Check {v} como visitado")
                fila.append(v)
            else:
                print("QUEEEEEEEEEEEE")

    return None
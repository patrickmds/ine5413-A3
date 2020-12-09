from collections import deque
from grafo import Grafo

def edmonds_karp(grafo, v_inicial, v_sorvedouro):
    
    rede_residual = [[None for x in range(grafo.qtd_vertices())] for y in range(grafo.qtd_vertices())]
    
    for u in range(len(grafo.arestas)):
        for v in range(len(grafo.arestas[u])):
            if grafo.arestas[u][v] != None:
                rede_residual[u][v] = 0


    caminho_aumentante = busca_em_largura_alt(grafo,v_inicial, v_sorvedouro, rede_residual)

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
        caminho_aumentante = busca_em_largura_alt(grafo,v_inicial, v_sorvedouro, rede_residual)
        
    # print(f"Total de caminhos: {total_caminhos}")
    # print(f"Fluxo máximo: {fluxo_maximo}")
    return fluxo_maximo

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
        for v in range(len(grafo.arestas[u])):
            if grafo.arestas[u][v] is None or v == u or (grafo.arestas[u][v] - rede_residual[u][v] <= 0):
                continue
            elif visitados[v] == False:
                visitados[v] = True
                antecessores[v] = u
                
                if v == v_sorvedouro:
                    # print("Sorvedouro encontrado. Criando caminho aumentante...")
                    caminho_aumentante = []
                    while v != None:
                        caminho_aumentante.append(v)
                        # print(f"{v}", end="-")
                        v = antecessores[v]
                    # print("end")
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
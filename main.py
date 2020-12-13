from grafo import Grafo
import algoritmos

def main():

    # As variáveis abaixo representam os nomes dos arquivos contendo os grafos para cada exercício da atividade, sendo:
    #
    # - ARQUIVO_1 usado para testar Edmonds-Karp
    # - ARQUIVO_2 usado para testar Hopcroft-Karp
    # - ARQUIVO_3 usado para testar o algoritmo de coloração de vértices
    #
    # Para usar outros arquivos, basta apenas substituir o nome nas variáveis abaixo

    ARQUIVO_1 = "ex_grafo_1.txt" # Trocar para o nome do arquivo usado no exercício 1, dirigido e ponderado
    ARQUIVO_2 = "ex_grafo_1.txt" # Trocar para o nome do arquivo usado no exercício 2, grafo bipartido, não-dirigido e não-ponderado
    ARQUIVO_3 = "ex_grafo_2.txt" # Trocar para o nome do arquivo usado no exercício 3, não-dirigido e não-ponderado

    print("------------------------------------------")
    print("Exercício 1: Edmonds-Karp ")
    print("------------------------------------------")

    grafo = Grafo()
    grafo.ler(ARQUIVO_1)

    algoritmos.edmonds_karp(grafo)

    print("\n")

    print("------------------------------------------")
    print("Exercício 2: Hopcroft-Karp")
    print("------------------------------------------")

    grafo = Grafo()
    grafo.ler(ARQUIVO_2)

    algoritmos.hopkroft_karp(grafo)

    print("\n")

    print("------------------------------------------")
    print("Exercício 3: Coloração dos vertices")
    print("------------------------------------------")

    grafo = Grafo()
    grafo.ler(ARQUIVO_3)

    print(algoritmos.lawler(grafo))
    algoritmos.conjuntos_independentes_maximais(grafo)



if __name__ == "__main__":
    main()

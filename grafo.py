class Grafo:

    def __init__(self, vertices=dict(), indice_vertices=dict(), arestas=list(), dirigido=False):
        # Vertices é um dicionário onde a chave é o índice e o valor é o rótulo do vértice
        self.vertices = vertices

        # indice_vertices é um dicionário onde a chave é o rotulo e o valor é o indice do vértice
        self.indice_vertices = indice_vertices

        # Arestas é uma matriz de Vertice pra vertice onde o valor é o peso da aresta
        self.arestas = arestas

        self.dirigido = dirigido

    # Retorna o número de Vertices do grafo
    def qtd_vertices(self):
        return len(self.vertices)

    # Retorna o número de arestas do grafo
    def qtd_arestas(self):
        qtd = 0
        for v in self.arestas:
            qtd += sum(a != None for a in v)

        if self.dirigido:
            return qtd
        # divido por 2, porque a (x, y) e (y, x) são consideradas a mesma aresta
        return qtd/2

    # Esse método deveria printar uma moto fazendo um grau e o numero de vizinhos do vertice V
    def grau(self, v):
        return len(self.vizinhos(v))

    # Retorna o rótulo do vertice V passado por parâmetro como índice
    def rotulo(self, v):
        return self.vertices[v]

    def vizinhos(self, v):
        vertices_vizinhos = list()

        for u in range(len(self.arestas[v])):
            if self.arestas[v][u] != None:
                vertices_vizinhos.append(u)

        return vertices_vizinhos

    # Retorna True se tiver uma aresta ligando os vertices u e v
    def ha_aresta(self, u, v):
    	return self.arestas[u][v] != None

    def peso(self, u, v):
    	return self.arestas[u][v]

    def ler(self, filename):
        if len(self.vertices) != 0:
            read = ''
            while read != 'y' or read != 'n':
                print("Grafo já existente, deseja continuar?(y/n): ")
                read = input()

                if read.lower() == 'y':
                    break

                if read.lower() == 'n':
                    print("Leitura cancelada")
                    return

        with open(filename) as f:
            lines = f.readlines()

        num_vertices = int(lines[0].replace('\n', '').split(' ')[1])
        self.vertices = dict()
        self.arestas = [[None for x in range(num_vertices)] for y in range(num_vertices)]

        self.dirigido = lines[num_vertices+1].split("*")[1].replace("\n", "") == "arcs"

        for line in lines[1:num_vertices+1]:
            line = line.replace('\n', '').split(' ')

            indice = int(line[0])
            rotulo = line[1].lower()

            self.vertices[indice-1]= rotulo
            #self.indice_vertices[rotulo] = indice

        for line in lines[num_vertices+2:]:
            line = line.replace('\n', '').split(' ')

            u = int(line[0])-1
            v = int(line[1])-1

            if len(line) > 2:
                peso = float(line[2])
            else:
                peso = 1

            self.arestas[u][v] = peso
            if not self.dirigido:
                self.arestas[v][u] = peso


    def printar_matriz_adj(self):
        vertices = list(self.vertices.values())

        header = "  |"
        for rotulo in vertices:
            header += f" {rotulo} "
        print(header)
        print('='*len(header))

        for indice, linha in enumerate(self.arestas):
            string = f"{self.vertices[indice]} |"
            for peso in linha:
                string += f" {'-' if peso == None else peso} "
            print(string)

    def arestas_transpostas(self):
        arestas_transpostas = [[None for x in range(self.qtd_vertices())] for y in range(self.qtd_vertices())]

        for u in range(self.qtd_vertices()):
            for v in range(self.qtd_vertices()):
                if not self.arestas[u][v] is None:
                    arestas_transpostas[v][u] = self.arestas[u][v]

        return arestas_transpostas







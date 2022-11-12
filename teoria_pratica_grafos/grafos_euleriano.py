"""
Grafo Euleriano -> Um grafo será Euleriano se existe uma trilha(Passei) fechada (Não repte arestas/começa e termina
no mesmo vertice) que passa por todas as arestas de G

Grafo semi Euleriano -> Um grafo será Semi Euleriano se existe uma trilha(Passei) aberta (Não repte arestas/começa e termina
em vertices diferentes) que passa por todas as arestas de G

Teorema de Euler -> Um grafo conexo G é Euleriano se, e somente se, todos os seus vertices tem grau par
Teorema 4 -> Um grafo conexo G é semiEuliriano se, e somente se, G tem dois vertices de Grau ímpar -> (Tem que começar em no vertice de grau impar
e terminar no outro de grau impar para fazer o caminho)

Grafo de Hamiltoniano -> Um ciclo (Não repete aresta/ não repete vertice/ começa e termina no mesmo lugar), que passa por todos os vertices de G

"""

class MatriAdj():

    def __init__(self, vertices):
        #self.vertices = [] # Lista de vertices
        self.vertices = vertices
        self.aresta = [] # Lista de Arestas
        self.matriz = [[0] * self.vertices for i in range(self.vertices)] # Matriz de Adjacencia

    def addAresta(self, u, v):
        """Não direcionado"""
        """Se tiver peso, podemos colocar os pesos no lugar do 1 ou criar uma matriz de peso"""

        self.matriz[u-1][v-1] += 1 # esse + e para caso tenha mais de uma aresta ligado os dois
        
        # Esse if e para caso tenha laço(laço sai e chega nele mesmo)
        if u != v:
            self.matriz[v-1][u-1] += 1

    def mostraMatriz(self):
        print("A Matriz de Adjacencia")
        for i in range(self.vertices):
            print(self.matriz[i])
    
    def isAresta(self, u, v):
        if self.matriz[u-1][v-1] == 0:
            return False
        else:
            return True
    
    def isEuliriano(self):
        #calcular o grau de todos os vertices
        contador_impar = 0
        for i in range(self.vertices):
            grau = 0
            for j in range(self.vertices):
                # Laço tem grau 2
                if i == j:
                    grau = grau + 2 * self.matriz[i][j]
                else:
                    grau += self.matriz[i][j]
            
            if grau % 2 != 0:
                contador_impar += 1
        
        if contador_impar == 0:
            print("Grafo Euleriano")
        elif contador_impar == 2:
            print("Grafo SemiEuliriano")
        else:
            print("Não Euleriano e nem semieuliriano")


g = MatriAdj(4)

g.addAresta(1, 2)
g.addAresta(1, 3)
g.addAresta(3, 4)

g.mostraMatriz()
g.isEuliriano()
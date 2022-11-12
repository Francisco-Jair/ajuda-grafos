# Uma matriz e uma lista dentro de uma lista

# Se tiver laço coloca 1 no valor da diagonal principal

class MatriAdj():

    def __init__(self, vertices):
        #self.vertices = [] # Lista de vertices
        self.vertices = vertices
        self.aresta = [] # Lista de Arestas
        self.matriz = [[0] * self.vertices for i in range(self.vertices)] # Matriz de Adjacencia

    def addAresta(self, u, v):
        """Não direcionado"""
        """Se tiver peso, podemos colocar os pesos no lugar do 1 ou criar uma matriz de peso"""

        self.matriz[u-1][v-1] = 1
        self.matriz[v-1][u-1] = 1

    def busca_em_largura(self, s=1):
        """Na busca em largura usa - se uma fila"""
        path = []
        listVisit = []
        path.append(s-1)

        while len(path) != 0:
            t = path[0]

            listVisit.append(t)
            #print(t)
            path.remove(t)
            #print(len(path))
            for i in range(self.vertices):
                if self.matriz[t][i] == 1 and i not in listVisit and i not in path:
                    path.append(i)

        print(listVisit)


    def busca_profundidade(self, s=1):
        """Na busca em profundidade usa - se uma pilha"""
        
        pilha = []
        visitados = []
        pilha.append(s-1)
        visitados.append(s-1)

        while pilha:
            v = pilha[-1]

            for i in range(self.vertices):
                flag = True
                if self.matriz[v][i] == 1 and i not in visitados:
                    flag = False
                    pilha.append(i)
                    visitados.append(i)
                    break

            if flag:
                pilha.pop()
            
       
        for i in visitados:
            print(i, end=' ')
        
        #print(visitados)

    def mostraMatriz(self):
        print("A Matriz de Adjacencia")
        for i in range(self.vertices):
            print(self.matriz[i])


g = MatriAdj(7)

g.addAresta(1, 5)
g.addAresta(1, 7)
g.addAresta(2, 6)
g.addAresta(2, 5)
g.addAresta(3, 6)
g.addAresta(3, 7)
g.addAresta(4, 5)

#g.busca_em_largura()
g.busca_profundidade()
#g.mostraMatriz()
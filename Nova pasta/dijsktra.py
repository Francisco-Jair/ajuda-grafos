# Soluciona o caminho mais curto

class Graph():

    def __init__(self, vertices):
        self.V = vertices # Numero de vertices
        self.graph = [] # Guarda as arestas com vertices que se relacionam

    #inicio, fim, peso
    def addEdge(self, u, v, w):
        #Coloca esses dois pq não é direcionado
        self.graph.append([u,v,w])
        self.graph.append([v,u,w])

    def minDistancia(self, dist, T):
        min = float('inf') # Marcando como infinito

        for v in range(self.V):
            if dist[v] < min and T[v] == False:
                min = dist[v]
                min_index = v
        
        return min_index
    
    def solution(self, dist):
        print("Vértice de Origem")
        for node in range(self.V):
            print(node, "\t", dist[node])

    def dijsktra(self, src):
        dist = [float("inf")] * self.V
        dist[src] = 0
        T = [False] * self.V

        for count in range(self.V):
            u = self.minDistancia(dist, T)
            for v in range(self.V):
                for item in self.graph:
                    if(item[0]==u) and (item[1]==v):
                        if(item[2]>0 and T[v] == False and dist[v] > dist[u]+item[2]):
                            dist[v] = dist[u]+item[2]
            
            T[u] = True
        self.solution(dist)


g = Graph(9)
g.addEdge(0, 1, 4)
g.addEdge(0, 7, 8)
g.addEdge(1, 2, 8)
g.addEdge(1, 7, 11)
g.addEdge(2, 3, 7)
g.addEdge(2, 5, 4)  
g.addEdge(2, 8, 2)
g.addEdge(3, 5, 14)
g.addEdge(3, 4, 9)
g.addEdge(4, 5, 10)
g.addEdge(5, 6, 2)
g.addEdge(6, 7, 1)
g.addEdge(6, 8, 6)
g.addEdge(7, 8, 7)
g.dijsktra(0)
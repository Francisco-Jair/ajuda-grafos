
class ListaAdj():
    

    def __init__(self, vertices):
        #vertices = [] # Conjunto dos vertices
        #arestas = [] # Conjunto das arestas
        self.vertices = vertices
        self.lista = [[] for i in range(self.vertices)]
    
    def adicionaAresta(self, u, v, peso=0):
        """Grafos não direcionados"""
        """Se tiver peso so add assim [vertice, peso]"""
        self.lista[u-1].append(v-1)
        self.lista[v-1].append(u-1)
    
    def mostrarLista(self):
        #Percorre as linhas
        for i in range(self.vertices):
            print(f'{i}:', end='  ')
            
            #pegar todos os valores de cada linha
            for j in self.lista[i]:
                print(f'{j} ->', end=' ')
            print('')

    def busca_em_profundidade(self, s=1):
        
        pilha = []
        visitados = []
        visitados.append(s-1)
        pilha.append(s-1)

        while pilha:
            t = pilha[-1]
            #visitados.append(t)

            for i in self.lista[t]:
                flag = True
                if i not in visitados:
                    flag = False
                    pilha.append(i)
                    visitados.append(i)
                    break

            if flag == True:
                pilha.pop()

        #print(visitados)
        for i in visitados:
            print(f"{i+1} -> ", end=" ")
        
        print("")
       

    def busca_em_largura(self, s=1):
        
        visitado = []
        path = []
        path.append(s-1)
        
        while path:
            t = path[0]
            path.remove(t)
            visitado.append(t)

            for i in self.lista[t]:
                if i not in visitado and i not in path:
                    path.append(i)

            

        print(visitado)
            
            


g = ListaAdj(8)

g.adicionaAresta(1, 5)
g.adicionaAresta(1, 4)
g.adicionaAresta(2, 3)
g.adicionaAresta(3, 4)
g.adicionaAresta(3, 6)
g.adicionaAresta(4, 5)
g.adicionaAresta(4, 8)
g.adicionaAresta(5, 6)
g.adicionaAresta(5, 7)


#g.busca_em_largura()
g.busca_em_profundidade(8)
g.mostrarLista()

from Graph import Graph, Edge, Vertex
import copy

def sum_edges(graph):
    w_sum = 0
    l = len(graph)
    for i in range(l):
        for j in range(i,l):
            w_sum += graph[i][j]
    return w_sum
            

def dijktra(graph, source, dest):
    shortest = [0 for i in range(len(graph))]
    selected = [source]
    l = len(graph)
    #Base case from source
    inf = 10000000
    min_sel = inf
    for i in range(l):
        if(i==source):
            shortest[source] = 0 #graph[source][source]
        else:
            if(graph[source][i]==0):
                shortest[i] = inf
            else:
                shortest[i] = graph[source][i]
                if(shortest[i] < min_sel):
                    min_sel = shortest[i]
                    ind = i
                
    if(source==dest):
        return 0
    # Dijktra's in Play
    selected.append(ind) 
    while(ind!=dest):
        #print('ind',ind)
        for i in range(l):
            if i not in selected:
                if(graph[ind][i]!=0):
                    #Check if distance needs to be updated
                    if((graph[ind][i] + min_sel) < shortest[i]):
                        shortest[i] = graph[ind][i] + min_sel
        temp_min = 1000000
        #print('shortest:',shortest)
        #print('selected:',selected)
        
        for j in range(l):
            if j not in selected:
                if(shortest[j] < temp_min):
                    temp_min = shortest[j]
                    ind = j
        min_sel = temp_min
        selected.append(ind)
    
    return shortest[dest]
                            
#Finding odd degree vertices in graph

def get_odd(graph):
    degrees = [0 for i in range(len(graph))]
    for i in range(len(graph)):
        for j in range(len(graph)):
                if(graph[i][j]!=0):
                    degrees[i]+=1
                
    #print(degrees)
    odds = [i for i in range(len(degrees)) if degrees[i]%2!=0]
    #print('odds are:',odds)
    return odds

#Function to generate unique pairs
def gen_pairs(odds):
    pairs = []
    for i in range(len(odds)-1):
        pairs.append([])
        for j in range(i+1,len(odds)):
            pairs[i].append([odds[i],odds[j]])
        
    #print('pairs are:',pairs)
    #print('\n')
    return pairs


#Final Compiled Function
def Chinese_Postman(graph):
    odds_vertices = get_odd(graph)
    if(len(odds_vertices)==0):
        return sum_edges(graph)
    vertexes_pairs_list = gen_pairs(odds_vertices)
    l = (len(vertexes_pairs_list)+1)//2
    pairings_sum = []
    def get_pairs(vertexes_pairs, vertexes_done = [], final = []):
        if(vertexes_pairs[0][0][0] not in vertexes_done):
            vertexes_done.append(vertexes_pairs[0][0][0])
            for i in vertexes_pairs[0]:
                finalvertex = final[:]
                value_vertex = vertexes_done[:]
                if(i[1] not in value_vertex):
                    finalvertex.append(i)
                else:
                    continue
                if(len(finalvertex)==l):
                    pairings_sum.append(finalvertex)
                    return 
                else:
                    value_vertex.append(i[1])
                    get_pairs(vertexes_pairs[1:],value_vertex, finalvertex)
        else:
            get_pairs(vertexes_pairs[1:], vertexes_done, final)
    get_pairs(vertexes_pairs_list)
    min_sums = []
    for i in pairings_sum:
        sumtotal = 0
        for j in range(len(i)):
            sumtotal += dijktra(graph, i[j][0], i[j][1])
        min_sums.append(sumtotal)
    added_dis = min(min_sums)
    chinese_dis = added_dis + sum_edges(graph)
    return chinese_dis

class ChinesePostmanAlgorithm:
    
    def __init__(self, graph: Graph):
        self.graph: Graph = graph
    def solve(self):
        # Prepare
        ## Create path to be returned by algorithm
        path = []
        r = None

        # Solve
        ## Check if it is an euler graph
        ### If so, return the euler path as the answer
        success, euler_path = self.graph.findEulerPath(self.graph.edges, self.graph.vertexes, self.graph.vertexes[0])
        if self.graph.isCompleteGraph() and success == True:
            return euler_path
        ### Else
        else:
            # Eulerize the graph
            vertexes = copy.deepcopy(self.graph.vertexes)
            edges = copy.deepcopy(self.graph.edges)
            matrix = []
            for i in range(len(vertexes)):
                line = []
                matrix.append(line)
                for j in range(len(vertexes)):
                    line.append(0)

            id_to_index = {}
            for ind, val in enumerate(vertexes):
                val: Vertex = val
                id_to_index[val.id] = ind
            print(id_to_index)

            for edge in edges:
                edge: Edge = edge
                print(edge)
                con1 = edge.connection[0].id
                con2 = edge.connection[1].id
                pos1 = id_to_index[con1]
                pos2 = id_to_index[con2]
                matrix[pos1][pos2] = edge.weight
                matrix[pos2][pos1] = edge.weight
                print(f"ACTION: {pos1}:{pos2} = {edge.weight}")

            for l in matrix:
                print(l)

            r = Chinese_Postman(matrix)
            print(r)
        
        # Return the algorithm generated path
        return path, r
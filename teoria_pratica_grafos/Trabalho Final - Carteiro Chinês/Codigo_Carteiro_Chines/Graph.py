from typing import Tuple, Union, List
import copy

class Vertex:
    def __init__(self, id: str):
        self.id = id
    def __eq__(self, other):
        if type(self) == type(other):
            return self.id == other.id
        return id(self) == id(other)
    def __str__(self):
        return f"V{self.id}"

class Edge:
    def __init__(self, vertex1: Vertex, vertex2: Vertex, weight: float):
        self.connection = (vertex1, vertex2)
        self.weight = weight
    def __eq__(self, other):
        if type(self) == type(other):
            # Compare edge
            if self.connection[0] == other.connection[0] and self.connection[1] == other.connection[1]:
                return True
            # Compare reversed edge
            elif self.connection[0] == other.connection[1] and self.connection[1] == other.connection[0]:
                return True
            # Both values are different, even with reverse comparation
            else:
                return False
        return False
    def __str__(self):
        return f"{self.connection[0]} <-> {self.connection[1]} : {self.weight} : {id(self)}"

class Graph:
    def __init__(self):
        self.vertexes = []
        self.edges = []

    def getVertex(self, node_id: str) -> Union[Vertex, None]:
        for vertex in self.vertexes:
            vertex: Vertex = vertex
            if vertex.id == node_id:
                return vertex
        return None

    def addVertex(self, node: Vertex) -> bool:
        if node not in self.vertexes:
            self.vertexes.append(node)
            return True
        return False
        
    def getEdge(self, node1: str, node2: str) -> Union[Edge, None]:
        vertex1 = self.getVertex(node1)
        vertex2 = self.getVertex(node2)
        e = Edge(vertex1, vertex2, 0)
        if e in self.edges:
            o = self.edges.index(e)
            return self.edges[o]
        return None

    def addEdge(self, node1: Vertex, node2: Vertex, weight: float) -> bool:
        conn = Edge(node1, node2, weight)
        if conn not in self.edges:
            self.edges.append(conn)
            return True 
        return False

    def getVertexDegree(self, id: str) -> Union[int, None]:
        degree = None
        v = self.getVertex(id)
        if type(v) != type(None):
            degree = 0
            for edge in self.edges:
                edge: Edge = edge
                if edge.connection[0] == v:
                    degree += 1
                elif edge.connection[1] == v:
                    degree += 1
        return degree

    def printGraph(self) -> None:
        print("Vertexes:", [str(a) for a in self.vertexes])
        print("Edges:", [str(a) for a in self.edges])

    def isCompleteGraph(self) -> bool:
        for vertex in self.vertexes:
            vertex: Vertex = vertex
            # Create an array to remaining vertexes
            remaining = copy.deepcopy(self.vertexes)
            remaining.remove(vertex)

            # Create connection and check if they exist in graph
            linked_to_all = True
            for target in remaining:
                target: Vertex = target
                conn = self.getEdge(vertex.id, target.id)
                # Break function if any of the links doesn't exists
                if type(conn) == type(None):
                    linked_to_all = False
                    break
            # Break function if any of the links doesn't exists (this is a check)
            if linked_to_all == False:
                return False
        # Return true, as all vertexes are connected
        return True

    def findEulerPath(self, edges: List[Edge], vertexes: List[Vertex], actualVertex: Vertex, path: List[Vertex] = []) -> Tuple[bool, list]:
        edgelist: List[Edge] = copy.deepcopy(edges)
        path.append(actualVertex)
        targetvertex = None
        targetedge = None
        # Find first edge connection to another vertex
        for edge in edgelist:
            edge: Edge = edge
            if edge.connection[0].id == actualVertex.id:
                targetvertex = edge.connection[1]
                targetedge = edge
                break
            if edge.connection[1].id == actualVertex.id:
                targetvertex = edge.connection[0]
                targetedge = edge
                break
        
        # Remove target edge
        if targetvertex != None and targetedge != None:
            # print(f"{actualVertex} to {targetvertex}")
            edgelist.remove(targetedge)
            self.findEulerPath(edgelist, self.vertexes, targetvertex, path)
        if len(path) == len(self.edges) or len(path) == len(self.edges) - 1:
            return True, path
        return False, path


if __name__ == "__main__":
    g = Graph()
    g.addVertex(Vertex("1"))
    g.addVertex(Vertex("2"))
    g.addVertex(Vertex("3"))
    g.addVertex(Vertex("4"))
    g.addEdge(g.getVertex("1"), g.getVertex("2"), 1)
    g.addEdge(g.getVertex("2"), g.getVertex("3"), 1)
    g.addEdge(g.getVertex("3"), g.getVertex("4"), 1)
    
    print(f"1, 2:", g.getEdge("1", "2"))
    print(f"2, 3:", g.getEdge("2", "3"))
    print(f"3, 4:", g.getEdge("3", "4"))
    print(f"4, 3:", g.getEdge("4", "3"))
    print(f"3, 2:", g.getEdge("3", "2"))
    print(f"2, 1:", g.getEdge("2", "1"))
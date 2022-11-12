from Graph import Graph, Edge, Vertex
import random

CONNECTION_THRESHOLD = 1.0 / 5.0

def generate_complete_graph(vertex_count: int):
    # Create Graph object
    g = Graph()
    # Create Vertexes objects and add them to Graph
    for i in range(vertex_count):
        vertex_id = str(i + 1)
        vertex = Vertex(vertex_id)
        g.addVertex(vertex)
    # Create connections from each vertex at graph to others vertex
    for vertex in g.vertexes:
        for candidate in g.vertexes:
            # Skip actual vertex
            if vertex == candidate:
                continue
            # Always connect a vertice to others
            g.addEdge(vertex, candidate, random.randrange(0, 10))
    return g

def generate_incomplete_graph(vertex_count: int, connection_threshold: float = CONNECTION_THRESHOLD):
    # Create Graph object
    g = Graph()
    # Create Vertexes objects and add them to Graph
    for i in range(vertex_count):
        vertex_id = str(i + 1)
        vertex = Vertex(vertex_id)
        g.addVertex(vertex)
    # Create connections from each vertex at graph to others vertex
    for vertex in g.vertexes:
        for candidate in g.vertexes:
            # Skip actual vertex
            if vertex == candidate:
                continue
            # Use random function to choose if will connect or not
            r = random.random()
            if r >= connection_threshold:
                g.addEdge(vertex, candidate, random.randrange(0, 10))
    return g

if __name__ == "__main__":
    g1 = GraphGenerator.generate_incomplete_graph(5, 0.5)
    g2 = GraphGenerator.generate_complete_graph(5)
    
    print("CG1", g1.isCompleteGraph())
    print("G1P1", [str(i) for i in g1.findEulerPath(g1.edges, g1.vertexes, g1.vertexes[0], [])[1]])
    print("G1P2", [str(i) for i in g1.findEulerPath(g1.edges, g1.vertexes, g1.vertexes[1], [])[1]])
    print("G1P3", [str(i) for i in g1.findEulerPath(g1.edges, g1.vertexes, g1.vertexes[2], [])[1]])
    print("G1P4", [str(i) for i in g1.findEulerPath(g1.edges, g1.vertexes, g1.vertexes[3], [])[1]])
    print("G1P5", [str(i) for i in g1.findEulerPath(g1.edges, g1.vertexes, g1.vertexes[4], [])[1]])

    print("CG2", g2.isCompleteGraph())
    print("G2P1", [str(i) for i in g2.findEulerPath(g2.edges, g2.vertexes, g2.vertexes[0], [])[1]])
    print("G2P2", [str(i) for i in g2.findEulerPath(g2.edges, g2.vertexes, g2.vertexes[1], [])[1]])
    print("G2P3", [str(i) for i in g2.findEulerPath(g2.edges, g2.vertexes, g2.vertexes[2], [])[1]])
    print("G2P4", [str(i) for i in g2.findEulerPath(g2.edges, g2.vertexes, g2.vertexes[3], [])[1]])
    print("G2P5", [str(i) for i in g2.findEulerPath(g2.edges, g2.vertexes, g2.vertexes[4], [])[1]])
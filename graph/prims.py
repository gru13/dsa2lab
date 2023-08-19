from weight_Graph import Graph
from math import inf
def prim(G:Graph,vertex):
    visited  = set()
    cur_min = 0
    visited.add(vertex)
    n = G.numberOfVertices()
    edges_Connected = set()
    result = []
    while len(visited) != n:
        break

    # print(visited,edges_Connected)


G = Graph()

if __name__ == '__main__':
    G.add_vertice("A")
    G.add_vertice("B")
    G.add_vertice("C")
    G.add_vertice("D")
    G.add_vertice("E")
    G.add_vertice("F")

    G.add_edge("A","B",4,un=True)
    G.add_edge("A","C",4,un=True)
    G.add_edge("B","C",2,un=True)

    G.add_edge("C","D",3,un=True)
    G.add_edge("D","F",3,un=True)
    G.add_edge("C","F",4,un=True)
    G.add_edge("C","E",2,un=True)
    G.add_edge("E","F",3,un=True)

    G.Print_adjMat()
    G.Print_adjList()
    print(G.allEdges(un = True))
    # prim(G,"C")


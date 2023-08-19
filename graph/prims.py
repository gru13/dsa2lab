from weight_Graph import Graph
from math import inf


def prim(G: Graph, vertex):
    n = G.numberOfVertices()
    visited_vertice = set()
    visited_edges = set()
    visited_vertice.add(vertex)
    while len(visited_vertice) != n:
        cur_edge = []
        for a in visited_vertice:
            cur_edge += G.edgesOf(a, n=True)
        # l1 = len(visited_edges)
        # l2 = len(visited_vertice)
        cur_edge = set(cur_edge) - visited_edges
        cur_edge = list(cur_edge)
        cur_edge = list(sorted(cur_edge, key=lambda x:x[-1]))
        visited_vertice.add(cur_edge[0][0])
        visited_vertice.add(cur_edge[0][1])
        visited_edges.add((cur_edge[0][0],cur_edge[0][1],cur_edge[0][2]))
        visited_edges.add((cur_edge[0][1],cur_edge[0][0],cur_edge[0][2]))
        # if l1 != len(visited_edges) and l2 != len(visited_vertice):
        print(cur_edge[0])
        # print(cur_edge)
        # print(visited_vertice)
        # break



G = Graph()

if __name__ == '__main__':
    G.add_vertice("A")
    G.add_vertice("B")
    G.add_vertice("C")
    G.add_vertice("D")
    G.add_vertice("E")
    G.add_vertice("F")

    G.add_edge("A", "B", 4, un=True)
    G.add_edge("A", "C", 4, un=True)
    G.add_edge("B", "C", 2, un=True)

    G.add_edge("C", "D", 3, un=True)
    G.add_edge("D", "F", 3, un=True)
    G.add_edge("C", "F", 4, un=True)
    G.add_edge("C", "E", 2, un=True)
    G.add_edge("E", "F", 3, un=True)

    # G.Print_adjMat()
    # G.Print_adjList()
    # print(G.allEdges(un = True))
    prim(G, "C")

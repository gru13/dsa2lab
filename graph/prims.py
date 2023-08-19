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

        cur_edge = set(cur_edge) - visited_edges
        cur_edge = list(cur_edge)

        cur_edge = list(sorted(cur_edge, key=lambda x:x[-1]))
        while (cur_edge[0][1] in visited_vertice and cur_edge[0][0] in visited_vertice):
            cur_edge.pop(0)

        v1 = cur_edge[0][0]
        v2 = cur_edge[0][1]
        w = cur_edge[0][-1]
        if v2 in visited_vertice and v1 in visited_vertice:
            visited_edges.add((v1,v2,w))
            visited_edges.add((v2,v1,w))
        else:
            visited_vertice.add(v2)
            visited_vertice.add(v1)
            visited_edges.add((v1,v2,w))
            visited_edges.add((v2,v1,w))
            yield cur_edge[0]

        # print(visited_edges)




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
    pt = prim(G, "C")
    print()
    print()
    print()
    print(list(pt), sep="\n")

from weight_Graph import Graph
from ds import DisjointSet


def kruskal(G: Graph):
    edges = G.allEdges()
    disSet = DisjointSet(G.Vertices())
    n = G.numberOfVertices()
    visted_edges = set()
    visted_vertices = set()
    edges.sort(key=lambda x: x[-1])
    while n != len(visted_vertices):
        min_ = edges.pop(0)
        if not (min_ in visted_edges and (min_[1], min_[0], min_[-1]) in visted_edges) and (disSet.find(min_[0]) != disSet.find(min_[1])):
            yield min_
            visted_edges.add(min_)
            visted_edges.add((min_[1], min_[0], min_[-1]))
            edges.remove((min_[1], min_[0], min_[-1]))
            disSet.union(min_[0], min_[1])
            visted_vertices.add(min_[0])
            visted_vertices.add(min_[1])


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
    # print(G.allEdges())
    k = list(kruskal(G))
    print(k, sep="\n")

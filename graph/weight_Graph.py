from math import inf


class Graph:
    def __init__(self, graph: dict = {}) -> None:
        self.__graph: dict = graph

    def add_vertice(self, vertice):
        if vertice in self.__graph.keys():
            return
        else:
            self.__graph[vertice] = []

    def add_edge(self, _from, _to, weigth, un=False):
        if _from in self.__graph.keys() and _to in self.__graph.keys():
            self.__graph[_from].append((_to, weigth))
            if un == True:
                self.__graph[_to].append((_from, weigth))
        else:
            return

    def edgesOf(self, vertice):
        if vertice in self.__graph.keys():
            return self.__graph[vertice]
        else:
            return None

    def numberOfVertices(self):
        return len(self.__graph)

    def isVertice(self, vertice) -> bool:
        if vertice in self.__graph.keys():
            return True
        else:
            return False

    def Vertices(self):
        return list(self.__graph.keys())

    def adjcent_list(self):
        return self.__graph

    def adjcent_mat(self):
        n = self.numberOfVertices()
        keys: list = self.Vertices()
        mat = [[0 for a in range(n)] for _ in range(n)]
        for a in range(n):
            for b in self.edgesOf(keys[a]):
                mat[a][keys.index(b[0])] = b[1]
        for a in range(n):
            for b in range(n):
                if mat[a][b] == 0:
                    if a == b:
                        mat[a][b] = 0
                    else:
                        mat[a][b] = inf
        return keys, mat

    def Print_adjMat(self):
        k, m = self.adjcent_mat()
        print("Adjcent Matrix:")
        print("key :", k)
        print("--------------------")
        for a in m:
            print(a)
        print("--------------------")

    def Print_adjList(self):
        print("Adjcent List:")
        print("--------------------")
        for a in self.__graph:
            print(a, ':', self.__graph[a])
        print("--------------------")


if __name__ == '__main__':
    # g = Graph()
    # g.add_vertice(1)
    # g.add_vertice(2)
    # g.add_vertice(3)
    # g.add_edge(1, 1)
    # g.add_edge(1, 3)
    # g.add_vertice(4)
    # g.add_edge(4, 3)
    # g.Print_adjList()
    # g.Print_adjMat()
    # pass
    G = Graph()
    G.add_vertice(1)
    G.add_vertice(2)
    G.add_vertice(3)
    G.add_vertice(4)
    # G.add_vertice(5)

    G.add_edge(1, 2, 5, un=True)
    G.add_edge(1, 3, 5, un=True)
    G.add_edge(2, 3, 5)
    G.add_edge(4,4,8)
    # G.add_edge(4, 2, 5)
    # G.add_edge(4, 3, 5)
    # G.add_edge(4, 5, 5)

    # G.adjcent_mat()
    G.Print_adjMat()
    # print(G.adjcent_list())
class Graph:
    def __init__(self, graph: dict = {}) -> None:
        self.__graph: dict = graph

    def add_vertice(self, vertice):
        if vertice in self.__graph.keys():
            return
        else:
            self.__graph[vertice] = []

    def add_edge(self, _from, _to, weigth):
        if _from in self.__graph.keys() and _to in self.__graph.keys():
            self.__graph[_from] = (_to, weigth)

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
        mat = []
        

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

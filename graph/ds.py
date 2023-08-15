class stack:
    def __init__(self, Stack=[]) -> None:
        self.__stack: list = Stack

    def push(self, val) -> None:
        self.__stack.append(val)

    def pop(self):
        return self.__stack.pop()

    def display(self) -> None:
        for a in self.__stack:
            print(a, end="->")
        print()


class queue:
    def __init__(self, Queue=[]) -> None:
        self.__Queue: list = Queue

    def push(self, val) -> None:
        self.__Queue.append(val)

    def pop(self):
        return self.__Queue.pop(0)

    def display(self) -> None:
        for a in self.__Queue:
            print(a, end="->")
        print()


class Graph:
    """
        This is a Unweigth,undirected graph
    """

    def __init__(self, graph={}) -> None:
        self.__graph: dict = graph

    def add_vertice(self, vertice: int):
        if vertice not in self.__graph.keys():
            self.__graph[vertice] = []

    def add_edge(self, _from, _to):
        if (_from not in self.__graph.keys() or _to not in self.__graph.keys()):
            return
        self.__graph[_from].append(_to)
        if _from != _to:
            self.__graph[_to].append(_from)

    def adjcent_mat(self):
        key: list = list(self.__graph.keys())
        mat = [[0 for _ in range(len(key))] for _ in range(len(key))]
        for a in key:
            for b in self.__graph[a]:
                mat[key.index(a)][key.index(b)] = 1
        return key, mat

    def adjcent_list(self):
        return self.__graph

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
    g = Graph()
    g.add_vertice(1)
    g.add_vertice(2)
    g.add_vertice(3)
    g.add_edge(1, 1)
    g.add_edge(1, 3)
    g.add_vertice(4)
    g.add_edge(4, 3)
    g.Print_adjList()
    g.Print_adjMat()

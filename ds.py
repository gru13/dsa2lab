class Stack:
    def __init__(self, Stack=[]) -> None:
        self.__stack: list = Stack

    def top(self):
        if not self.isEmpty():
            return self.__stack[-1]
        else:
            return

    def push(self, val) -> None:
        self.__stack.append(val)

    def pop(self):
        return self.__stack.pop()

    def display(self) -> None:
        for a in self.__stack:
            print(a, end="->")
        print()

    def isEmpty(self) -> bool:
        if (len(self.__stack) == 0):
            return True
        else:
            return False

    def inStack(self, val):
        if val in self.__stack:
            return True
        else:
            return False


class Queue:
    def __init__(self, Queue=[]) -> None:
        self.__Queue: list = Queue

    def enQueue(self, val) -> None:
        self.__Queue.append(val)

    def deQueue(self):
        if self.isEmpty():
            return
        return self.__Queue.pop(0)

    def front(self):
        return self.__Queue[0]

    def isEmpty(self) -> bool:
        if (len(self.__Queue) == 0):
            return True
        else:
            return False

    def inQueue(self, val):
        if val in self.__Queue:
            return True
        else:
            return False

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

    def numberOfVertices(self) -> int:
        return len(self.__graph)

    def vertices(self) -> list:
        return list(self.__graph.keys())

    def edgesOf(self, vertice):
        if vertice in self.__graph.keys():
            return list(self.__graph[vertice])
        else:
            return None

    def isVertice(self, vertice) -> bool:
        if vertice in self.__graph.keys():
            return True
        else:
            return False


# class DisjointSet:
#     def __init__(self, preSet: list = None) -> None:
#         self.key: list = []
#         self.val: list = []
#         self.len = 0
#         if preSet != None:
#             for i in preSet:
#                 self.add(i)
#                 self.len += 1

#     def add(self, k):
#         self.key.append(k)
#         self.val.append(-1)

#     def union(self, u, v):
#         if u not in self.key:
#             self.add(u)
#         if v not in self.key:
#             self.add(v)

#         u = self.key.index(u)
#         v = self.key.index(v)
#         if self.val[u] < self.val[v]:
#             self.val[u]
#         else:


#     def find(self, u):
#         if u not in self.key:
#             return None
#         u = self.key.index(u)
#         while self.val[u] > 0:
#             u = self.val[u]
#         return u

#     def display(self) -> None:
#         print("DisJoint SET:")
#         for i in range(self.len):
#             print(self.key[i], ":", self.val[i])
class DisjointSet:
    def __init__(self, preSet: list = None) -> None:
        self.key_disjoint = {}
        self.disjoint = []
        self.preSet = preSet
        if preSet != None:
            self.key_disjoint = {preSet[i-1]: i for i in range(1, len(preSet)+1)}
            self.disjoint = [-1]*(len(preSet)+1)

    def add(self, k):
        self.key_disjoint[k] = len(self.disjoint) + 1
        self.preSet.append(k)

    def union(self, u, v):
        if u not in self.key_disjoint.keys():
            self.add(u)
        if v not in self.key_disjoint.keys():
            self.add(v)
        u = self.key_disjoint[u]
        v = self.key_disjoint[v]
        if (self.disjoint[u] < self.disjoint[v]):
            self.disjoint[u] += self.disjoint[v]
            self.disjoint[v] = u
        else:
            self.disjoint[v] += self.disjoint[u]
            self.disjoint[u] = v

    def find(self, u):
        if u not in self.key_disjoint.keys():
            return None
        u = self.key_disjoint[u]
        while self.disjoint[u] > 0:
            u = self.disjoint[u]
        return self.preSet[u-1]

    def display(self) -> None:
        print("DisJoint SET:")
        for (k, v) in self.key_disjoint.items():
            print(k, ":", self.disjoint[v])


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
    G.add_vertice(5)

    G.add_edge(1, 2)
    G.add_edge(1, 3)
    G.add_edge(4, 2)
    G.add_edge(4, 3)
    G.add_edge(4, 5)

    G.Print_adjList()
    print(G.adjcent_list())

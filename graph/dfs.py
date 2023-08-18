from ds import Stack, Graph

def dfs(G:Graph, starting_vertex):
    visited = set()
    stk = Stack()
    stk.push(starting_vertex)
    visited.add(starting_vertex)
    while not stk.isEmpty():
        vertx = stk.top()
        h = (set(G.edgesOf(vertx)) - visited)
        if len(h) == 0:
            print(stk.pop())
        else:
            adj = list(h)[0]
            visited.add(adj)
            stk.push(adj)




# G = Graph(graph={0: [1, 2, 3], 1: [0, 2], 2: [0, 4], 3: [1], 4: [2]})
# # G = Graph()
# G.add_vertice(1)
# G.add_vertice(2)
# G.add_vertice(3)
# G.add_vertice(4)

# G.add_edge(1, 2)
# G.add_edge(1, 3)
# G.add_edge(4, 2)
# G.add_edge(4, 3)
# G.add_edge(4, 5)

G = Graph(graph={1:[2,3], 2:[1,4,5], 3:[1,4], 4:[2,3,5], 5:[2,4]})

G.Print_adjList()


DFS = dfs(G, 1)
# print(DFS)
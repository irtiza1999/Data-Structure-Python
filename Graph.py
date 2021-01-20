class Graph:
    def __init__(self, gdict=None):
        if gdict == None:
            gdict = {}
        self.gdict = gdict

    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)

    def bfs(self, vertex):
        visited = [vertex]
        queue = [vertex]
        while queue:
            dequeueVertex = queue.pop(0)
            print(dequeueVertex)
            for adjacentVertex in self.gdict[dequeueVertex]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    queue.append(adjacentVertex)  # Time = O(V+E), Space = O(V+E)

    def dfs(self, vertex):
        visited = [vertex]
        stack = [vertex]
        while stack:
            popVertex = stack.pop()
            print(popVertex)
            for adjecentVertex in self.gdict[popVertex]:
                if adjecentVertex not in visited:
                    visited.append(adjecentVertex)
                    stack.append(adjecentVertex)  # Time = O(V+E), Space= O(V+E)

customDict = {"a": ["b", "c"],
              "b": ['a', 'd', 'e'],
              'c': ['a', 'e'],
              'd': ['b', 'e', 'f'],
              'e': ['d', 'f'],
              'f': ['d', 'e']
              }
graph = Graph(customDict)
print(graph.gdict)
graph.dfs('a')

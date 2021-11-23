class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []


    def addEdge(self, cur_vertex, next_vertex, weight):
        self.graph.append([cur_vertex, next_vertex, weight])


    def printArr(self, dist):
        print("Vertex Distance from Source")
        for i in range(self.V):
            print("{0}\t\t{1}".format(i, dist[i]))

    def BellmanFord(self, src):

        dist = [float("Inf")] * self.V
        dist[src] = 0

        for i in range(self.V):

            for cur_vertex, next_vertex, weight in self.graph:
                if dist[cur_vertex] != float("Inf") and dist[cur_vertex] + weight < dist[next_vertex]:
                    dist[next_vertex] = dist[cur_vertex] + weight
                    if i == self.V :
                        print("Found negative cycle")




        self.printArr(dist)


g = Graph(5)
g.addEdge(0, 1, 9)
g.addEdge(0, 2, 3)
g.addEdge(1, 2, 6)
g.addEdge(1, 4, 2)
g.addEdge(2, 1, 2)
g.addEdge(2, 3, 1)
g.addEdge(3, 2, 2)
g.addEdge(3, 4, 2)

g.BellmanFord(0)


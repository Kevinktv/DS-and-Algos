"""
Adjacency list rep of a non weighted directed/undirected graph
"""

from __future__ import annotations
from typing import Optional, Any, List, Dict, Set
from collections import deque


class Vertex:
    item: Any
    neighbours: Set[Vertex]

    def __init__(self, item):
        self.item = item
        self.neighbours = set()


class Graph:
    vertices: Dict[Any, Vertex]
    isDirected: bool

    def __init__(self, Direction: bool = False):
        self.vertices = {}
        self.isDirected = Direction

    def addVertex(self, item):
        # Creates a new vertex containing item and adds it to vertex list if not there
        if item not in self.vertices:
            v = Vertex(item)
            self.vertices[item] = v

    def addEdge(self, item1, item2):
        # Given two items, adds an edge between them
        if item1 not in self.vertices or item2 not in self.vertices:
            return

        v1 = self.vertices[item1]
        v2 = self.vertices[item2]
        if not self.isDirected:  # Undirected
            v1.neighbours.add(v2)
            v2.neighbours.add(v1)

        else:  # Directed
            v1.neighbours.add(v2)

    def bfs(self, item):
        """Conducts breadth first search on Graph starting with item
        white means not discovered
        grey means discovered not finished
        black means finished
        """
        if item not in self.vertices:
            return

        status = {}
        parent = {}
        for v in self.vertices.keys():
            status[v] = ["white", -1]
            parent[v] = None

        q = deque()

        status[item][0] = "grey"
        status[item][1] = 0
        parent[item] = None
        q.append(item)

        while len(q) != 0:
            temp = q.popleft()
            vertex = self.vertices[temp]
            # Do stuff with item here
            # print(f"Item: {vertex.item}, dist: {status[vertex.item][1]}")
            for x in vertex.neighbours:
                if status[x.item][0] == "white":
                    q.append(x.item)
                    status[x.item][0] = "grey"
                    status[x.item][1] = status[vertex.item][1] + 1
                    parent[x.item] = vertex.item

            status[vertex.item][0] = "black"

        return status, parent

    def find_path(self, source, dest):
        """Returns one of the possible shortest path from source to destination"""
        paths = self.bfs(dest)[1]

        actualpath = []
        currentnode = source
        actualpath.append(currentnode)
        while paths[currentnode] is not None:
            currentnode = paths[currentnode]
            actualpath.append(currentnode)
        return actualpath

    def isConnected(self):
        """Returns whether the graph is connected. I do this by checking if a spanning tree
        exists"""
        onevert = list(self.vertices.keys())[0]
        paths = self.bfs(onevert)[1]
        flag = 0
        for i in paths.values():
            if i is None:
                flag += 1

        if flag > 1:
            return False

        return True

    def bfsBipartiteHelper(self, vertex, color, discovered):
        """A helper for bipartite graph"""
        q = deque()
        q.append(vertex)
        discovered[vertex] = True

        while len(q) != 0:
            temp = q.popleft()
            vert = self.vertices[temp]
            for x in vert.neighbours:
                if discovered[x.item] == False:
                    discovered[x.item] = True
                    if color[vert.item] == "blue":
                        color[x.item] = "red"
                    else:
                        color[x.item] = "blue"
                    q.append(x.item)

                if color[x.item] == color[vert.item]:
                    return False

        print("bruh")
        return True

    def bipartite(self):
        """Colors every vertex into 2 colours. If two vertices are adjacent
        they have different colour. If not possible, then returns not possible
        Colours are red and blue. Will colour for different connected components as well.
        """
        color = {}
        discovered = {}
        for v in self.vertices.keys():
            color[v] = None
            discovered[v] = False

        for v in self.vertices.values():
            if discovered[v.item] == False:
                color[v.item] = "red"
                res = self.bfsBipartiteHelper(v.item, color, discovered)
                if not res:
                    print("Not bipartite")
                    return
        return color


if __name__ == "__main__":
    g = Graph()
    g.addVertex(1)
    g.addVertex(2)
    g.addVertex(3)
    g.addVertex(4)
    g.addVertex(5)
    g.addVertex(6)
    g.addVertex(7)
    g.addVertex(8)
    g.addEdge(1, 8)
    g.addEdge(1, 7)
    g.addEdge(1, 2)
    # g.addEdge(2, 7)
    g.addEdge(2, 3)
    g.addEdge(2, 5)
    # g.addEdge(3, 5)
    g.addEdge(3, 4)
    g.addEdge(5, 4)
    g.addEdge(5, 6)

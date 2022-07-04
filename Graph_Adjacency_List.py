class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

class Graph:
    def __init__(self, noOfVertices, directed = False):
        self.size = noOfVertices
        self.vertices = [None] * noOfVertices
        self.directed = directed
    
    def addEdge(self, u, v):
        newNode = Node(v)
        newNode.next = self.vertices[u]
        self.vertices[u] = newNode
        
        if not self.directed:
            newNode2 = Node(u)
            newNode2.next = self.vertices[v]
            self.vertices[v] = newNode2
            
    def hasEdge(self, u, v):
        temp = self.vertices[u]
        while temp is not None:
            if temp.value == v:
                return True
        return False
        
    def printGraph(self):
        for i in range(self.size):
            temp = self.vertices[i]
            print("Adjacent nodes of current node: ", i, "-->", end=" ")
            while temp is not None:
                print(temp.value, end= " ")
                temp = temp.next
            print()

    def BFS(self, head=None):
        print("BFS OF GRAPH: ")
        queue = []
        visited = [False] * self.size
        for i in range(self.size):
            if visited[i]:
                continue
            queue.append(i)
            visited[i] = True
            while len(queue) > 0:
                current = queue.pop(0)
                print(current, end=" ")
                temp = self.vertices[current]
                while temp is not None:
                    if visited[temp.value]:
                        temp = temp.next
                        continue

                    queue.append(temp.value)
                    visited[temp.value] = True
                    temp = temp.next
        print()

    def DFS(self, head=0, visited=None):
        if visited is None:
            print("DFS OF GRAPH: ")
            visited = [False] * self.size

        if visited[head]:
            return

        print(head, end= " ")
        visited[head] = True
        temp = self.vertices[head]
        while temp is not None:
            nxt = temp.value
            self.DFS(nxt, visited)
            temp = temp.next  

    def topologicalSort(self):
        print()
        stack = []
        visited = [False] * self.size
        for i in range(self.size):
            if visited[i]:
                continue
            self.topologicalSortUtil(i, visited, stack)
        
        print("Topological Order: ", list(reversed(stack)))

    def topologicalSortUtil(self, u, visited, stack):
        if visited[u]:
            return
            
        visited[u] = True
        curr = self.vertices[u]
        while curr is not None:
            self.topologicalSortUtil(curr.value, visited, stack)
            curr = curr.next
        stack.append(u)

    def hasCycleUsingBFS(self):
        visited = [False] * self.size
        queue = []
        parent = [-1] * self.size
        for i in range(self.size):
            if visited[i]:
                continue
            visited[i] = True
            queue.append(i)
            while len(queue) > 0:
                curr = queue.pop(0)
                adj = self.vertices[curr]
                while adj is not None:
                    if adj.value == curr:
                        adj = adj.next
                        continue

                    if visited[adj.value]:
                        print("Graph is cyclic")
                        return True

                    queue.append(adj.value)
                    visited[adj.value] = True
                    adj = adj.next
        print("Graph is Acyclic")
        return False

    def hasCycleUtil(self, u, visited, stack):
        visited[u] = True
        stack[u] = True

        curr = self.vertices[u]
        while curr is not None:
            if not visited[curr.value]:
                return self.hasCycleUtil(curr.value, visited, stack)
            elif stack[curr.value]:
                return True
            curr = curr.next
        stack[u] = False
        return False

    def isBiparite(self):
        color = [-1] * self.size
        queue = []
        for i in range(self.size):
            if color[i] != -1:
                continue
            queue.append(i)
            color[i] = 1
            while len(queue) > 0:
                curr = queue.pop(0)
                print("Current vertice: ", curr)
                temp = self.vertices[curr]
                while temp is not None:
                    if color[temp.value] == -1:
                        color[temp.value] = 1 - color[curr]
                        queue.append(temp.value)

                    elif color[temp.value] == color[curr]:
                        print("Graph is not Biparite")
                        return False
                    temp = temp.next
        print("Graph is Biparite")
        return True

def main():
    n, m = map(int, input().split())
    graph = Graph(n)
    for i in range(m):
        u, v = map(int, input().split())
        graph.addEdge(u, v)
    
    graph.printGraph()
    graph.BFS()
    graph.DFS()
    graph.topologicalSort()
    graph.isBiparite()
    graph.hasCycleUsingBFS()

if __name__ == "__main__":
    main()
    
# INPUT:

"""
5 5
0 1
1 2
2 3
3 0
2 4

"""
"""
8 7
1 0
0 4
4 2
0 5
5 6
5 3
5 7
"""
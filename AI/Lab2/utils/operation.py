import sys


class Operation:
    def __init__(self):
        pass

    def allVisited(self, graph):
        for v in graph:
            if v.visited == False:
                return False
        return True

    def setAllUnvisited(self, graph):
        for v in graph:
            v.set_unvisited()

    def findPath(self, graph, start, finish):
        path = []
        currentVertex = start
        sum = 0
        while (self.allVisited(graph) == False):
            currentVertex.set_visited()
            path.append(currentVertex.get_id())
            min = sys.maxsize
            for neighbor in currentVertex.get_connections():
                if (currentVertex.get_weight(neighbor) < min) & (neighbor.visited == False):
                    min = currentVertex.get_weight(neighbor)
                    next = neighbor
            sum += currentVertex.get_weight(next)
            currentVertex = next
            if currentVertex == finish:
                break

        if start != finish:
            path.append(finish.get_id())

        if (self.allVisited(graph)) & (start == finish):
            sum += currentVertex.get_weight(start)

        self.setAllUnvisited(graph)
        return ([path, sum])

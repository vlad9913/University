import sys

from domain.graph import Graph, Vertex


class Repository:
    def __init__(self):
        self._graph = Graph()
        self._length = 0
        self._start = -1
        self._finish = -1
        self.readFromFile()

    def readFromFile(self):
        f = open("date.txt", "r")
        lines = f.readlines()
        self._length = int(lines[0])
        for i in range(1, self._length + 1):
            line = lines[i].split(',')
            for j in range(0, len(line)):
                self._graph.add_edge(i, j + 1, int(line[j]))
        self._start = int(lines[self._length + 1])
        self._finish = int(lines[self._length + 2])
        f.close()

    def writeToFile(self, rezult1, rezult2):
        path1 = rezult1[0]
        cost1 = rezult1[1]
        path2 = rezult2[0]
        cost2 = rezult2[1]

        lines = [str(self._length) + '\n',
                 str(path1)[1:-1] + '\n',
                 str(cost1) + '\n',
                 str(len(path2)) + '\n',
                 str(path2)[1:-1] + '\n',
                 str(cost2) + '\n'
                ]
        file= open('rezultate.txt','w')
        file.writelines(lines)
        file.close()
        return

    def getGraph(self):
        return self._graph

    def getLength(self):
        return self._length

    def getStart(self):
        return self._start

    def getFinish(self):
        return self._finish

from repo.repository import *
from domain.graph import *
from utils.operation import Operation


class Service:
    def __init__(self, repo, op):
        self._repo = repo
        self._op = op

    def problema1(self):
        graph = self._repo.getGraph()
        return self._op.findPath(graph,graph.get_vertex(1),graph.get_vertex(1))


    def problema2(self):
        graph = self._repo.getGraph()
        start = self._repo.getStart()
        finish = self._repo.getFinish()
        return self._op.findPath(graph,graph.get_vertex(start),graph.get_vertex(finish))

    def write_to_file(self):
        graph=self._repo.getGraph()
        rez1=self.problema1()
        rez2=self.problema2()

        self._repo.writeToFile(rez1,rez2)

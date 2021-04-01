from networkx import *
from numpy import *

filePath = "C:/Users/Vlad/PycharmProjects/lab3/Utils/lesmis.gml"


def readGML(filePath):
    net = {}
    G = read_gml(filePath)
    # G = networkx.karate_club_graph()

    mat = networkx.to_numpy_matrix(G)

    n = int(sqrt(size(mat)))

    net["noNodes"] = n
    net["mat"] = mat
    net['noEdges'] = G.number_of_edges()

    degrees = []
    for i in range(n):
        d = 0
        for j in range(n):
            if (mat.item(i, j) == 1):
                d += 1
        degrees.append(d)

    net["degrees"] = degrees
    return net


network = readGML(filePath)

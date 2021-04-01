from networkx import *
from numpy import *


def readMatrix(fileName):
    f = open(fileName, "r")
    net = {}
    n = int(f.readline())
    net['noNodes'] = n
    mat = []
    for i in range(n):
        mat.append([])
        line = f.readline()
        elems = line.split(",")
        for j in range(n):
            mat[-1].append(int(elems[j]))
    net["mat"] = mat
    f.close()
    return net

def readPlane(fileName):
    file = open(fileName,"r")
    net={}
    lista = []
    mat=[]
    lines = file.readlines()
    n=0

    for line in lines:
        n+=1
        linie = (line.split(" "))
        linie[2]=linie[2][:-1]
        lista.append(linie)

    for i in range(0,n):
        mat.append([])
        for j in range(0,n):
            mat[-1].append(math.sqrt( (int(lista[i][1])-int(lista[j][1]))*(int(lista[i][1])-int(lista[j][1]))+
                                      (int(lista[i][2])-int(lista[j][2]))*(int(lista[i][2])-int(lista[j][2]))))

    net['noNodes']=n
    net['mat']=mat
    file.close()
    return net























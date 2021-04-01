def modularity(c, param):
    noNodes = param['noNodes']
    mat = param['mat']
    repr = c.repres
    sum = 0
    for i in range(0, noNodes-1):
        sum+=mat[repr[i]][repr[i+1]]
    sum+=mat[repr[-1]][repr[0]]

    return 1/sum

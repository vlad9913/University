from Persistence import *
from toolOperations import *
def makeTranspose(m):
    rez = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
    return rez

def multiplyMatrici(m1, m2):
    result = [[0 for x in range(len(m2[0]))] for y in range(len(m1))]

    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                result[i][j] += m1[i][k] * m2[k][j]

    return result

def inversaMatrice(m):
    # stim ca trebuie inversa la o matrice 3x3 deci nu e chiar asa rau
    a =   m[1][1] * m[2][2] - m[1][2] * m[2][1]
    b = -(m[1][0] * m[2][2] - m[1][2] * m[2][0])
    c =   m[1][0] * m[2][1] - m[1][1] * m[2][0]
    d = -(m[0][1] * m[2][2] - m[0][2] * m[2][1])
    e =   m[0][0] * m[2][2] - m[0][2] * m[2][0]
    f = -(m[0][0] * m[2][1] - m[0][1] * m[2][0])
    g =   m[0][1] * m[1][2] - m[0][2] * m[1][1]
    h = -(m[0][0] * m[1][2] - m[0][2] * m[1][0])
    i =   m[0][0] * m[1][1] - m[0][1] * m[1][0]

    det = m[0][0] * a + m[0][1] * b + m[0][2] * c

    if det==0:
        print("Determinant zero")

    det = 1/det
    return [[det*a,det*d,det*g],[det*b,det*e,det*h],[det*c,det*f,det*i]]




def formulaBeta():
    transpusa = makeTranspose(trainX)
    primaParanteza = multiplyMatrici(transpusa, trainX)
    inversata = inversaMatrice(primaParanteza)
    aproapeGata = multiplyMatrici(inversata,transpusa)
    betaFinal = multiplyMatrici(aproapeGata,trainY)
    return betaFinal



betauri = formulaBeta()

def testTheFunction():
    loss = 0
    for i in range(len(testX)):
        yComputed = betauri[0][0] + testX[i][1]*betauri[1][0] + testX[i][2]*betauri[2][0]
        print("For test number "+str(i)+" -  yComputed: "+str(yComputed)+";  yTrue:"+str(testY[i][0]))
        loss += abs(yComputed-testY[i][0])

    loss /= len(testY)
    print("MAE for this set of data is: " + str(loss))

testTheFunction()
print("MAE with tools is: "+str(toolMAE))
print(reg.intercept_ [0], reg.coef_[0][1],reg.coef_[0][2])
print(formulaBeta())
print("f(x)="+str(betauri[0][0])+" +x1*"+str(betauri[1][0])+"+ x2*"+str(betauri[2][0]))

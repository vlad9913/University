from sklearn import metrics
from sklearn.linear_model import SGDRegressor

from Persistence import *


def statisticalNormalisation(data, col):
    suma = 0
    for i in range(len(data)):
        suma += data[i][col]
    meanValue = suma / len(data)
    stdDevValue = (1 / len(data) * sum([(feat[col] - meanValue) ** 2 for feat in data])) ** 0.5
    normalisedData = [(feat[col] - meanValue) / stdDevValue for feat in data]
    return normalisedData, stdDevValue, meanValue


def statisticalNormalisationTest(data, col, stdDevValue, meanValue):
    normalisedData = [(feat[col] - meanValue) / stdDevValue for feat in data]
    return normalisedData


def gradientDescentUni(epoci, rate, trainX, trainY):
    startBetas = [0, 0]
    epochBetas = []
    for k in range(epoci):
        epochBetas = startBetas
        for i in range(len(trainX)):
            x = trainX[i][1]
            y = trainY[i][0]

            guess = startBetas[0] + x * startBetas[1]
            error = guess - y

            epochBetas[0] = epochBetas[0] - rate * error
            epochBetas[1] = epochBetas[1] - rate * error * x

        startBetas = epochBetas

    return epochBetas


def gradientDescentMulti(epoci, rate, nrX, trainX, trainY):
    startBetas = []

    for i in range(nrX + 1):
        startBetas.append(0)

    epochBetas = []
    for k in range(epoci):
        epochBetas = startBetas
        for i in range(len(trainX)):
            x = []
            for j in range(1,nrX+1):
                x.append(trainX[i][j])

            y = trainY[i][0]
            guess = startBetas[0]
            for j in range(nrX):
                guess += x[j] * startBetas[j + 1]
            error = guess - y

            epochBetas[0] = epochBetas[0] - rate * error
            for j in range(nrX):
                epochBetas[j + 1] = epochBetas[j + 1] - rate * error * x[j]

        startBetas = epochBetas

    return epochBetas

def toolGD(epoci,trainX,trainY,testX,testY):
    regressor = SGDRegressor()
    for i in range(epoci):
        regressor.partial_fit(trainX,trainY)
    b0,b1=regressor.intercept_,regressor.coef_[0]
    yComputed = regressor.predict(testX)

    error = metrics.mean_absolute_error(testY,yComputed)
    return error




# functie unde testez f(x)-ul calculat, practic main-ul meu
def testTheFunction(epoci, rate, nrX, trainX, trainY, testX, testY):
    loss = 0
    normX = []
    stdDevX = []
    meanX = []
    for i in range(nrX):
        norm, stdDev, mean = statisticalNormalisation(trainX, i + 1)
        normX.append(norm)
        stdDevX.append(stdDev)
        meanX.append(mean)

    normalisedTrainX = makeMatrix(normX[0], normX[1])
    #print(normalisedTrainX)

    normY, stdDevY, meanY = statisticalNormalisation(trainY, 0)

    normalisedTrainY = []
    for i in range(len(normY)):
        normalisedTrainY.append([normY[i]])

    normTsX=[]
    for i in range(nrX):
        norm = statisticalNormalisationTest(testX,i+1,stdDevX[i],meanX[i])
        normTsX.append(norm)

    normalisedTestX = makeMatrix(normTsX[0],normTsX[1])



    normTsY = statisticalNormalisationTest(testY,0,stdDevY,meanY)
    normalisedTestY=[]
    for i in range(len(normTsY)):
        normalisedTestY.append([normTsY[i]])




    # betauri = gradientDescentUni(epoci, rate, trainX, trainY)
    betauri = gradientDescentMulti(epoci, rate, nrX, normalisedTrainX, normalisedTrainY)

    for i in range(len(testX)):
        yComputed = betauri[0] + normalisedTestX[i][1] * betauri[1] + normalisedTestX[i][2] * betauri[2]

        print("For test number " + str(i) + " -  yComputed: " + str(yComputed) + ";  yTrue:" + str(normalisedTestY[i][0]))
        loss += abs(yComputed - normalisedTestY[i][0])

    loss /= len(normalisedTestY)
    print("MAE for this set of data is: " + str(loss))

    print("MAE with tool : "+ str(toolGD(epoci,normalisedTrainX,normY,normalisedTestX,normalisedTestY)))


testTheFunction(3000, 0.001, 2, trainX, trainY, testX, testY)
#print(statisticalNormalisation(trainX, 1))
#print(trainY)

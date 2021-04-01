import csv
import random



def readData(filename):
    inputData=[]
    outputData=[]
    with open(filename) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        for row in csvreader:
            if row:
                inputData.append([float(i) for i in row[:-1]])
                outputData.append( row[-1])
    return inputData,outputData



def splitMatrix(matX,matY):
    trainX = []
    testX = []

    trainY = []
    testY = []

    for i in range(len(matX)):
        a = random.random()
        if a >= 0.8:
            testX.append(matX[i])
            testY.append(matY[i])
        else:
            trainX.append(matX[i])
            trainY.append(matY[i])
    return trainX, trainY, testX, testY



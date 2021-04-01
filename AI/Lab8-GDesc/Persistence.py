import csv
import numpy as np
import random

filePath = "happinessIndex2017.csv"


def loadData(fileName, inputVariabName1, inputVariabName2, outputVariabName):
    data = []
    dataNames = []
    with open(fileName) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                dataNames = row
            else:
                data.append(row)
            line_count += 1
    selectedVariable = dataNames.index(inputVariabName1)
    inputs1 = [float(data[i][selectedVariable]) for i in range(len(data))]
    selectedVariable2 = dataNames.index(inputVariabName2)
    inputs2 = [float(data[i][selectedVariable2]) for i in range(len(data))]
    selectedOutput = dataNames.index(outputVariabName)
    outputs = [float(data[i][selectedOutput]) for i in range(len(data))]

    return inputs1, inputs2, outputs


inputs1, inputs2, outputs = loadData(filePath, 'Economy', 'Freedom', 'Happiness Score')


# print('Economy: ',inputs1[:5])
# print('Freedom:',inputs2[:5])
# print('out-Happiness: ',outputs[:5])


def makeMatrix(inputs1, inputs2):
    matrix = []
    for i in range(len(inputs1)):
        matrix.append([1, inputs1[i], inputs2[i]])
    return matrix


def splitMatrixinTwo(matX, matY):
    trainX = []
    testX = []

    trainY = []
    testY = []

    for i in range(len(matX)):
        a = random.random()
        if a >= 0.8:
            testX.append(matX[i])
            testY.append([matY[i]])
        else:
            trainX.append(matX[i])
            trainY.append([matY[i]])
    return trainX, trainY, testX, testY


mat = makeMatrix(inputs1, inputs2)
trainX, trainY, testX, testY = splitMatrixinTwo(mat, outputs)
# print(trainY)


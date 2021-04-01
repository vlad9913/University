import array
import math

from sklearn import linear_model

from Reading import *
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


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


def multiClassStatistics(realLabels, computedLabels):
    labels = []
    for label in realLabels:
        if label not in labels:
            labels.append(label)
    # fac o lista cu labelurile

    precizii = []
    rapele = []

    # abordez strategia one vs all parcurg fiecare label pentru a calcula precizia si rapelul fiecaruia
    # adica, pentru fiecare label, cel actual va fi Positive, iar restul Negative

    for label in labels:
        tp = 0
        fp = 0
        fn = 0
        for i in range(len(computedLabels)):
            if ((computedLabels[i] == label) and (realLabels[i] == label)):
                tp += 1
            if ((computedLabels[i] == label) and (realLabels[i] != label)):
                fp += 1
            if ((computedLabels[i] != label) and (realLabels[i] == label)):
                fn += 1

        precizieAcum = tp / (tp + fp)
        rapelAcum = tp / (tp + fn)
        precizii.append(precizieAcum)
        rapele.append(rapelAcum)

    acuratete = 0

    for i in range(len(realLabels)):
        if realLabels[i] == computedLabels[i]:
            acuratete += 1
    acuratete /= len(realLabels)

    return acuratete, precizii, rapele


def gradientDescentMulti(epoci, rate, nrX, trainX, trainY, label):
    startBetas = []

    for i in range(nrX + 1):
        startBetas.append(0)

    epochBetas = []
    for k in range(epoci):
        epochBetas = startBetas
        for i in range(len(trainX)):

            x = []
            for j in range(0, nrX):
                x.append(trainX[i][j])

            if trainY[i] == label:
                y = 1
            else:
                y = 0

            guess = startBetas[0]
            for j in range(nrX):
                guess += x[j] * startBetas[j + 1]

            guess = sigmoid(guess)
            error = guess - y

            epochBetas[0] = epochBetas[0] - rate * error
            for j in range(nrX):
                epochBetas[j + 1] = epochBetas[j + 1] - rate * error * x[j]

        startBetas = epochBetas

    return epochBetas


def trainTheFunction(epoci, rate, nrX, trainX, trainY):
    normX = []
    stdDevX = []
    meanX = []
    for i in range(nrX):
        norm, stdDev, mean = statisticalNormalisation(trainX, i)
        normX.append(norm)
        stdDevX.append(stdDev)
        meanX.append(mean)

    normalisedTrainX = [[normX[j][i] for j in range(len(normX))] for i in range(len(normX[0]))]

    bSetosa = gradientDescentMulti(epoci, rate, nrX, normalisedTrainX, trainY, "Iris-setosa")
    bVersicolor = gradientDescentMulti(epoci, rate, nrX, normalisedTrainX, trainY, "Iris-versicolor")
    bVirginica = gradientDescentMulti(epoci, rate, nrX, normalisedTrainX, trainY, "Iris-virginica")

    return bSetosa, bVersicolor, bVirginica, stdDevX, meanX, normalisedTrainX


def testTheFunction(bSetosa, bVersicolor, bVirginica, stdDevX, meanX, testX, testY):
    normTsX = []
    for i in range(len(testX[0])):
        norm = statisticalNormalisationTest(testX, i, stdDevX[i], meanX[i])
        normTsX.append(norm)

    normalisedTestX = [[normTsX[j][i] for j in range(len(normTsX))] for i in range(len(normTsX[0]))]

    computedLabels = []
    for i in range(len(normalisedTestX)):
        yComputedSetosa = bSetosa[0] + normalisedTestX[i][0] * bSetosa[1] + normalisedTestX[i][1] * bSetosa[2] \
                          + normalisedTestX[i][2] * bSetosa[3] + normalisedTestX[i][3] * bSetosa[4]

        yComputedSetosa = sigmoid(yComputedSetosa)

        yComputedVersicolor = bVersicolor[0] + normalisedTestX[i][0] * bVersicolor[1] + normalisedTestX[i][1] * \
                              bVersicolor[2] \
                              + normalisedTestX[i][2] * bVersicolor[3] + normalisedTestX[i][3] * bVersicolor[4]

        yComputedVersicolor = sigmoid(yComputedVersicolor)

        yComputedVirginica = bVirginica[0] + normalisedTestX[i][0] * bVirginica[1] + normalisedTestX[i][1] * \
                             bVirginica[2] + normalisedTestX[i][2] * bVirginica[3] + normalisedTestX[i][3] * bVirginica[
                                 4]

        yComputedVirginica = sigmoid(yComputedVirginica)


        #threshold ar veni aici in cazul in care yComputed-urile sunt prea mici iar max-ul nu are sens, nu depaseste
        #thresholdul, iar atunci algoritmul spune "niciun label"

        labelComputed = ""
        if max(yComputedSetosa, yComputedVersicolor, yComputedVirginica) == yComputedSetosa:
            labelComputed = "Iris-setosa"
        if max(yComputedSetosa, yComputedVersicolor, yComputedVirginica) == yComputedVersicolor:
            labelComputed = "Iris-versicolor"
        if max(yComputedSetosa, yComputedVersicolor, yComputedVirginica) == yComputedVirginica:
            labelComputed = "Iris-virginica"

        print("For test number " + str(i) + " - Computed label is: " + labelComputed + "/ Real one is: " + testY[
            i] + " // Probabilites are (S,Ve,Vi): " +
              str(yComputedSetosa) + " " + str(yComputedVersicolor) + " " + str(yComputedVirginica))

        computedLabels.append(labelComputed)

    return computedLabels, normalisedTestX


def withTool(trainX, trainY, testX, testY):
  # trY = [[trainY[j]] for j in range(len(trainY))]
  # tsY = [[testY[j]] for j in range(len(testY))]

    clr = linear_model.LogisticRegression()
    clr.fit(trainX, trainY)
    computedY = clr.predict(testX)


    return computedY




def main():
    filename = "iris.data"
    inputData, outputData = readData(filename)
    trainX, trainY, testX, testY = splitMatrix(inputData, outputData)

    bSetosa, bVersicolor, bVirginica, stdDevX, meanX, normalisedTrainX = trainTheFunction(2000, 0.001, 4, trainX,
                                                                                          trainY)
    computedLabels, normalisedTestX = testTheFunction(bSetosa, bVersicolor, bVirginica, stdDevX, meanX, testX, testY)

    acuratete, precizii, rapele = multiClassStatistics(testY, computedLabels)
    print("\nAcuratete: " + str(acuratete))
    print("Precizii[Setosa,Versicolor,Virginica]: " + str(precizii[0]) + ", " + str(precizii[1]) + ", " + str(
        precizii[2]))
    print("Rapele[Setosa,Versicolor,Virginica]: " + str(rapele[0]) + ", " + str(rapele[1]) + ", " + str(rapele[2]))


    toolY = withTool(normalisedTrainX, trainY, normalisedTestX, testY)
    acuratete, precizii, rapele = multiClassStatistics(testY, toolY)
    print("\nWITH TOOL:")
    print(toolY)
    print("Acuratete: " + str(acuratete))
    print("Precizii[Setosa,Versicolor,Virginica]: " + str(precizii[0]) + ", " + str(precizii[1]) + ", " + str(
        precizii[2]))
    print("Rapele[Setosa,Versicolor,Virginica]: " + str(rapele[0]) + ", " + str(rapele[1]) + ", " + str(rapele[2]))


main()

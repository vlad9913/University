import math
'''
Multi-target regression: (y1,y2, ..., yk) = [f1(x1, x2, ..,xD), f2(x1, x2, ..,xD), ..., fk(x1, x2, ..,xD)] - 
more real values are predicted based on D features (x1, x2, ..., xD) of an example

Problem specification:

input: realOutput, computedOutput - k-dimensional arrays of the same length containing real values
 (two matrix of k*noSamples elements, k = number of output targets, noSamples = no of samples/examples)

output: prediction error - real value
'''

#MAE
def eroareMultiTarget(realOutput, computedOutput):
    medieFinala = 0
    # len(realOutput) - k-ul din exemplu
    for i in range(len(realOutput)):
        mediePeUnK = 0
        # len(realOutput(i)) - noSamples din exemplu
        for j in range(len(realOutput[i])):
            mediePeUnK += abs(computedOutput[i][j] - realOutput[i][j])
        mediePeUnK /= len(realOutput[i])
        medieFinala += mediePeUnK

    medieFinala /= len(realOutput)
    return medieFinala

#RMSE
def eroareMultiTarget2(realOutput, computedOutput):
    medieFinala = 0
    # len(realOutput) - k-ul din exemplu
    for i in range(len(realOutput)):
        mediePeUnK = 0
        # len(realOutput(i)) - noSamples din exemplu
        for j in range(len(realOutput[i])):
            mediePeUnK += (computedOutput[i][j] - realOutput[i][j])**2
        mediePeUnK /= len(realOutput[i])
        mediePeUnK = math.sqrt(mediePeUnK)
        medieFinala += mediePeUnK

    medieFinala /= len(realOutput)
    return medieFinala



def testEroareMultiTarget():
    assert (0.44 < eroareMultiTarget([[2, 2, 3], [2, 5, 8], [2, 4, 7]],
                                     [[2, 2, 4], [2, 5, 8], [3, 5, 6]]) < 0.45)  # 0.(4)
    assert (eroareMultiTarget([[2, 4], [2, 4]], [[3, 4], [4, 5]]) == 1.0)

    assert(0.525<eroareMultiTarget2([[2, 2, 3], [2, 5, 8], [2, 4, 7]],
                                     [[2, 2, 4], [2, 5, 8], [3, 5, 6]])<0.53)
    print("testEroareMultiTarget PASSED")

'''
Remember:

Binary classification: y = f(x1, x2, ..,xD) - a single binary label (y) is predicted based on D features (x1, x2, ..., xD) of an example

Multi-class classification: y = f(x1, x2, ..,xD) - a single label (from a particular set of possible labels whose size > 2) is predicted based on D features (x1, x2, ..., xD) of an example

Problem specification:

input: realLabels, computedLabels - one-dimensional arrays of the same length containing labels (two arrays of $noSamples$ labels from 
${label_1, label_2, \ldots, label_C}$, $noSamples$ = no of samples/exampeles)

output: prediction quality expressed by accuracy, precison and recall.
'''


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


def testMultiClassStatistics():
    assert(multiClassStatistics(["1", "2", "3", "4", "5"], ["1", "2", "5", "4", "3"])==(0.6, [1.0, 1.0, 0.0, 1.0, 0.0], [1.0, 1.0, 0.0, 1.0, 0.0]))
    print("testMultClassStatistics PASSED")


# MAE - Mean Absolute Error, este ce am calculat in prima functie, are aceeasi formula doar ca asta nu e multi
def lossRegression(realOutput, computedOutput):
    MAE = 0
    for i in range(len(realOutput)):
        # len(realOutput(i)) - noSamples din exemplu
        MAE += abs(computedOutput[i] - realOutput[i])
    MAE /= len(realOutput)
    return MAE


def testLossRegression():
    assert(lossRegression([2, 2, 3], [3, 3, 4])==1.0)
    assert(lossRegression([1,2,3,4,5,6],[1,2,4,4.5,5.5,7])==0.5)
    print("testLossRegression PASSED")

def executeTests():
    testEroareMultiTarget()
    testMultiClassStatistics()
    testLossRegression()

executeTests()

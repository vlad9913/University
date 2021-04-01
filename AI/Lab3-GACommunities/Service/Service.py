from Domain.Chromosome import *
from Utils.Reading import *
from random import *
from collections import Counter


def randomChromosome():
    repr = []
    noNodes = network["noNodes"]

    i = 0
    while i <= noNodes - 1:
        x = randint(1, noNodes)
        repr.append(x)
        i += 1

    return repr


def crossover(c1, c2):
    noNodes = network["noNodes"]
    slice = randint(0, noNodes - 1)
    c3 = []
    i = 0
    while i <= noNodes - 1:
        if i <= slice:
            c3.append(c1[i])
        else:
            c3.append(c2[i])
        i += 1
    return c3


def mutation(c):
    cCopy = c
    noNodes = network["noNodes"]
    x = randint(1, noNodes)
    i = randint(0, noNodes - 1)
    cCopy[i] = x
    return cCopy


def evolution(nrGens, popLength):
    population = []
    i = 0

    maxFitness = 0
    while i < popLength - 1:
        c = Chromosome(randomChromosome())
        if c.fitness > 0:
            population.append(c)
            if c.fitness>maxFitness:
                maxFitness = c.fitness
                bestChromo = c
            i += 1


    for i in range(nrGens):
        newPopulation = []
        newPopulation.append(bestChromo)
        for j in range(popLength - 1):
            mother = population[randint(0, len(population) - 1)]
            father = population[randint(0, len(population) - 1)]

            c1_before = crossover(mother.repres, father.repres)
            c1_after = mutation(c1_before)

            c2_before = crossover(mother.repres, father.repres)
            c2_after = mutation(c2_before)

            child1 = Chromosome(c1_after)
            child2 = Chromosome(c2_after)

            if child1.fitness > child2.fitness:
                child = child1
            else:
                child = child2

            newPopulation.append(child)
            if maxFitness < child.fitness:
                maxFitness = child.fitness
                bestChromo = child

        print(bestChromo)
        nrCom = len(set(bestChromo.repres))
        print("\n No. of communities: ",nrCom )

        population = newPopulation

    return bestChromo


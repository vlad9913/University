from Domain.Chromosome import *
from Utils.Reading import *
from random import *
from collections import Counter


network = readMatrix("C:/Users/Vlad/PycharmProjects/lab3/Utils/mediumF.txt")


def evolution(nrGens, popLength):
    population = []
    maxFitness = 0

    i = 0
    while i < popLength - 1:
        c = Chromosome(network)
        c.fitness=modularity(c,network)
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

            c1 = mother.crossover(father)
            c1.mutation()
            c1.fitness=modularity(c1,network)

            c2 = mother.crossover(father)
            c2.mutation()
            c2.fitness=modularity(c2,network)


            if c1.fitness > c2.fitness:
                child = c1
            else:
                child = c2

            newPopulation.append(child)
            if maxFitness < child.fitness:
                maxFitness = child.fitness
                bestChromo = child

        print(bestChromo)
        population = newPopulation

    f = open("out.txt","w")
    f.write(str(bestChromo.repres))
    f.write("\n")
    f.write(str(1/bestChromo.fitness))


    return bestChromo


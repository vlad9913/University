from Utils.Fitness import *
from Utils.Reading import *


class Chromosome:
    def __init__(self, repres):
        self.__repres = repres
        self.__fitness = modularity(self.__repres, network)

    @property
    def repres(self):
        return self.__repres

    @property
    def fitness(self):
        return self.__fitness

    @repres.setter
    def repres(self, l):
        self.__repres = l

    @fitness.setter
    def fitness(self, fit=0.0):
        self.__fitness = fit

    def __str__(self):
        return '\nChromosome: ' + str(self.__repres) + ' has fit: ' + str(self.__fitness)

    def __eq__(self, c):
        return self.__repres == c.__repres and self.__fitness == c.__fitness
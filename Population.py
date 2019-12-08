#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Individual import Individual
from FileInterface import FileInterface

import random

random.seed()

class Population:

    def __init__(self, n, m_rate):
        self.individuals = []
        self.volume = n
        self.generation = 0
        self.mutation_rate = m_rate
        for _ in range(n):
            self.individuals.append(Individual())

    def NewGeneration(self):
        self.generation += 1
        self.Roulette()
        self.Reproduction()
        self.Mutation()
        self.MakeInputs()
        self.MakeReport()

    def SetDirectoryInput(self, dir, input, core_amount):
        self.directory = dir
        self.FI = FileInterface(dir + "/scripts/bash/run_jobs.sh", dir + "/inp/" + input, core_amount)

    
    def MakeInputs(self):
        result = self.FI.MakeDir(self.directory + "/results","gen"+str(self.generation))
        for individual in self.individuals:
            #set simulation parameters 
            variables = [individual.GetVariables()[0], individual.GetVariables()[0] + individual.GetVariables()[1]]
            individual.file_association = self.FI.MakeInput(result,str(individual.chromosome)+"i",variables)
            if not individual.file_association: return False
        self.FI.RunInputCluster(result) #cluster run
        for individual in self.individuals:
            individual.keff = self.FI.ReadResult("ABS_KEFF",[47,58],individual.file_association)
            #if individual.file_associoation : 
            #    individual.keff = self.FI.RunInput(individual.file_associoation)  #check file exist
            #else: return False
        return True

    def Roulette(self):
        nIndividuals = []
        for _ in range(self.volume):
            barrier = random.uniform(0, self.GetFitSum())
            sum = 0.0
            for individual in self.individuals:
                sum += individual.GetFitness()
                if (sum > barrier):
                    nIndividuals.append(individual)
                    break
        self.individuals = nIndividuals

    def Reproduction (self):
        nIndividuals = []
        while len(self.individuals) > 1:
            parent1 = random.choice(self.individuals)
            self.individuals.remove(parent1)
            parent2 = random.choice(self.individuals)
            self.individuals.remove(parent2)
            point = random.randint(0, Individual().GetChromosomeLen())
            child1 =  (parent1.chromosome >> point) << point | (parent2.chromosome & ((2**point) -1))
            child2 =  (parent2.chromosome >> point) << point | (parent1.chromosome & ((2**point) -1))
            nIndividuals.append(Individual(child1))
            nIndividuals.append(Individual(child2))
        nIndividuals.extend(self.individuals)
        self.individuals = nIndividuals

    def Mutation(self):
        nIndividuals = []
        for individual in self.individuals:
            if random.uniform(0,1) < self.mutation_rate:
                rand = 2**random.randint(0,individual.GetChromosomeLen()-1)
                nIndividuals.append( Individual( individual.chromosome ^ rand ) ) #XOR operation
            else:
                nIndividuals.append(individual)
        self.individuals = nIndividuals
        


    def GetMaxFit(self):
        max = 0.0
        for individual in self.individuals:
            if max < individual.GetFitness() : max = individual.GetFitness()
        return max

    def GetFitSum(self):
        sum = 0.0
        for individual in self.individuals:
            sum += individual.GetFitness()
        return sum

    def MakeReport(self):
        print("===========Raport============")
        print("Pokolenie : {}".format(self.generation))
        best = Individual()
        for individual in self.individuals:
            print(individual)
            if individual.GetFitness() > best.GetFitness(): best = individual
        print ("Max Fit : {}".format(self.GetMaxFit()))
        print (best)
        print ("Params : {}".format(best.GetVariables()))
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Individual import Individual
from FileInterface import FileInterface

import random

random.seed()

class Population:

    def __init__(self, n):
        self.individuals = []
        self.volume = n
        self.generation = 0
        for i in range(n):
            self.individuals.append(Individual())

    def NewGeneration(self):
        self.generation += 1
        self.Roulette()
        self.Reproduction()
        self.Mutation()
        self.MakeInputs()
        self.MakeReport()

    def SetDirectoryInput(self, dir, input):
        self.directory = dir
        self.FI = FileInterface(dir + "/sss2", dir + "/inp/" + input)

    
    def MakeInputs(self):
        for i, individual in enumerate(self.individuals):
            #ustawienie parametrów dla symulacji
            variables = [individual.GetVariables()[0], individual.GetVariables()[0] + individual.GetVariables()[1]]
            individual.file_associoation = self.FI.MakeInput(self.directory + "/results",str(individual.chromosome),variables)
            individual.keff = self.FI.RunInput(individual.file_associoation)

    def Roulette(self):
        nIndividuals = []
        for i in range(self.volume):
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
            #print("{:010b}".format(parent1.chromosome))
            self.individuals.remove(parent1)
            parent2 = random.choice(self.individuals)
            #print("{:010b}".format(parent2.chromosome))
            self.individuals.remove(parent2)
            point = random.randint(0, Individual().GetChromosomeLen())
            #print(point)
            child1 =  (parent1.chromosome >> point) << point | (parent2.chromosome & ((2**point) -1))
            #print("{:010b}".format(child1))
            child2 =  (parent2.chromosome >> point) << point | (parent1.chromosome & ((2**point) -1))
            #print("{:010b}".format(child2))
            nIndividuals.append(Individual(child1))
            nIndividuals.append(Individual(child2))
        nIndividuals.extend(self.individuals)
        self.individuals = nIndividuals

    def Mutation(self):
        for individual in self.individuals:
            bin_str = bin(individual.chromosome)[2:].zfill(individual.GetChromosomeLen())
            out_str = ""
            for bit in bin_str:
                if random.uniform(0,1) < 0.01:
                    if bit == '1': out_str += '0'
                    else : out_str += '1'
                else : out_str += bit
            individual = Individual( int ( out_str , base = 2 ))


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


        

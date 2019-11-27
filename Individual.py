#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from math import exp, sqrt

random.seed()


class Individual:
    __min_vals = [1, 0]
    __max_vals = [10,40]
    __chromo_len = [16, 16]
    
    def __init__(self, Chromosome = -1):
        if Chromosome == -1 : self.chromosome = random.randint(0,(2**self.GetChromosomeLen())-1)
        else : self.chromosome = Chromosome
        self.keff = 0.0
        self.file_association = ""

    def __str__(self):
        #form = " {:0" + str(self.GetChromosomeLen()) + "b} | {} | {:6.3} | {:6.3}"
        #return form.format(self.chromosome, self.GetVariables(),self.GetFitness(), self.keff)
        form = " {:0" + str(self.GetChromosomeLen()) + "b} | {:6.3} | {:6.3}"
        return form.format(self.chromosome,float(self.GetFitness()), float(self.keff))

    def GetVariables(self):
        variables = []
        bin_str = bin(self.chromosome)[2:].zfill(self.GetChromosomeLen())
        pos = 0
        for i, l in enumerate(self.__chromo_len):
            integer = int ( bin_str[pos : pos + l], base = 2 )
            variables.append(self.__min_vals[i] + (integer * (self.__max_vals[i]-self.__min_vals[i]))/float((2**self.__chromo_len[i])-1))
            pos += l
        return variables

    # diff (difficulty) if higher then hadrer 
    def GetFitness(self, diff = 20):
        if diff < 20 : 
            add = (20-diff)*0.05
        else:
            add = 0
        return ((10000*(1-abs(self.keff-1))**40)/(self.GetVariables()[0]**3 * (18.1) + self.GetVariables()[1]**3 * 1.0) + add)


    def GetChromosomeLen(self):
        sum = 0
        for l in self.__chromo_len: sum += l
        return sum

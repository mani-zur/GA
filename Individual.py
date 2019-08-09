import random
from math import exp

random.seed()


class Individual:
    __min_vals = [1, 0]
    __max_vals = [10,20]
    __chromo_len = [16, 16]
    
    def __init__(self, Chromosome = -1):
        if Chromosome == -1 : self.chromosome = random.randint(0,(2**self.GetChromosomeLen())-1)
        else : self.chromosome = Chromosome
        self.keff = 0.0
        self.file_association = ""

    def GetVariables(self):
        variables = []
        bin_str = bin(self.chromosome)[2:].zfill(self.GetChromosomeLen())
        pos = 0
        for i, l in enumerate(self.__chromo_len):
            integer = int ( bin_str[pos : pos + l], base = 2 )
            variables.append(self.__min_vals[i] + (integer * (self.__max_vals[i]-self.__min_vals[i]))/float((2**self.__chromo_len[i])-1))
            pos += l
        return variables

    def GetFitness(self):
        return (-abs(self.keff-1)+1)**6 * (10 - self.GetVariables()[0])**3
        #return (-abs(self.keff-1)+1)**10 * 1.0 / self.GetVariables()[0]
        #return exp(-(self.keff-1)**2)**4-0.015625
        #return 1.0/abs(1-self.keff)

    def GetChromosomeLen(self):
        sum = 0
        for l in self.__chromo_len: sum += l
        return sum

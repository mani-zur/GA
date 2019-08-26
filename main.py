#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Population import Population

def main():
    pop = Population(50) #count of individuals
    pop.SetDirectoryInput("/nica/user/z/zurkowski/Serpent", "uranium_reflected.inp") #for cluster
    pop.MakeInputs()
    pop.MakeReport()
    while pop.GetMaxFit() < 0.5 :
        pop.NewGeneration()
    #for i in range(10): #nuber of generations
    #    pop.NewGeneration()

if __name__ == '__main__':
    main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Population import Population

def main():
    pop = Population(30) #count of individuals
    pop.SetDirectoryInput("/nica/user/z/zurkowski/Serpent", "uranium_reflected.inp")
    pop.MakeInputs()
    pop.MakeReport()
    for i in range(15): #nuber of generations
        pop.Roulette()
        pop.Reproduction()
        pop.MakeInputs()
        pop.MakeReport()

if __name__ == '__main__':
    main()

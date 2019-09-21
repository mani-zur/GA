#!/usr/bin/env python
# -*- coding: utf-8 -*-

#This is config file, here you can edit enivromental variables

#SIMULATION SETTINGS
MAIN_DIR = "/~"             #Project directory (see README.md)
INPUT_FILE = "example.inp"  #Name of input file
CORE_AMOUNT = 1             #Set how many cores can serpent use             

#GA SETTINGS
POP_QUALITY = 50            #Population Quality
LOOP_TYPE = "FOR"           #Type of loop chose: "FOR", "WHILE"
LIMITER = 10                #FOR - iteration count, WHILE - minimal fit function
MUTATION_RATE = 0.01        #Must be double betwen 0 and 1


#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Population import Population
import config

def main():
	pop = Population( config.POP_QUALITY , config.MUTATION_RATE ) #count of individuals
	pop.SetDirectoryInput( config.MAIN_DIR , config.INPUT_FILE, config.CORE_AMOUNT ) #file config
	if pop.MakeInputs():
		pop.MakeReport()
		if config.LOOP_TYPE == "FOR":
			for i in range( config.LIMITER ): pop.NewGeneration()
		if config.LOOP_TYPE == "WHILE":
			while pop.GetMaxFit() < config.LIMITER : pop.NewGeneration()

if __name__ == '__main__':
    main()

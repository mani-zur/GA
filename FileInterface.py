#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os import path
import subprocess

class FileInterface:
    
    def __init__(self, Sss2 , input):
        self.sss2 = Sss2
        self.input_file_name = input

    def MakeInput (self, output_path, name , args):
        if(path.isfile(self.input_file_name)):
            input = open(self.input_file_name,"r")
            output_full_path = output_path + "/" + name
            output = open(output_full_path, "w")
            i = 0
            for line in input:
                if "{}" in line:
                    line = line.replace("{}",str(args[i]))
                    i += 1
                output.write(line)

            input.close()
            output.close()
            return output_full_path
        else:
            print("No input file !!!")
            return False

    def RunInput(self, input_path):
        if not(path.isfile(input_path + "_res.m")):     #sprawdzenie czy symulacja istnieje
            print("Wykonuję symulację dla : {}".format(input_path))
            subprocess.check_output([self.sss2, "-omp", "60", input_path]) 
        else:
            print("Znalezion symulację : {}".format(input_path))
        
        result = open(input_path + "_res.m", "r")
        for line in result:
            if "ABS_KEFF" in line:
                return float(line[47:58])
        
        


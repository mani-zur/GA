#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os import path
import subprocess
import multiprocessing

class FileInterface:
    
    def __init__(self, Sss2 , input, Core_amount):
        self.sss2 = Sss2
        self.input_file_name = input
        if Core_amount <= multiprocessing.cpu_count():
            self.core_amount = Core_amount
        else:
            self.WriteLog("Error", "Wrong core amount in config.py")
            self.WriteLog("Info ", "Max core amount for this device is " + str(multiprocessing.cpu_count()))
            self.core_amount = 1


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
            self.WriteLog("Error", "Input {} doesn't exist!".format(self.input_file_name))
            return False

    def RunInput(self, input_path):
        if not(path.isfile(input_path + "_res.m")):     #sprawdzenie czy symulacja istnieje
            self.WriteLog("Info ","Wykonuję symulację dla : {}".format(input_path))
            try:
                subprocess.check_output([self.sss2, "-omp", str(self.core_amount), input_path])
            except subprocess.CalledProcessError:   #simulation failed
                self.WriteLog("Error","Symulacja błędna !")
                return 0
        else:
            self.WriteLog("Info ", "Znalezion symulację : {}".format(input_path))
        result = open(input_path + "_res.m", "r")
        for line in result:
            if "ABS_KEFF" in line:
                return float(line[47:58])
        
    def WriteLog(self, type, message): 
        log = open("log.txt", "a")
        print(type + " : " + message)
        log.write(type + " : " + message + "\n")
        log.close()

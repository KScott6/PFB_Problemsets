#!/usr/bin/env python3
import re

fasta = open("Python_07.fasta","r")
fastaFile = fasta.read()

print(re.findall(r">\S+\s.+", fastaFile))







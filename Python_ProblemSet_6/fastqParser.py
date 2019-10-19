#!/usr/bin/env python3
import math
import re

#Remember, structure of fastq is:
	#Line 1: begins with @character and followed by seq identifier and optional description
	#line 2: raw sequence
	#line 3: begins with + character and optionally followed by same seq identifier and optional description
	#line 4: encodes the quality values for seq- MUST contain same number of symbols as letters in the raw seq
#importing fastq file

#it's best to initialize variables outside the with block
totalLineLength = 0
linecount = 1
with open("Python_06.fastq","r") as fastqFile: 
	for line in fastqFile:
		linecount += 1
		totalLineLength += len(line)
	print("Number of lines in file:",linecount)	
	print("Total number of characters:",totalLineLength)
	print("Average number of characters per line:",totalLineLength/linecount)


#!/usr/bin/env python3
import re
#Im using the Python_07.fasta as an example 
#I want to open the fasta file, cleans up any extra newline characters, saves each geneID+description and sequence as key/value in a dict


#opening file
geneID_desc = []
seq = []
with open("Python_07.fasta","r") as fastaFile:
	for line in fastaFile:
		#this is removing the extra whitespace at the end of each line
		line = line.rstrip()
		#I think if we solved the problem up here, it will be easier
		match = re.search(r"^>",line)
		if match:
			geneID_desc.append(line)
		#something is going on here....we could concatenate these lines, but I don't think thats the solution
		else:
			seq.append(line)
	print(geneID_desc)
	print(seq)
		#geneList[geneID_desc] = seq
	#print(geneList)







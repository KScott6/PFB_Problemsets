#!/usr/bin/env python3
import re


#I'm using the fasta file from the 7th problem set as example datafor this fasta parser
fastaFile = open("Python_07.fasta","r")
fastaFile = fastaFile.read()
#this is now a string, and not callable by the regex below
#have to change it into something else- check previous examples

#finds the geneIDs(plus their descriptions) and puts them in capture group 1, then finds the sequence data and puts that in capture group 2
#there might be something wrong with the regex here
for line in fastaFile(r"(^>\S.+\s.+)\n(\w+)\n"):
	#removing excess whitespace, do I have to even worry about this?
	#fasta = fastaFile.rstrip()
	#I don't think I need this below line
	#geneID_desc = re.findall(r"^>\S.+\s.+",fasta)
	geneID_desc = found.group(1)
	seq = found.group(2)
	geneDict[geneID_desc] = seq
print(geneDict)









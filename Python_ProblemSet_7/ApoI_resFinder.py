#!/usr/bin/env python3
import re


with open("Python_07_ApoI.fasta", "r") as fastaFile:
	fastaFileS = fastaFile.read()
	#this is finding the RAATTY cut site location(s) in the provided fasta file
	for found in re.finditer(r"([AG]AATT[CT])", fastaFileS):
		#for each instance of a found RAATTY cut site, saving out the actual sequence start position of it in a variable
		cutStartPos = found.start(1)+2
		#as well as the actual sequence of the site
		cutSites = found.group(1)

for position in cutSites:
	newCutSites = re.sub(r"AA", "^AA",cutSites)
	print("Cut site:",newCutSites,"is at start position",cutStartPos)
print("There are",len(cutSites),"total")
	














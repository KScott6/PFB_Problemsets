#!/usr/bin/env python3
import re
#Im using the Python_07.fasta as an example 
#I want to open the fasta file, cleans up any extra newline characters, saves each gene and sequence as key/value in a dict
#does this work on sequences that don't have descriptions?

#opening file
geneID_list = []
desc_list = []
seq_list = [] #ended up not needing this, but could be used in a different method of a fasta parser
gene_dict = {}
seq = ''
fullseq = ''
with open("Python_08.fasta","r") as fastaFile:
	for line in fastaFile:
		line = line.rstrip()
		#this is removing the extra whitespace at the end of each line
		match = re.search(r"(^>\S+)(\s+.+)",line)	
		if match:
			geneID = match.group(1)
			desc = match.group(2)
			geneID_list.append(geneID)
			#I've made a list of descriptions here, just in case we need this info for later
			desc_list.append(desc)
			fullseq = ''
			#I commented out the below line to try the dict-zip method
			#gene_dict[geneID] = ''
		else:
			fullseq += (line)
			#empties the 'fullseq' variable so it doesn't grow perpetually larger
			seq_list.append(fullseq)
	#print(geneID_list)
	#print(desc_list)
	#print(gene_dict)
gene_dict = dict(zip(geneID_list, seq_list))
print(gene_dict)
print(len(gene_dict))







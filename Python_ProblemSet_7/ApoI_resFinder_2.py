#!/usr/bin/env python3
import re
#does this work on sequences that don't have descriptions?

#opening file
geneID_list = []
seq_list = []
gene_dict = {}
seq = ''
fullseq = ''
with open("Python_07_ApoI.fasta","r") as fastaFile:
	for line in fastaFile:
		line = line.rstrip()
		#this is removing the extra whitespace at the end of each line
		match = re.search(r"(^>\S+)",line)
		if match:
			geneID = match.group(1)
			geneID_list.append(geneID)
			fullseq = ''
			#I commented out the below line to try the dict-zip method
			#gene_dict[geneID] = ''
		else:
			fullseq += (line)
			#empties the 'fullseq' variable so it doesn't grow perpetually larger
			#seq_list.append(fullseq)
	#print(geneID_list)
	#print(desc_list)
	#print(gene_dict)
gene_dict = dict(zip(geneID_list, seq_list))
#print(gene_dict)
print(len(gene_dict))
print(seq_list)





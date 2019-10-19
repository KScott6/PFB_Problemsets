#!/usr/bin/env python3
import re
#Im using the Python_07.fasta as an example 
#I want to open the fasta file, cleans up any extra newline characters, saves each gene and sequence as key/value in a dict


#opening file
geneID_list = []
desc_list = []
#seq_list = [] #ended up not needing this, but could be used in a different method of a fasta parser
gene_dict = {}
seq = ''
with open("Python_07.fasta","r") as fastaFile:
	for line in fastaFile:
		#this is removing the extra whitespace at the end of each line
		line = line.rstrip()
		match = re.search(r"(^>\S+)(\s+.+)",line)
		if match:
			geneID = match.group(1)
			desc = match.group(2)
			geneID_list.append(geneID)
			#I've made a list of descriptions here, just in case we need this info for later
			desc_list.append(desc)
			gene_dict[geneID] = ''
		else:
			seq += line
			#maybe can make a list of seq so we can dict-zip?
			#seq_list.append(seq) #haven't tested this, would also have to comment out the below line
			gene_dict[geneID] = seq	
	print(geneID_list)
	print(desc_list)
	print(gene_dict)

#I this could be another viable method- making the two lists of geneID and seq and then dict-zipping them together
#	print(seq_list)
#	gene_dict = dict(zip(geneID_list, seq_list))
#	print(gene_dict)
	







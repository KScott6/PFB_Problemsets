#!/usr/bin/env python3

#creating an empty dictionary for the genes/seq
genes = {}

#this chunk of code reads in the tab-delimited file, strips the whitespaces, and adds each string in as a key and value into the dictionary 'genes'
revCompSeq = [] #creating an empty list for the eventual reverse complements
with open("Python_06.seq.txt","r") as dnaSeq:
	for line in dnaSeq:
		#removes extra new line characters within the sequences
		line = line.rstrip()
		#splits the columns based on whitespaces
		gene_id,seq = line.split()
		#below is where I change the sequences to their reverse complements
		seq = seq.replace("A","t")
		seq = seq.replace("T","a")
		seq = seq.replace("C","g")
		seq = seq.replace("G","c")
		seqCompUC = seq.upper()
		#reversing the sequences
		revComp = seqCompUC[::-1]
		genes[gene_id] = revComp
print(genes)

#this command takes the information in the genes dictionary and prints it to a fasta
with open("RevComp.fasta","w") as rcFasta:
	for line in genes:
		rcFasta.write(">" + gene_id + " " + "#the following seq is the reverse complement" + "\n" + revComp + "\n")


	













#!/usr/bin/env python3

dnaSeq = "AAATTTGCGCAGTCT"
#There are 4 As and 5 Ts in this test seq

NumberAs = dnaSeq.count('A')
NumberTs = dnaSeq.count('T')
totalNumNuc = len(dnaSeq)

ATproportion = ((NumberAs + NumberTs)/totalNumNuc)*100
print(NumberAs)
print(NumberTs)
print(totalNumNuc)
print("AT proportion in DNA sequence = ",ATproportion,"%",sep='')



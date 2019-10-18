#!/usr/bin/env python3

dnaSeq = "ATGCAGGGGAAACATGATTCAGGAC"

replacement1 = dnaSeq.replace('A','t')
replacement2 = replacement1.replace('T','a')
replacement3 = replacement2.replace('C','g')
replacement4 = replacement3.replace('G','c')

comp = replacement4.upper()
revComp = comp[::-1]

string = """Original Sequence 5'{} 3'
Complement 3'{} 5'
Reverse Complement 5'{} 3'"""

new_string = string.format(dnaSeq,comp,revComp)
print(new_string)
#still need to fix the white space issue with the output





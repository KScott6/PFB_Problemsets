#!/usr/bin/env python3
import re


poem = open("Python_07_nobody.txt","r")
poem_contents = poem.read()

#this finds every instance of "Nobody" and prints out the position of each to the commd line
re.findall(r"(Nobody)", poem_contents)
#for found in re.finditer(r"(Nobody)",poem_contents):
#	nobody_start = found.start(1)+1
#	print(nobody_start)

#now I am going to replace each instance of "Nobody" with "Andy"
new_poem = open("Andy.txt","w")
new_poem.write(re.sub(r"Nobody","Andy",poem_contents))
print(new_poem)










#!/usr/bin/env python3
import sys


favDict = {'song' : "Paradise by the Dashboard Light" , 'movie' : 'Happy Feet' , 'color' : 'purple'}

#print(favDict['song'])
favDict['organism'] = 'meerkats'
print(favDict['organism'])
favDict['organism'] = 'cat'
print(favDict['organism'])

#can use variables assigned a key term to look up values in a dictionary
#fav_thing = 'organism'
#print(favDict[fav_thing])

#can use the input from the command line to look up values in the dictionary
#fav_thing = sys.argv[1]
#print(favDict[fav_thing])

#I have no idea what I need to do for the input() function...ask again later
#str = input("Enter your input: ")






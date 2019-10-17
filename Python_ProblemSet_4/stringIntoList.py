#!/usr/bin/env python3

taxa = "sapiens, erectus, neanderthalensis"
#print(taxa[1])
#this just returns 'a' since taxa is a string
#print(type(taxa))

#splitting the string based on ',', renaming new list as species
species = taxa.split(',')
print(species)

species[1]
print(type(species))

#sorts by alphabetical order (by making all characters all lowercase first then sorting by ASCII value)
print(sorted(species, key = str.lower, reverse=False))

#sorts by length of each string in the list
print(sorted(species, key = len, reverse=False))

#!usr/bin/env python3
import sys

dummyVar = sys.argv[1]
print(type(dummyVar))
if dummyVar == 'False':
	dummyVar = False
	print(dummyVar, "is False")
elif bool(dummyVar) is True:
	message = "is True"
	print(dummyVar, message)
else:
	message = "is Not True"
	print(dummyVar, message)


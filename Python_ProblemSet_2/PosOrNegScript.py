#!usr/bin/env python3
import sys

inputNumber = int(sys.argv[1])
print(type(inputNumber))

if inputNumber == 50:
	print(inputNumber, "is equal to 50")
elif inputNumber > 0:
	if inputNumber < 50:
		if inputNumber%2 == 0:
			print(inputNumber, "is an even number less than 50")
		else:
			print(inputNumber, "is greater than 0 and less than 50")
	elif inputNumber%3 == 0:
		print(inputNumber, "is greater than 0 and divisible by 3")
	else:
		print(inputNumber, "is positive and greater than 50")		
elif inputNumber == 0:
	print(inputNumber, "is equal to zero")
else:
	print(inputNumber, "is negative")



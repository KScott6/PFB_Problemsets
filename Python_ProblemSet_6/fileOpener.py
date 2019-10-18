#!/usr/bin/env python3

ucSong = open("Python_06_uc.txt", "w")
with open("Python_06.txt","r") as song:
	for line in song:
		ucLine = line.upper()
		print(ucLine)
		ucSong.write(ucLine)









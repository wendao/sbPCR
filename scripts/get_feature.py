#!/usr/bin/env python

import os
abs_file = os.path.abspath(__file__)
abs_dir = abs_file[:abs_file.rfind("/")]

lines = open(abs_dir+"/../models/top250_v1", "r").readlines()
space = []
length = []
for line in lines:
	space.append(line.split()[2])
	length.append(int(line.split()[1]))
align = open("align", "r").readlines()
features = open("formated_input", "w")
for peptide in align:
	peptide = peptide.strip().split()[2]
	peptide = list(peptide)
	features.write("0 ")
	for i in range(250):
		temp_peptide = peptide[20-length[i]:21+length[i]]
		k = int(list(space[i])[1])
		count = 0
		for j in range(2*length[i] - k ):
			if temp_peptide[j] == list(space[i])[0] and temp_peptide[j + k + 1] == list(space[i])[2]:
				count = count + 1
		features.write(str(i+ 1) + ":" + str(count) + " ")
	features.write("\n")

#!/usr/bin/env python

import sys

#cmd features align

features = open(sys.argv[1], "r")
number = []
for feature in features:
	number.append(int(feature.strip().split()[-1]))
train = open("train", "w")
whole = open(sys.argv[2], "r")
for line in whole:
	line = line.strip().split()
	train.write(line[0] + " ")
	for i in range(len(number)):
		temp = line[number[i]]
		new = str(i+1) + ":" + temp.split(":")[1]
		train.write(new + " ")
	train.write("\n")

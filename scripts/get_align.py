#!/usr/bin/env python
import sys
#get 40 resi around cys
seq = open(sys.argv[1], 'r').readlines()
align = open("align", "w")
#get cys alignment
ii = 0
while ii < len(seq):
	sequence = ""
	if ">" in list(seq[ii]):
		gene = seq[ii].split("|")[1]
		ii = ii + 1
		while ii < len(seq) and ">" not in list(seq[ii]) :
			sequence = sequence + seq[ii].strip()
			ii = ii + 1
	list_seq = list(sequence)
	for i in range(len(list_seq)):
		if list_seq[i] == "C":
			align.write(gene + " " + str(i+1) + " ")
			if i < 20:
				for j in range(20-i):
					align.write("-")
				align.write("".join(list_seq[:i+1]))
			else:
				align.write("".join(list_seq[i-20:i+1]))
			if i > len(list_seq) - 21:
				align.write("".join(list_seq[i+1:]))
				for j in range(21-len(list_seq)+i):
					align.write("-")
				align.write("\n")
			else:
				align.write("".join(list_seq[i+1:i+21]) + "\n")




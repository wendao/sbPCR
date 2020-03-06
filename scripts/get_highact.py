#!/usr/bin/env python
predict = open("predict", "r").readlines()
align = open("align", "r").readlines()
high = open("high_act", "w")
for i in range(len(predict)):
	if predict[i].strip() == "1":
		high.write(align[i])

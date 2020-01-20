#!/usr/bin/python3

#import numpy as np

#Y = np.array([2, 14, -13, 5, 12, 4, -19])

def std(x):
	mean = 0.0
	ret = 0.0
	count = 0
	for y in x:
		mean = mean + y
		count = count + 1
	if (count == 0):
		return(None)
	mean = (mean / count)
	for z in x:
		ret = ret + (((z - mean)**2) / count)
	ret = ret**0.5
	return(ret)

#print(std(Y))
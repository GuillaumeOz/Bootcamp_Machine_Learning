#!/usr/bin/python3

#import numpy as np

#X = np.array([0, 15, -9, 7, 12, 3, -21])

def variance(x):
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
	return(ret)

#print(variance(X/2))
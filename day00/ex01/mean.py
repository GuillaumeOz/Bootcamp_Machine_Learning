#!/usr/bin/python3

#import numpy as np

#X = np.array([0, 15, -9, 7, 12, 3, -21])

def mean(x):
	number = 0.0
	count = 0
	for y in x:
		number = number + y
		count = count + 1
	if (count == 0):
		return(None)
	number = (number / count)
	return(number)

#print(mean(X ** 2))
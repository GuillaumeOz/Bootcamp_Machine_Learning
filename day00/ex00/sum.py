#!/usr/bin/python3

#import numpy as np

#X = np.array([0, 15, -9, 7, 12, 3, -21])

def sum_(x, f):
	number = 0.0
	if (x.size == 0):
		return(None)
	try:
		f(x[0])
	except ValueError:
		return(None)
	for y in x:
		number = number + f(y)
	return(number)

#print(sum_(X, lambda x: x**2))
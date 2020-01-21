#!/usr/bin/python3

#import numpy as np

#X = np.array([0, 15, -9, 7, 12, 3, -21])
#Y = np.array([2, 14, -13, 5, 12, 4, -19])

def dot(x, y):
	dot_ret = 0.0
	if((x.size == 0) or (y.size == 0)):
		return(None)
	if (x.size != y.size):
		return(None)
	dot_ret = sum([x * y for x, y in zip(x, y)])
	return(dot_ret)

#print(dot(X, Y))

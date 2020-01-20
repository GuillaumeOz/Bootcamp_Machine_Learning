#!/usr/bin/python3

import numpy as np

X = np.array([0, 15, -9, 7, 12, 3, -21])
Y = np.array([2, 14, -13, 5, 12, 4, -19])

def dot(x, y):
	ret = 0.0
	dot_x = 0.0
	dot_y = 0.0
	count_x = 0
	count_y = 0
	for i in x:
		dot_x = dot_x + i
		count_x = count_x + 1
	for j in y:
		dot_y = dot_y + j
		count_y = count_y + 1
	if ((count_x == 0) or (count_y == 0)):
		return(None)
	if (count_x != count_y):
		return(None)
	return(ret)

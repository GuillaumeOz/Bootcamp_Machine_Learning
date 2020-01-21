#!/usr/bin/python3

import numpy as np

# W = np.array([
#     [ -8, 8, -6, 14, 14, -9, -4],
#     [ 2, -11, -2, -11, 14, -2, 14],
#     [-13, -2, -5, 3, -8, -4, 13],
#     [ 2, 13, -14, -15, -14, -15, 13],
#     [ 2, -1, 12, 3, -7, -3, -6]]) #5x7
# X = np.array([0, 15, -9, 7, 12, 3, -21]).reshape((7,1))# 7x1
# Y = np.array([2, 14, -13, 5, 12, 4, -19]).reshape((7,1))

def mat_vec_prod(x, y):
	mvp_ret = np.zeros((x.shape[0],1))
	mvp_count = -1
	if((x.size == 0) or (y.size == 0)):
		return(None)
	for i in x:
		row = 0
		mvp_count = mvp_count + 1
		while(row < y.shape[0]):
			mvp_ret[mvp_count] = mvp_ret[mvp_count] + (y[row][0] * i[row])
			row = row + 1
	return(mvp_ret)

#print(mat_vec_prod(W, X))
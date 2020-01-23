#!/usr/bin/python3

# import numpy as np

def mat_mat_prod(x,y):
	nb_row_x, nb_col_x = x.shape[0], x.shape[1]
	nb_row_y, nb_col_y = y.shape[0], y.shape[1]
	array = np.zeros((nb_row_x, nb_col_y))
	# pour chaque ligne de x
	i = 0
	while i < nb_row_x:
		# pour chaque colonne de y
		j = 0
		while j < nb_col_y:
			#print(i + j)
			row_x = x[i, :] # toute la ligne
			col_y = y[:, j] # toute la colone 
			array[i][j] = np.dot(row_x, col_y)
			j += 1
		i += 1
	return(array)

# def main():
# 	W = np.array([
# 		[ -8, 8, -6, 14, 14, -9, -4],
# 		[ 2, -11, -2, -11, 14, -2, 14],
# 		[-13, -2, -5, 3, -8, -4, 13],
# 		[ 2, 13, -14, -15, -14, -15, 13],
# 		[ 2, -1, 12, 3, -7, -3, -6]])

# 	Z = np.array([
# 		[ -6, -1, -8, 7, -8],
# 		[ 7, 4, 0, -10, -10],
# 		[ 7, -13, 2, 2, -11],
# 		[ 3, 14, 7, 7, -4],
# 		[ -1, -3, -8, -4, -14],
# 		[ 9, -14, 9, 12, -7],
# 		[ -9, -4, -10, -3, 6]]) # 7 x 5
# 	print(mat_mat_prod(W, Z))

# if __name__ == '__main__':
# 	main()
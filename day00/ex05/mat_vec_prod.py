#!/usr/bin/python3

import numpy as np

def mat_vec_prod(x, y):
	sum([x * y for i, j in zip(x, y)])
def complete(matrix,max):
	for x in range(max):
		for y in range(max):
			if matrix[x][y]==0:
				return False
	return True
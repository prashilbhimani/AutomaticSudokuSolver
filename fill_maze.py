def fillmaze(matrix,max):
	for i in range(max*max):
		for j in range(max*max):
			matrix[i][j]=set(range(1, max*max+1))
	return matrix

	

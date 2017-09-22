def countzero(max,matrix):
	count=0
	for x in range(max):
		for y in range(max):
			if matrix[x][y]==0:
				count=count+1
	return count
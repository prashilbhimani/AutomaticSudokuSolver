
def setmatrix(matrix,max,possiblemaze):
	for i in range(max):
		for j in range(max):
			if len(possiblemaze[i][j])==1:
				k=possiblemaze[i][j].pop()
				matrix[i][j]=k
				possiblemaze[i][j].add(k)
	return matrix
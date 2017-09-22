def checkcolumn(matrix,max,possiblemaze):
	for i in range(max):
		for j in range(max):
			if matrix[j][i]!=0:
				possiblemaze[j][i].clear()
				possiblemaze[j][i].add(matrix[j][i])
				for x in range(max):
					if x!=j:
						possiblemaze[x][i].discard(matrix[j][i])
	return possiblemaze

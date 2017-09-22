
def checkrow(matrix,max,possiblemaze):
	for i in range(max):
		for j in range(max):
			if matrix[i][j]!=0:
				possiblemaze[i][j].clear()
				possiblemaze[i][j].add(matrix[i][j])
				for x in range(max):
					if x!=j:
						possiblemaze[i][x].discard(matrix[i][j])
	return possiblemaze

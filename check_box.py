def checkbox(matrix,max,possiblemaze):
	for x in range(max):
		for y in range(max):
			for i in range(max):
				for j in range(max):
					if matrix[i+max*x][j+max*y]!=0:
						for q in range(max):
							for r in range(max):
								if q!=i and r!=j:
									possiblemaze[q+max*x][r+max*y].discard(matrix[i+max*x][j+max*y])

	return possiblemaze
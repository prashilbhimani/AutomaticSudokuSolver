def intelligentrow(matrix,max,possiblemaze):
	for i in range(max):
		countlist=[0] * max
		for j in range(max):
			for k in range(max):
				if k+1 in possiblemaze[i][j]:
					countlist[k]=countlist[k]+1
		for q in range(max):
			if countlist[q]==1:
				for x in range(max):
					if q+1 in possiblemaze[i][x]:
						possiblemaze[i][x].clear()
						possiblemaze[i][x].add(q+1)
	return possiblemaze
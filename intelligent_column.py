def intelligentcolumn(matrix,max,possiblemaze):
	for i in range(max):
		countlist=[0] * max
		for j in range(max):
			for k in range(max):
				if k+1 in possiblemaze[j][i]:
					countlist[k]=countlist[k]+1
		for q in range(max):
			if countlist[q]==1:
				for x in range(max):
					if q+1 in possiblemaze[x][i]:
						possiblemaze[x][i].clear()
						possiblemaze[x][i].add(q+1)
	return possiblemaze
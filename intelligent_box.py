def intelligentbox(matrix,max,possiblemaze):
	for x in range(max):
		for y in range(max):
			countdict={}
			for m in range(max*max):
				countdict.setdefault(m+1,0)
			for i in range(max):
				for j in range(max):
					for k in possiblemaze[i+max*x][j+max*y]:
						countdict[k]=countdict[k]+1
			for key, value in countdict.items():
				if value==1:
					for i in range(max):
						for j in range(max):
							if key in possiblemaze[i+max*x][j+max*y]:
								possiblemaze[i+max*x][j+max*y].clear()
								possiblemaze[i+max*x][j+max*y].add(key)
	return possiblemaze
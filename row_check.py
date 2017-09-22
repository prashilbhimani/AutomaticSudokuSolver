def rowcheck(possiblemaze,max):
	
	for i in range(max):
		countdict={}
		for m in range(max):
			countdict.setdefault(m+1,0)
		for j in range(max):
			if len(possiblemaze[j][i])==0:
				return False
			for x in possiblemaze[i][j]:
				countdict[x]=countdict[x]+1
		for k in range(max):
			if countdict[k+1]==0:
					return False
	return True
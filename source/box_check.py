def boxcheck(possiblemaze,max):
	for x in range(max):
		for y in range(max):
			countdict={}
			for m in range(max*max):
				countdict.setdefault(m+1,0)
			for i in range(max):
				for j in range(max):
					for z in possiblemaze[i+max*x][j+max*y]:
						countdict[z]=countdict[z]+1
			for k in range(max*max):
				if countdict[k+1]==0:
					return False
	return True
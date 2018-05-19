def check(possiblemaze,max):
	flag1=rowcheck(possiblemaze,max*max)
	flag2=columncheck(possiblemaze,max*max)
	flag3=boxcheck(possiblemaze,max)
	if flag1 and flag2 and flag3:
		return True
	else:
		return False

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


def columncheck(possiblemaze,max):
	
	for i in range(max):
		countdict={}
		for m in range(max):
			countdict.setdefault(m+1,0)
		for j in range(max):
			if len(possiblemaze[j][i])==0:
				return False
			for x in possiblemaze[j][i]:
				countdict[x]=countdict[x]+1
		for k in range(max):
			if countdict[k+1]==0:
				return False
	return True

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
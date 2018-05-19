def sub_position(matrix,max,possiblemaze):
	length=max
	i=-1
	j=-1
	#print(i,j,length)
	for x in range(max):
		for y in range(max):
			if len(possiblemaze[x][y])<length and len(possiblemaze[x][y])>1:
				length=int(len(possiblemaze[x][y]))
				i=x
				j=y
	return i,j,length
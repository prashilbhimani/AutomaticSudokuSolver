def printpossible(max,possiblemaze):
	for i in range(max):
		for j in range(max):
			print("Row number %d Column number %d"%(i+1,j+1))
			print(possiblemaze[i][j])
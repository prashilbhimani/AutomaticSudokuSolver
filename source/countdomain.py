def count_domain(max,possiblemaze):
	count=0
	for x in range(max):
		for y in range(max):
			count=count+len(possiblemaze[x][y])
	return count
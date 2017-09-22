import sys
def printmatrix(matrix,max):
	for x in range(max):
		for y in range(max):
			if matrix[x][y]!=0:
				sys.stdout.write(str(matrix[x][y]))
			else:
				sys.stdout.write("_")
			sys.stdout.write(" ")
		print("")
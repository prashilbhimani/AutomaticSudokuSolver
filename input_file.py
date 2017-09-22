from print_matrix import printmatrix
def inputfile(matrix,max,a):
	k=0
	for i in range(max*max):
		for j in range(max*max):
			matrix[i][j]=int(a[k])
			k=k+1
	#printmatrix(matrix,max*max)
	#print("")
	return matrix
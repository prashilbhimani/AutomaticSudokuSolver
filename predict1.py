from sudoku_solver import basicsolver
from set_matrix import setmatrix
import copy
from check_complete import complete
from print_matrix import printmatrix

def prediction(matrix,max,possiblemaze,boxpredicted,leng):
	if complete(matrix,max*max):
		printmatrix(matrix,max*max)
	else:
		i,j,length=sub_position(matrix,max*max,possiblemaze)
		print(length)
		boxpredicted=boxpredicted+1
		leng=leng+length
		for x in possiblemaze[i][j]:
			sub_matrix=copy.deepcopy(copy.deepcopy(matrix))
			sub_possiblemaze=copy.deepcopy(copy.deepcopy(copy.deepcopy(possiblemaze)))
			sub_possiblemaze[i][j].clear()
			sub_possiblemaze[i][j].add(x)
			sub_matrix=setmatrix(sub_matrix,max*max,sub_possiblemaze)
			sub_matrix,max,sub_possiblemaze=basicsolver(sub_matrix,max,sub_possiblemaze)
			if complete(sub_matrix,max*max):
				printmatrix(sub_matrix,max*max)
				return boxpredicted,leng
			if check(sub_possiblemaze,max):
				boxpredicted,leng=prediction(sub_matrix,max,sub_possiblemaze,boxpredicted,leng)
				return boxpredicted,leng
	return boxpredicted,leng

def sub_position(matrix,max,possiblemaze):
	length=max
	i=-1
	j=-1
	#print(i,j,length)
	for x in range(max):
		for y in range(max):
			if len(possiblemaze[x][y])<length and len(possiblemaze[x][y])>1:
				length=len(possiblemaze[x][y])
				i=x
				j=y
	return i,j,length

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

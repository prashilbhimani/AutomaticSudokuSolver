from check_row import checkrow
from check_column import checkcolumn
from check_box import checkbox
from set_matrix import setmatrix
from intelligent_row import intelligentrow
from intelligent_column import intelligentcolumn
from intelligent_box import intelligentbox
from zero_count import countzero
from countdomain import count_domain
import copy

def basicsolver(sub_matrix,max,sub_possible_maze):
	matrix=copy.deepcopy(copy.deepcopy(sub_matrix))
	possible_maze=copy.deepcopy(copy.deepcopy(copy.deepcopy(sub_possible_maze)))
	times=0
	count=countzero(max*max,matrix)
	flag1=True
	while flag1:
		flag=True
		while flag:
			possible_maze=checkrow(matrix,max*max,possible_maze)
			matrix=setmatrix(matrix,max*max,possible_maze)
			possible_maze=checkcolumn(matrix,max*max,possible_maze)
			matrix=setmatrix(matrix,max*max,possible_maze)
			possible_maze=checkbox(matrix,max,possible_maze)
			matrix=setmatrix(matrix,max*max,possible_maze)
			count1=countzero(max*max,matrix)
			if count1<count:
				count=count1
			else:
				flag=False
		c=count_domain(max*max,possible_maze)
		possible_maze=intelligentrow(matrix,max*max,possible_maze)
		matrix=setmatrix(matrix,max*max,possible_maze)
		possible_maze=intelligentcolumn(matrix,max*max,possible_maze)
		matrix=setmatrix(matrix,max*max,possible_maze)
		possible_maze=intelligentbox(matrix,max,possible_maze)
		matrix=setmatrix(matrix,max*max,possible_maze)
		c1=count_domain(max*max,possible_maze)
		if c1<c:
			c1=c
		else:
			flag1=False
		
	
	return matrix,max,possible_maze
	
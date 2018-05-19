from print_matrix import printmatrix
from fill_maze import fillmaze
from print_possible import printpossible
from sudoku_solver import basicsolver
from predict1 import prediction
from input_file import inputfile
import time
start_time = time.time()
max=3  
maze = [[0 for x in range(max*max)] for x in range(max*max)]
possible_maze = [[0 for x in range(max*max)] for x in range(max*max)]
f=open("sudoku.txt")
number=1
totalpred=0
totallen=0
for line in f:
	print("Sudoku # %d" %number)
	maze=inputfile(maze,max,line)

	possible_maze=fillmaze(possible_maze,max)
	boxpredicted=0
	maze,max,possible_maze=basicsolver(maze,max,possible_maze)
	leng=0
	boxpredicted,leng=prediction(maze,max,possible_maze,0,0)	
	totallen=totallen+leng
	totalpred=totalpred+boxpredicted
	print(boxpredicted)
	print(leng)
	number=number+1
print("Total")
print(totalpred)
print(totallen)

print("--- %s seconds ---" % (time.time() - start_time))

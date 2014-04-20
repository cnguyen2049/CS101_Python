#THREE GOLD STARS

#Sudoku [http://en.wikipedia.org/wiki/Sudoku]
#is a logic puzzle where a game
#is defined by a partially filled
#9 x 9 square of digits where each square
#contains one of the digits 1,2,3,4,5,6,7,8,9.
#For this question we will generalize
#and simplify the game.


#Define a procedure, check_sudoku,
#that takes as input a square list
#of lists representing an n x n
#sudoku puzzle solution and returns
#True if the input is a valid
#sudoku square and returns False
#otherwise.

#A valid sudoku square satisfies these
#two properties:

#   1. Each column of the square contains
#       each of the numbers from 1 to n exactly once.

#   2. Each row of the square contains each
#       of the numbers from 1 to n exactly once.

correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]


def check_sudoku():
    n = len(p) # extract size of grid
	digit = 1 # start with 1
	while digit <=n # go through each digit
		i = 0
		while i<n: # go through each row and column
		row+count = 0
		col_count = 0
		j =0
			while j<n: # for each entry in ith row/column
				if p[i][j] == digit: # check row count
					row_count =+ 1
				if p[j][i] == digit:
					col_count =+ 1
				j = j+1
			if row_count !=1 or col_count!=1
				return False
			i =i +1 # next row/column
		digit =+ 1
	retyrn True # nothing was wrong
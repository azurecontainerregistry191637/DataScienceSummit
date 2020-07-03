def is_safe(board,row,col,size):
	for c in range(col):
		if board[row][c]==1:
			return False
	i = row
	j = col
	while i>=0 and j>=0:
		if board[i][j]==1:
			return False
		i=i-1
		j=j-1
	i = row
	j = col
	while i<size and j>=0:
		if board[i][j]==1:
			return False
		i=i+1
		j=j-1
	return True

def nQueens(board, col,size):
	if col>=size:
		return True
	for i in range(size):
		if is_safe(board,i,col,size):
			board[i][col]=1
			if nQueens(board,col+1,size):
				return True
			board[i][col]=0
	return False
	
size=int(input('Enter the input number :'))

board =[[0 for j in range(size)] for i in range(size)]

if nQueens(board,0, size) == True:
	result = []
	for i in range(size):
		for j in range(size):
			if board[i][j] == 1:
				result.append(j)
			print(board[i][j], end = ' ' )
		print()
	print(result)
else:
	print ("Not possible")

def asd(board):
	board=board.split('/', 8)
	i=0
	for rank in board:
		board[i]=list(rank)
		i+=1
	print board
	for x in board:
		j=0
		for y in x:
			j+=1
			print y
			board[j]=y
	print board

asd('8/8/8/8/5Rqr/pppk4/5K2/8')
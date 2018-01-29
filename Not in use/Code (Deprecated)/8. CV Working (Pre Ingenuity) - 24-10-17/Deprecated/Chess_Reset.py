import numpy
import re
import Chess_Pathfinding as pathfinding
import Chess_Movement as move
# import Chess_Pathfinding as pathfinding


def resetBoard(board,Graves):

	################################################################################
	#    Board defanition   
	################################################################################
	board = board.split(' ', 1)[0] 								# Converts fen board to pathable matrix

	def r(o):return('0,'*11+'0\n0,0,'+''.join(['0,'*int(h)if h.isdigit()else'0,0\n0,0,'if h=='/' else h for h in o])+'0,0\n0'+',0'*11) # Converts fen to a map
	nmap = r(board)
	nmap = re.sub('([A-z]{1})', '1,', nmap)
	nmap = numpy.array([[int(j) for j in i.split(',')] for i in nmap.splitlines()]) # Converts map string to an array of integers

	def R(o):return(''.join(['0,'*int(h)if h.isdigit()else'\n'if h=='/' else h for h in o])) # Converts fen to a map
	board = R(board)
	board = re.sub(r'([A-z])(?!$)', r'\1,', board)
	board = numpy.array([[str(j) for j in i.split(',')] for i in board.splitlines()]) # Converts map string to an array of integers
	board = board[:,:-1]

	for grave in Graves['White']:
		nmap[grave[1]] = 1 if grave[0] != 'e' else 0
	for grave in Graves['Black']:
		nmap[grave[1]] = 1 if grave[0] != 'e' else 0

	# for grave in Graves['White']:
	# 	board[grave[1]] = grave[0] if grave[0] != 'e' else '0'
	# for grave in Graves['Black']:
	# 	board[grave[1]] = grave[0] if grave[0] != 'e' else '0'



	print 'done!\n',nmap , '\n'
	print board
	################################################################################
	#    Reseting Pieces on board  
	################################################################################

	




Graves = {
	'Black': [('p',(1,0)),('p',(2,0)),('p',(3,0)),('p',(4,0)),('n',(5,0)),('r',(6,0)),('q',(7,0)),('e',(8,0)),('e',(1,1)),('e',(2,1)),('e',(3,1)),('e',(4,1)),('e',(5,1)),('e',(6,1)),('e',(7,1)),('e',(8,1))],
	'White': [('P',(8,11)),('P',(7,11)),('P',(6,11)),('P',(5,11)),('P',(4,11)),('P',(3,11)),('N',(2,11)),('N',(1,11)),('R',(8,10)),('B',(7,10)),('R',(6,10)),('Q',(5,10)),('e',(4,10)),('e',(3,10)),('e',(2,10)),('e',(1,10))]
	} # Note White peices are interred in the 'Black' Graves

resetBoard('r1bk4/1pp5/p3b3/3p4/8/1P1n3B/6P1/2K5 w KQkq - 0 1',Graves)
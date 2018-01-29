import numpy
import Chess_Pathfinding as pathfinding
import Chess_CheckPiece as checker
import Chess_Take as take
import Chess_Serial as serial
# import Chess_Movement as makeMove

def resetBoard(nmap,board,wgraves,bgraves):
	board=board.split('/', 8)
	print '\n',board,'\n'
	i=0
	atHome = {'p':0,'r':0,'n':0,'b':0,'P':0,'R':0,'N':0,'B':0}
	home =(0,0)

	for grave in reversed(wgraves):									# Fills cemetary
		position = (grave[0],grave[1])
		char = grave[2]
		if char == 'done':
			break
		else:
			nmap[position] = 1
	for grave in reversed(bgraves):									# Fills cemetary
		position = (grave[0],grave[1])
		char = grave[2]
		if char == 'done':
			break
		else:
			nmap[position] = 1

	for rank in board:
		i+=1
		j=1
		for char in rank:
			if char in ['p','r','n','b','k','q','P','R','N','B','K','Q']:
				j+=1
				position = (i,j)
				nmap[position] = 0
				path = take.take(nmap,position,wgraves,bgraves,char)
				nmap[path[-1]]=1
				serial.makeMove(path)
				print nmap,'\n'
			else:
				j+=int(char)
	for grave in reversed(wgraves):
		position = (grave[0],grave[1])
		char = grave[2]
		if char == 'done':
			break
		else:
			nmap[position] = 0
			home = checker.checkPieceReset(char,atHome)
			path = pathfinding.astar(nmap, home, position)
			serial.makeMove(path)
			nmap[home]=ord(char)
			print nmap,'\n'
	for grave in reversed(bgraves):
		position = (grave[0],grave[1])
		char = grave[2]
		if char == 'done':
			break
		else:
			nmap[position] = 0
			home = checker.checkPieceReset(char,atHome)
			path = pathfinding.astar(nmap, home, position)
			serial.makeMove(path)
			nmap[home]=ord(char)
			print nmap,'\n'
	print 'done!\n',nmap



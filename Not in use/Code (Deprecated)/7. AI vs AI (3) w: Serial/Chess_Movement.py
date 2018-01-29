import numpy
#import Chess_Pathfinding as pathfinding
import Chess_Take as take
import Chess_Knight as knight
import Chess_Reset as reset
import Chess_Serial as serial
import Chess_CheckPiece as checker
import Chess_Pathfinding as pathfinding
import time
import re

################################################################################
#    Movement System 
################################################################################
#     Board layout and coordinate system
#     Cordinates are [rank,column]
#
#      *,*,A,B,C,D,E,F,G,H,*,*
#      0,1,2,3,4,5,6,7,8,9,0,1
#     [0,0,0,0,0,0,0,0,0,0,0,0] 0*
#     [0,0,0,0,0,0,0,0,0,0,0,0] 1
#     [0,0,0,0,0,0,0,0,0,0,0,0] 2
#     [0,0,0,0,0,0,0,0,0,0,0,0] 3
#     [0,0,0,0,0,0,0,0,0,0,0,0] 4
#     [0,0,0,0,0,0,0,0,0,0,0,0] 5
#     [0,0,0,0,0,0,0,0,0,0,0,0] 6
#     [0,0,0,0,0,0,0,0,0,0,0,0] 7
#     [0,0,0,0,0,0,0,0,0,0,0,0] 8
#     [0,0,0,0,0,0,0,0,0,0,0,0] 9*

Graves = {'White': [],'Black': []}
		

def move(board1,board2,startPos,endPos,piece,colour): # The move function generates a path for the piece to move along
	
	################ Move interpretation ################
	startPos = (int(startPos[1]),ord(startPos[0])-95)
	endPos = (int(endPos[1]),ord(endPos[0])-95)
	dist = numpy.subtract(endPos,startPos)
	dVec = []
	dVec.append(-1 if dist[0]<0 else (0 if dist[0]==0 else 1))
	dVec.append(-1 if dist[1]<0 else (0 if dist[1]==0 else 1))
	global path
	global nmap
	global stopPos
	shiftBack = (0,0)
	path = []

	print startPos, endPos, dist, piece


	################  Board Defanition  ################
	board1 = board1.split(' ', 1)[0] 								# Converts fen board to pathable matrix
	board2 = board2.split(' ', 1)[0]
	def r(o):return('0,'*11+'0\n0,0,'+''.join(['0,'*int(h)if h.isdigit()else'0,0\n0,0,'if h=='/' else h for h in o])+'0,0\n0'+',0'*11) # Converts fen to a map
	nmap = r(board1)
	nmap = re.sub('([A-z]{1})', '1,', nmap)
	nmap = numpy.array([[int(j) for j in i.split(',')] for i in nmap.splitlines()]) # Converts map string to an array of integers

	print nmap, '\n'

	################    Fill Graves     ################
	for grave in Graves['White']:
		nmap[grave[1]]=1
	for grave in Graves['Black']:
		nmap[grave[1]]=1

	################      Movement      ################
	if piece == 'k' or piece == 'K' and dist[1]>1: 			# Castling
		# if :
		print colour + ' castle!'
		path.append([startPos,endPos])
		nmap[startPos],nmap[endPos]=0,1
		nmap[(endPos[0],endPos[1]+dVec[1])],nmap[(endPos[0],endPos[1]-dVec[1])]=0,1
		if dVec[1] == -1:
			dVec = [x * 2 for x in dVec]
		rookPath = pathfinding.astar(nmap,(endPos[0],endPos[1]-dVec[1]),(endPos[0],endPos[1]+dVec[1]))
		rookPath.append((endPos[0],endPos[1]-dVec[1]))
		path.append(rookPath)
	else:
		if piece == 'n' or piece == 'N':
			print 'Knight move!'
			nmap[startPos]=0
			shiftBack = knight.knightMove(nmap,startPos,endPos,dist,dVec)
		else:
			print 'Standard move!'
			path.append([startPos,(endPos[0]-dVec[0],endPos[1]-dVec[1])])

		# if (isinstance(path[0], list)):
		stopPos = path[-1][-1]
		# else:
		# 	stopPos = path[-1]

		if nmap[endPos]!= 0:
			print 'Take!'
			takenPiece = checker.checkPieceTaken(board1,board2)
			# take.takePiece(startPos,endPos,piece,takenPiece,colour)
		else:
			pass

		path.append([stopPos,endPos])
		if shiftBack != (0,0):
				path.append(shiftBack)
	nmap[startPos],nmap[endPos]=0,1
			

	# print path,'\n',nmap,'\n'


move('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1','rnbqkbnr/pppppppp/8/8/8/P7/1PPPPPPP/RNBQKBNR w KQkq - 0 1', 'a7', 'a6','P','White');



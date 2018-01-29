import numpy
#import Chess_Pathfinding as pathfinding
import Chess_Take as take
import Chess_Knight as knight
import Chess_Reset as reset
import Chess_Serial as serial
import Chess_CheckPiece as checker
import time
import re

wgraves = [(0,0,'done')]
bgraves = [(0,0,'done')]
##################################################################################
#    Movement System 
##################################################################################


#     Board layout and coordinate system
#      Cordinates are [rank,column]
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


def move(board1,board2,startPos,endPos,piece,doReset): # The move function generates a path for the piece to move along
	
	# Starting and ending positions
	startPos = (9-int(startPos[1]),ord(startPos[0])-95)
	endPos = (9-int(endPos[1]),ord(endPos[0])-95)
	dist = numpy.subtract(endPos,startPos)
	# EP=0
	#print startPos, endPos

	# Board defanition
	board1 = board1.split(' ', 1)[0] 								# Converts fen board to pathable matrix
	board2 = board2.split(' ', 1)[0]
	def r(o):return('0,'*11+'0\n0,0,'+''.join(['0,'*int(h)if h.isdigit()else'0,0\n0,0,'if h=='/' else h for h in o])+'0,0\n0'+',0'*11) # Converts fen to a map
	nmap = r(board1)
	nmap = re.sub('([A-Z]{1})', '1,', nmap)
	nmap = re.sub('([a-z]{1})', '1,', nmap)
	nmap = numpy.array([[int(j) for j in i.split(',')] for i in nmap.splitlines()]) # Converts map string to an array of integers
	#print nmap
	#print '\n'
	
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

	if doReset==1:													# Reset to starting positions
		print '\n\nReset!\n\n'									
		nmap = r(board2)
		nmap = re.sub('([A-Z]{1})', '1,', nmap)
		nmap = re.sub('([a-z]{1})', '1,', nmap)
		nmap = numpy.array([[int(j) for j in i.split(',')] for i in nmap.splitlines()]) # Converts map string to an array of integers
		reset.resetBoard(nmap,board2,wgraves,bgraves)
	else:
		if piece=='k' and abs(endPos[1]-startPos[1])>1:				# Castling
			if (endPos[1]-startPos[1])>1:
				print 'Black king castle!'
				path = (startPos,endPos)
				serial.makeMove(path)
				nmap[startPos]=0
				path = ((1,9), (0,8), (1,7))
				nmap[(1,9)]=0
				nmap[(1,7)]=1
			else:
				print 'Black queen castle!'
				path = (startPos,endPos)
				serial.makeMove(path)
				nmap[startPos]=0
				path = ((1,2), (0,3), (0,4), (1,5))
				nmap[(1,2)]=0
				nmap[(1,5)]=1
		elif piece=='K' and abs(endPos[1]-startPos[1])>1:
			if (endPos[1]-startPos[1])<-1:
				print 'White king castle!'
				path = (startPos,endPos)
				serial.makeMove(path)
				nmap[startPos]=0
				path = ((8,2), (9,3), (9,4), (8,5))
				nmap[(8,2)]=0
				nmap[(8,5)]=1
			else:
				print 'White queen castle!'
				path = (startPos,endPos)
				serial.makeMove(path)
				nmap[startPos]=0
				path = ((8,9), (9,8), (8,7))
				nmap[(8,9)]=0
				nmap[(8,7)]=1
		elif piece=='n':								# Knight
			print 'Knight move!'
			nmap[startPos]=0
			path = knight.knightMove(nmap,startPos,endPos,dist)
		elif piece=='N':								# Knight
			print 'White Knight move!'
			nmap[startPos]=0
			path = knight.knightMove(nmap,startPos,endPos,dist)
		# elif (piece=='p' or piece=='P') and EP==0 and dist[1]!=0:
		# 	victim = (startPos[0],startPos[1]+dist[1])				# En Passant
		# 	nmap[victim] = 0
		# 	path = take.take(nmap,victim,wgraves,bgraves,piece)
		# 	nmap[path[-1]]=1
		# 	serial.makeMove(path)
		# 	print 'En passant!'
		# 	path = (startPos,endPos)
		# 	nmap[startPos]=0
		else:
			print 'Standard move!'									# Standard move
			path = (startPos,endPos)
			nmap[startPos]=0

		if nmap[endPos]!=0:											# Taking 
			if piece=='n':
				tPath = take.take(nmap,endPos,startPos,dist,wgraves,bgraves,checker.checkPieceTaken(board1,board2),knight.shiftBack[1])
				serial.makeMove(tPath)
				serial.makeMove(path)
				serial.makeMove(knight.shiftBack)
			elif piece=='N':
				tPath = take.take(nmap,endPos,startPos,dist,wgraves,bgraves,checker.checkPieceTaken(board1,board2),knight.shiftBack[1])
				serial.makeMove(tPath)
				serial.makeMove(path)
				serial.makeMove(knight.shiftBack)
			else:
				tPath = take.take(nmap,endPos,startPos,dist,wgraves,bgraves,checker.checkPieceTaken(board1,board2),0)
			nmap[endPos]=0

		nmap[endPos]=1
		serial.makeMove(path)
		print nmap
		print '\n'

move('8/8/8/8/5Rqr/pppk4/5K2/8 b - - 0 1','8/8/8/8/5Rqr/pppk4/5K2/8 b - - 0 1', 'd8', 'c7','K',0)
# move('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1','rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1', 'a1', 'a1','p',1)

open('reset.txt', 'w').close()
file = open('reset.txt', 'a')
file.write(str(serial.servoList)+'\n'+'\n') 
file.write(str(len(serial.servoList)))

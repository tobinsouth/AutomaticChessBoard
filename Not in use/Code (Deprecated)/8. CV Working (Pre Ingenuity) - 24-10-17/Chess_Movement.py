import numpy
import Chess_Pathfinding as pathfinding
import re
import Chess_Serial as serial

################################################################################
#    Movement System 
################################################################################
#     Board layout and coordinate system
#     Cordinates are (rank,column)
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

Graves = {
	'Black': [('e',(1,0)),('e',(2,0)),('e',(3,0)),('e',(4,0)),('e',(5,0)),('e',(6,0)),('e',(7,0)),('e',(8,0)),('e',(1,1)),('e',(2,1)),('e',(3,1)),('e',(4,1)),('e',(5,1)),('e',(6,1)),('e',(7,1)),('e',(8,1))],
	'White': [('e',(8,11)),('e',(7,11)),('e',(6,11)),('e',(5,11)),('e',(4,11)),('e',(3,11)),('e',(2,11)),('e',(1,11)),('e',(8,10)),('e',(7,10)),('e',(6,10)),('e',(5,10)),('e',(4,10)),('e',(3,10)),('e',(2,10)),('e',(1,10))]
	} # Note White peices are interred in the 'Black' Graves
		
################################################################################
#    Knight Movement 
################################################################################
def knightMove(nmap,startPos,endPos,dist,dVec): 

	path1 = []
	path2 = []

	knightPath = []
	shiftBack=[(0,0)]
	for i in range(0,dist[0],dVec[0]):
		nextpos=numpy.add(startPos,(i,0))
		nextpos=(nextpos[0],nextpos[1])
		if nmap[nextpos]!=0:
			shift=[nextpos,(nextpos[0]+float(dVec[0])/2,nextpos[1]-float(dVec[1])/2)]
			shiftBack=[shift[1],shift[0]]
			path1.append(shift)
		knightPath.append(nextpos)
	if abs(dist[1])>1:
		nextpos=numpy.add(startPos,(dVec[0],dVec[1]))
		nextpos=(nextpos[0],nextpos[1])
		knightPath.append(nextpos)
		if nmap[nextpos]!=0:
			shift=[nextpos,(nextpos[0]+float(dVec[0])/2,nextpos[1]-float(dVec[1])/2)]
			shiftBack=[shift[1],shift[0]]
			path1.append(shift)
	knightPath.append(endPos)
	path1.append(knightPath)
	if shiftBack != [(0,0)]:
		path1.append(shiftBack) 

	knightPath = []
	shiftBack=[(0,0)]
	for i in range(0,dist[1],dVec[1]):
		nextpos=numpy.add(startPos,(0,i))
		nextpos=(nextpos[0],nextpos[1])
		if nmap[nextpos]!=0:
			shift=[nextpos,(nextpos[0]+float(dVec[0])/2,nextpos[1]-float(dVec[1])/2)]
			shiftBack=[shift[1],shift[0]]
			path2.append(shift)
		knightPath.append(nextpos)
	if abs(dist[0])>1:
		nextpos=numpy.add(startPos,(dVec[0],dVec[1]))
		nextpos=(nextpos[0],nextpos[1])
		knightPath.append(nextpos)
		if nmap[nextpos]!=0:
			shift=[nextpos,(nextpos[0]+float(dVec[0])/2,nextpos[1]-float(dVec[1])/2)]
			shiftBack=[shift[1],shift[0]]
			path2.append(shift)
	knightPath.append(endPos)
	path2.append(knightPath)
	if shiftBack != [(0,0)]:
		path2.append(shiftBack)

	print 'path1', path1, '\n', 'path2', path2 

	if len(path1) <= len(path2):
		for paths in path1:
			path.append(paths)
	else:
		for paths in path2:
			path.append(paths)

################################################################################
#    Taking  
################################################################################
def checkPieceTaken(board1,board2):
	board1 = re.sub('\W+', '', board1)
	board2 = re.sub('\W+', '', board2)
	board1 = re.sub('\d+', '', board1)
	board2 = re.sub('\d+', '', board2)

	def convert_to_ascii(text):
		# print text
		return (ord(char) for char in text)

	takenPiece = chr(abs(sum(convert_to_ascii(board1))-sum(convert_to_ascii(board2)))) #fuck me whalley we made it abs to fix it as not in range(256)
	return takenPiece

def cut(pathIn, k):
	path = [pathIn[0]]
	i=-1

	# print k, i, len(pathIn)
	while i < len(pathIn)-1:
		i=i+1
		for j in range(i,len(pathIn)):
			# print j, pathIn[j]
			if pathIn[i][k] != pathIn[j][k]:
				if j-1 == i:
					# print 'Include' ,i ,' and ' , j
					path.append(pathIn[j])
				else:
					# print 'Combine points ',i ,' to ' , j
					path.append(pathIn[j-1])
					path.append(pathIn[j])
				i=j-1
				break
			if j == len(pathIn)-1 and path[-1] != pathIn[j]:
				path.append(pathIn[j])
				# print 'Combine points ',i ,' to ' , j
				i=j
				break
	pathIn = path
	return path

def cutDiag(pathIn):
	path = [pathIn[0]]
	i=-1

	# print k, i, len(pathIn)
	while i < len(pathIn)-1:
		i=i+1
		for j in range(i,len(pathIn)):
			dist = numpy.subtract(pathIn[j],pathIn[i])
			dVec = [(-1 if dist[0]<0 else (0 if dist[0]==0 else 1)),(-1 if dist[1]<0 else (0 if dist[1]==0 else 1))]
			# print pathIn[i], pathIn[j], dis t, dVec
			if abs(dist[0]) != abs(dist[1]):
				if j-1 == i:
					# print 'Include', j
					path.append(pathIn[j])
				else:
					# print 'Combine points ',i ,' to ' , j
					path.append(pathIn[j-1])
					path.append(pathIn[j])
				i=j-1
				break
			if j == len(pathIn)-1 and path[-1] != pathIn[j]:
				path.append(pathIn[j])
				# print 'Combine points ',i ,' to ' , j
				i=j
				break
	return path

def takePiece(nmap,endPos,takenPiece,colour):
	i=0
	while Graves[colour][i][0] != 'e':
		i=i+1
	Graves[colour][i] = (takenPiece,Graves[colour][i][1])
	graveSite = Graves[colour][i][1]
	nmap[endPos]=0
	takePath = pathfinding.astar(nmap,graveSite,endPos)
	takePath.append(graveSite)
	takePath = cut(takePath, 0)
	takePath = cut(takePath, 1)
	takePath = cutDiag(takePath)
	nmap[graveSite] = 1
	return takePath


################################################################################
#    Primary Movement 
################################################################################
def move(board1,board2,startPos,endPos,piece,colour): # The move function generates a path for the piece to move along
	
	################ Move interpretation ################
	startPos = (9-int(startPos[1]),ord(startPos[0])-95)
	endPos = (9-int(endPos[1]),ord(endPos[0])-95)
	dist = numpy.subtract(endPos,startPos)
	dVec = []
	dVec.append(-1 if dist[0]<0 else (0 if dist[0]==0 else 1))
	dVec.append(-1 if dist[1]<0 else (0 if dist[1]==0 else 1))
	global path
	global nmap
	global stopPos
	shiftBack = (0,0)
	path = []

	print startPos, endPos, dist, dVec, piece, colour

	################  Board Defanition  ################
	board1 = board1.split(' ', 1)[0] 								# Converts fen board to pathable matrix
	board2 = board2.split(' ', 1)[0]
	def r(o):return('0,'*11+'0\n0,0,'+''.join(['0,'*int(h)if h.isdigit()else'0,0\n0,0,'if h=='/' else h for h in o])+'0,0\n0'+',0'*11) # Converts fen to a map
	nmap = r(board1)
	nmap = re.sub('([A-z]{1})', '1,', nmap)
	nmap = numpy.array([[int(j) for j in i.split(',')] for i in nmap.splitlines()]) # Converts map string to an array of integers
	# print nmap, '\n'

	################    Fill Graves     ################
	for grave in Graves['White']:
		nmap[grave[1]] = 1 if grave[0] != 'e' else 0
	for grave in Graves['Black']:
		nmap[grave[1]] = 1 if grave[0] != 'e' else 0

	################      Movement      ################
	if nmap[endPos] == 1:
		print 'Take!'
		takenPiece = checkPieceTaken(board1,board2)
		takePath = takePiece(nmap,endPos,takenPiece,colour)
		path.append(takePath)

	if piece == 'k' or piece == 'K' and abs(dist[1])>1: 			# Castling
		x = 2 if dist[1] == -2 else 9
		print colour + ' castle!'
		path.append([startPos,endPos])
		nmap[startPos],nmap[endPos]=0,1
		nmap[(endPos[0],x)],nmap[(endPos[0],(startPos[1]+endPos[1])/2)] = 0,2
		rookPath = pathfinding.astar(nmap,(endPos[0],(startPos[1]+endPos[1])/2),(endPos[0],x))
		rookPath.append((endPos[0],(startPos[1]+endPos[1])/2))
		path.append(rookPath)
	else:
		if piece == 'n' or piece == 'N':
			print 'Knight move!'
			nmap[startPos]=0
			shiftBack = knightMove(nmap,startPos,endPos,dist,dVec)
		else:
			print 'Standard move!'
			path.append([startPos,endPos])

	nmap[startPos],nmap[endPos]=0,1
			

	print path,'\n',nmap,'\n', 'end of move', '\n'
	serial.splitMove(path)


#testing call of function
move('r3k2r/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1','5kr1/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1', 'e1', 'g1','K','White') # Castle test
# move('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1','rnbqkbnr/pppppppp/8/8/8/5N2/PPPPPPPP/RNBQKB1R w KQkq - 0 1', 'g8', 'f6','N','White')


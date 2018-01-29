import numpy
import re
import Chess_Pathfinding as pathfinding
# import Chess_Serial as serial
from time import sleep
# import Chess_Movement as move
# import Chess_Pathfinding as pathfinding

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
	if board[-1] != '0':
		board+=','
	board = numpy.array([[str(j) for j in i.split(',')] for i in board.splitlines()]) # Converts map string to an array of integers
	board = board[:,:-1]
	# print board

	for grave in Graves['White']:
		nmap[grave[1]] = 1 if grave[0] != 'e' else 0
	for grave in Graves['Black']:
		nmap[grave[1]] = 1 if grave[0] != 'e' else 0

	# print nmap

	################################################################################
	#    Reseting Pieces on board  
	################################################################################
	atHome = {'p':0,'r':0,'n':0,'b':0,'P':0,'R':0,'N':0,'B':0}
	home =(0,0)
	whiteHomes = {
	'P': [(0,(7,2)),(0,(7,3)),(0,(7,4)),(0,(7,5)),(0,(7,6)),(0,(7,7)),(0,(7,8)),(0,(7,9))],
	'R': [(0,(8,2)),(0,(8,9))],
	'N': [(0,(8,3)),(0,(8,7))],
	'B': [(0,(8,4)),(0,(8,6))],
	'Q': [(0,(8,5))],
	'K': [(0,(8,6))]
	}
	blackHomes = {
	'p': [(0,(2,2)),(0,(2,3)),(0,(2,4)),(0,(2,5)),(0,(2,6)),(0,(2,7)),(0,(2,8)),(0,(2,9))],
	'r': [(0,(1,2)),(0,(1,9))],
	'n': [(0,(1,3)),(0,(1,7))],
	'b': [(0,(1,4)),(0,(1,6))],
	'q': [(0,(1,5))],
	'k': [(0,(1,6))]
	}

	# def houseCall():
	i=0
	for rank in board:
		i+=1 
		j=1
		# print rank
		for char in rank:
			j+=1
			path = []
			# print char
			if char in ['p','r','n','b','k','q']:
				for house in blackHomes[char]:
					if (i,j)==house[1]:
						# blackHomes[char][] = (takenPiece,blackHomes[char][i][1])
						print(house)
						house=(1,house[1])
						print(house)
					else:
						pass
			elif char in ['P','R','N','B','K','Q']:
				for house in whiteHomes[char]:
					if (i,j)==house[1]:
						house=(1,house[1])
					else:
						pass
	print(whiteHomes)
	print(blackHomes)

			
	# sleep(60)
	# # print '\n All pieces removed!\n'
	# for grave in reversed(Graves['Black']):
	# 	piece, position = grave[0], grave[1]
	# 	# if piece == 'e':
	# 	# 	continue
	# 	# print piece,position

	# 	if piece == 'P':
	# 		home = (7,2+atHome[piece])
	# 		atHome[piece]+=1
	# 	elif piece == 'R':
	# 		home = (8,2+7*atHome[piece])
	# 		atHome[piece]+=1
	# 	elif piece == 'N':
	# 		home = (8,3+5*atHome[piece])
	# 		atHome[piece]+=1
	# 	elif piece == 'B':
	# 		home = (8,4+3*atHome[piece])
	# 		atHome[piece]+=1
	# 	elif piece == 'Q':
	# 		home = (8,5)
	# 	elif piece == 'K':
	# 		home = (8,6)

	# 	# print home
	# 	path = []
	# 	nmap[position]=0
	# 	returnPath = pathfinding.astar(nmap,home,position)
	# 	nmap[home]=1
	# 	returnPath.append(home)
	# 	returnPath = cut(returnPath, 0)
	# 	returnPath = cut(returnPath, 1)
	# 	returnPath = cutDiag(returnPath)
	# 	path.append(returnPath)
	# 	# print path
	# 	serial.splitMove(path)
	# 	sleep(15)
	# 	# print nmap
        
	# path = [[(7,2),(7.5,2.5)]]
	# sleep(60)
	# serial.splitMove(path)
	# nmap[(7,2)] = 0


	# for grave in reversed(Graves['White']):
	# 	piece, position = grave[0], grave[1]
	# 	# if piece == 'e':
	# 	# 	continue
	# 	# print piece,position

	# 	if piece == 'p':
	# 		home = (2,2+atHome[piece])
	# 		atHome[piece]+=1
	# 	elif piece == 'r':
	# 		home = (1,2+7*atHome[piece])
	# 		atHome[piece]+=1
	# 	elif piece == 'n':
	# 		home = (1,3+5*atHome[piece])
	# 		atHome[piece]+=1
	# 	elif piece == 'b':
	# 		home = (1,4+3*atHome[piece])
	# 		atHome[piece]+=1
	# 	elif piece == 'q':
	# 		home = (1,5)
	# 	elif piece == 'k':
	# 		home = (1,6)

	# 	# print home
	# 	path = []
	# 	nmap[position]=0
	# 	returnPath = pathfinding.astar(nmap,home,position)
	# 	nmap[home]=1  
	# 	returnPath.append(home)
	# 	returnPath = cut(returnPath, 0)
	# 	returnPath = cut(returnPath, 1)
	# 	returnPath = cutDiag(returnPath)
	# 	path.append(returnPath)
	# 	# print(path)
	# 	serial.splitMove(path)
	# 	sleep(15)
	# 	# print nmap

	# path = [[(7.5,2.5),(7,2)]]
	# serial.splitMove(path)
	# nmap[(7,2)] = 1

	# print nmap
	# print '\n done!'


# Graves = {
# 	'Black': [('p',(1,0)),('p',(2,0)),('p',(3,0)),('p',(4,0)),('n',(5,0)),('r',(6,0)),('q',(7,0)),('e',(8,0)),('e',(1,1)),('e',(2,1)),('e',(3,1)),('e',(4,1)),('e',(5,1)),('e',(6,1)),('e',(7,1)),('e',(8,1))],
# 	'White': [('P',(8,11)),('P',(7,11)),('P',(6,11)),('P',(5,11)),('P',(4,11)),('P',(3,11)),('N',(2,11)),('N',(1,11)),('R',(8,10)),('B',(7,10)),('R',(6,10)),('Q',(5,10)),('e',(4,10)),('e',(3,10)),('e',(2,10)),('e',(1,10))]
# 	} # Note White peices are interred in the 'Black' Graves


# resetBoard('r1bk4/1pp5/p3b3/3p4/8/1P1n3B/6P1/2K5 w KQkq - 0 1',Graves)

Graves = {
	'Black': [('e',(1,0)),('e',(2,0)),('e',(3,0)),('e',(4,0)),('e',(5,0)),('e',(6,0)),('e',(7,0)),('e',(8,0)),('e',(1,1)),('e',(2,1)),('e',(3,1)),('e',(4,1)),('e',(5,1)),('e',(6,1)),('e',(7,1)),('e',(8,1))],
	'White': [('e',(8,11)),('e',(7,11)),('e',(6,11)),('e',(5,11)),('e',(4,11)),('e',(3,11)),('e',(2,11)),('e',(1,11)),('e',(8,10)),('e',(7,10)),('e',(6,10)),('e',(5,10)),('e',(4,10)),('e',(3,10)),('e',(2,10)),('e',(1,10))]
	}

resetBoard('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1',Graves)
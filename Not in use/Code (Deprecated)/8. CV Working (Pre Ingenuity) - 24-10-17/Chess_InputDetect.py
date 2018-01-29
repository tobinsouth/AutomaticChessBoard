import numpy 
import re
import Computer_Vision as cv

def detectMove(board,arena):
##	[a, b, c, d] = arena
##	image = cv.openCV(a, b, c, d)
	board = board.split(' ', 1)[0] 								# Converts fen board to pathable matrix
	def r(o):return(''.join(['0'*int(h)if h.isdigit()else'\n' if h=='/' else h for h in o])) # Converts fen to a map
	board = r(board)
	board = re.sub('([a-z]{1})', '0', board)
	board = re.sub('([A-Z]{1})', '1', board)
	board = numpy.array([list(i) for i in board.splitlines()])
	board = numpy.array([[int(x) for x in i] for i in board])
	change = board-image
	print board
	print image
	print change
	nonzero = numpy.nonzero(change)
	# print nonzero[1][0]
	if len(nonzero[1]) > 2:
		startSquare = 'e1'
		if nonzero[1][0] == 4:
			endSquare = 'g1'
		else :
			endSquare = 'b1'
	else :
		start = numpy.argmax(change)
		start = [start/8,start%8]
		startSquare = str(unichr(start[1]+97))+str(7-start[0]+1)
		# print 'Start position: ', start, ' ', startSquare
		end = numpy.argmin(change)
		end = [end/8,end%8]
		endSquare = str(unichr(end[1]+97))+str(7-end[0]+1)
		# print 'End position: ', end, ' ', endSquare
	move = startSquare + endSquare
	return move


image = numpy.array([[0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 1, 1, 0]],np.uint8)


# # move = detectMove('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKB1R w KQkq - 0 1', image)
move = detectMove('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/R3K2R w KQkq - 0 1', image)
print move

# array =

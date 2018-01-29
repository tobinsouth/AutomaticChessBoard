import numpy
import re

def checkPieceTaken(board1,board2):
	board1 = re.sub('\W+', '', board1)
	board2 = re.sub('\W+', '', board2)
	board1 = re.sub('\d+', '', board1)
	board2 = re.sub('\d+', '', board2)

	def convert_to_ascii(text):
	    return (ord(char) for char in text)

	piece = chr(sum(convert_to_ascii(board1))-sum(convert_to_ascii(board2)))
	return piece

# checkPieceTaken('8/8/8/8/5Rqr/pppk4/5K2/8 b - - 0 1','8/8/8/8/5Rqr/pppk4/5K2/8 b - - 0 1')

def checkPieceReset(char,atHome):
	if char == 'p':
		home = (2,2+atHome[char])
		atHome[char]+=1
	elif char == 'P':
		home = (7,2+atHome[char])
		atHome[char]+=1
	elif char == 'r':
		home = (1,2+atHome[char])
		atHome[char]+=7
	elif char == 'R':
		home = (8,2+atHome[char])
		atHome[char]+=7
	elif char == 'n':
		home = (1,3+atHome[char])
		atHome[char]+=5
	elif char == 'N':
		home = (8,3+atHome[char])
		atHome[char]+=5
	elif char == 'b':
		home = (1,4+atHome[char])
		atHome[char]+=3
	elif char == 'B':
		home = (8,4+atHome[char])
		atHome[char]+=3
	elif char == 'k':
		home = (1,6)
	elif char == 'K':
		home = (8,5)
	elif char == 'q':
		home = (1,5)
	elif char == 'Q':
		home = (8,6)
	return home
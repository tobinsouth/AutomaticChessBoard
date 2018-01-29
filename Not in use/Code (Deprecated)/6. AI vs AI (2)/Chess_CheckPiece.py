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
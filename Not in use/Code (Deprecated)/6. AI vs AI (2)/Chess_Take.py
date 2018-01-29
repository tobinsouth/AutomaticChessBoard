import numpy
import Chess_Pathfinding as pathfinding
import Chess_CheckPiece as checker
import Chess_Serial as serial
import Chess_Knight as knight
import Chess_Movement as movement

def takePiece(startPos,endPos,piece,takenPiece,colour):
	print 'Take!'

	num = len(movement.Graves[colour])

	if colour=='White' and num<=7: # Determines gravessite
		grave = (num+1,0)
	elif colour=='White' and num>7:
		grave = (num-7,1)
	elif colour=='Black' and num<=7:
		grave = (8-num,11)
	else:
		grave = (16-num,10)

	movement.Graves[colour].append([takenPiece,grave])
	print movement.Graves[colour]

	if piece == 'n' or piece == 'N' :
		knightTake(startPos,endPos)



	pass
	# return takePath # Returns path to the move function
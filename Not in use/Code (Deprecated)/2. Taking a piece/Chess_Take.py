import numpy
import Chess_Pathfinding as pathfinding
import Chess_CheckPiece as checker
import Chess_Serial as serial

def take(nmap,startPos,wgraves,bgraves,board1,board2):
	print 'Take!'

	wnum = len(wgraves)-1
	bnum = len(bgraves)-1

	piece = checker.checkPieceTaken(board1,board2)

	if piece in ['p','r','n','b','k','q']:
		color = 1		
	else:
		color = 0

	if color==0 and wnum<=7: # Determines gravessite
		end = (wnum+1,0)
	elif color==0 and wnum>7:
		end = (wnum-7,1)
	elif color==1 and bnum<=7:
		end = (8-bnum,11)
	else:
		end = (16-bnum,10)

	if color==0:
		wgraves = wgraves.append((end[0],end[1], piece))
	else:
		bgraves = bgraves.append((end[0],end[1], piece))

	path = pathfinding.astar(nmap, end, startPos) # Pathfinding
	path.append(end)
	print end

	return path # Returns path to the move function
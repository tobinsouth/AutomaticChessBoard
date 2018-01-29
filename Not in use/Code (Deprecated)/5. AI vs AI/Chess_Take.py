import numpy
import Chess_Pathfinding as pathfinding
import Chess_CheckPiece as checker
import Chess_Serial as serial
import Chess_Knight as knight

def take(nmap,endPos,startPos,dist,wgraves,bgraves,piece,k):
	print 'Take!'

	wnum = len(wgraves)-1
	bnum = len(bgraves)-1

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


	if k!=0:
		nmap[k]=1
		takePath = pathfinding.astar(nmap, end, endPos)
		takePath.append(end)
	else:
		dVec = []
		for i in range(0,2):
			dVec.append(dist[i]/abs(dist[i]))

		path = (startPos,numpy.subtract(endPos,dVec),endPos)
		
		serial.makeMove([path[0],path[1]])
		nmap[path[1]]=1

		takePath = pathfinding.astar(nmap, end, endPos) # Pathfinding
		takePath.append(end)

		serial.makeMove(takePath[0])
		serial.makeMove(takePath[1])

		del takePath[0]
		del takePath[1]

		serial.makeMove(path[2])

	nmap[takePath[-1]]=1
	return takePath # Returns path to the move function
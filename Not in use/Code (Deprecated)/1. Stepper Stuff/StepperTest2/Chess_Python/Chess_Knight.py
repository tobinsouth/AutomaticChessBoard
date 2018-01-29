import numpy
import Chess_Pathfinding as pathfinding

def knightMove(nmap,startPos,endPos,dist):
	#dist = numpy.subtract(endPos,startPos)
	direction1 = -1 if dist[0]<0 else 1
	direction2 = -1 if dist[1]<0 else 1
	#print dist[0], direction1, direction2,'\n'
	path=[]
	for i in range(0,dist[0],direction1):
		nextPlace=numpy.add(startPos,(i,0))
		nextPlace=(nextPlace[0],nextPlace[1])
		path.append(nextPlace)
		#print nextPlace
		if nmap[nextPlace]==1:
			shift=(nextPlace,(nextPlace[0]+float(direction1)/2,nextPlace[1]-float(direction2)/2))
			# serial(shift)
			#print shift 
		else:
			continue
	if abs(dist[1])>1:
		nextPlace=numpy.add(startPos,(direction1,direction2))
		nextPlace=(nextPlace[0],nextPlace[1])
		path.append(nextPlace)
		path.append(endPos)
		#print nextPlace
		if nmap[nextPlace]==1:
			shift=(nextPlace,(nextPlace[0]+float(direction1)/2,nextPlace[1]-float(direction2)/2))
			# serial(shift)
			#print shift
	else:
		path.append(endPos)
	return path
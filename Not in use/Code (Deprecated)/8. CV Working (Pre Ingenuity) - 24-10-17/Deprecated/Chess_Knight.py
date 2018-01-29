import numpy
import Chess_Movement as movement

def knightMove(nmap,startPos,endPos,dist,dVec): 
	path = movement.path
	knightPath = []
	shiftBack=[(0,0)]
	for i in range(0,dist[0],dVec[0]):
		nextpos=numpy.add(startPos,(i,0))
		nextpos=(nextpos[0],nextpos[1])
		if nmap[nextpos]!=0:
			shift=[nextpos,(nextpos[0]+float(dVec[0])/2,nextpos[1]-float(dVec[1])/2)]
			shiftBack=[shift[1],shift[0]]
			path.append(shift)
		knightPath.append(nextpos)
	if abs(dist[1])>1:
		nextpos=numpy.add(startPos,(dVec[0],dVec[1]))
		nextpos=(nextpos[0],nextpos[1])
		knightPath.append(nextpos)
		if nmap[nextpos]!=0:
			shift=[nextpos,(nextpos[0]+float(dVec[0])/2,nextpos[1]-float(dVec[1])/2)]
			shiftBack=[shift[1],shift[0]]
			path.append(shift)
	knightPath.append(endPos)
	path.append(knightPath)
	return shiftBack
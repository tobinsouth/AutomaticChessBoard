import numpy

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
	return path

#############################################################
path = [(0,0),(0,1),(0,2),(0,3),(0,4),(1,4),(0,4),(1,4),(2,4),(2,5),(2,6),(2,7),(3,6),(4,5),(5,4),(6,3),(6,4)]

print len(path), path
path = cut(path, 0)
print len(path), path
path = cut(path, 1)
print len(path), path
path = cutDiag(path)
print len(path), path
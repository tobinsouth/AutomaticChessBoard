import numpy

dist = (-5,0)
dVec = []
dVec.append(-1 if dist[0]<0 else (0 if dist[0]==0 else 1))
dVec.append(-1 if dist[1]<0 else (0 if dist[1]==0 else 1))

dVec = [x * 2 for x in dVec]
print numpy.add(dist,dVec)

print dist, dVec
# Author: Christian Careaga (christian.careaga7@gmail.com)
# A* Pathfinding in Python (2.7)
# Please give credit if used

import numpy
from heapq import *

##################################################################################
#    A* pathfinding algorithm 
##################################################################################
def heuristic(a, b):
    return (b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2

def astar(array, start, goal):

    neighbors = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]

    close_set = set()
    came_from = {}
    gscore = {start:0}
    fscore = {start:heuristic(start, goal)}
    oheap = []

    heappush(oheap, (fscore[start], start))
    
    while oheap:

        current = heappop(oheap)[1]

        if current == goal:
            data = []
            while current in came_from:
                data.append(current)
                current = came_from[current]
            return data

        close_set.add(current)
        for i, j in neighbors:
            neighbor = current[0] + i, current[1] + j            
            tentative_g_score = gscore[current] + heuristic(current, neighbor)
            if 0 <= neighbor[0] < array.shape[0]:
                if 0 <= neighbor[1] < array.shape[1]:                
                    if array[neighbor[0]][neighbor[1]] == 1:
                        continue
                else:
                    # array bound y walls
                    continue
            else:
                # array bound x walls
                continue
                
            if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):
                continue
                
            if  tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1]for i in oheap]:
                came_from[neighbor] = current
                gscore[neighbor] = tentative_g_score
                fscore[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heappush(oheap, (fscore[neighbor], neighbor))
                
    return False

##################################################################################
#    Movement System 
##################################################################################


#     Board layout and coordinate system
#	   Cordinates are [rank,column]
#
#      *,*,A,B,C,D,E,F,G,H,*,*
#      0,1,2,3,4,5,6,7,8,9,0,1
#     [0,0,0,0,0,0,0,0,0,0,0,0] 0*
#     [0,0,0,0,0,0,0,0,0,0,0,0] 1
#     [0,0,0,0,0,0,0,0,0,0,0,0] 2
#     [0,0,0,0,0,0,0,0,0,0,0,0] 3
#     [0,0,0,0,0,0,0,0,0,0,0,0] 4
#     [0,0,0,0,0,0,0,0,0,0,0,0] 5
#     [0,0,0,0,0,0,0,0,0,0,0,0] 6
#     [0,0,0,0,0,0,0,0,0,0,0,0] 7
#     [0,0,0,0,0,0,0,0,0,0,0,0] 8
#     [0,0,0,0,0,0,0,0,0,0,0,0] 9*

def take(nmap,startPos,grave):
    print 'Take!'
    if grave[0]==0 and grave[1]<=8: # Determines gravesite
        end = (grave[1],0)
    elif grave[0]==0 and grave[1]>8:
        end = (grave[1]-8,1)
    elif grave[0]==1 and grave[1]<=8:
        end = (9-grave[1],11)
    else:
        end = (17-grave[1],10)

    path = astar(nmap, end, startPos) # Pathfinding
    path.append(end)

    return path # Returns path to the move function


def move(board,startPos,endPos,peice): # The move function generates a path for the peice to move along
    
    # Starting and ending positions
    startPos = (int(startPos[1]),ord(startPos[0])-95)
    endPos = (int(endPos[1]),ord(endPos[0])-95)
    print startPos, endPos

    # Board defanition
    nmap = board.split(' ', 1)[0] # Removes unneccesary fen
    print nmap
    def r(o):return('0,'*11+'0\n0,0,'+''.join(['0,'*int(h)if h.isdigit()else'0,0\n0,0,'if h=='/'else '1,' for h in o])+'0,0\n0'+',0'*11) # Converts fen to a map
    nmap = r(nmap)
    nmap = numpy.array([[int(j) for j in i.split(',')] for i in nmap.splitlines()]) # Converts map string to an array of integers
    print nmap
    print '\n'

    grave = (0,1)

    if nmap[endPos]==1:
    	nmap[endPos]=0
    	path = take(nmap,endPos,grave)
        # serial(path)

    if peice=='k' and abs(endPos[1]-startPos[1])>1:
    	if (endPos[1]-startPos[1])>1:
    		print 'White king castle!'
    		path = (startPos,endPos)
    		# serial(path)
    		nmap[startPos]=0
    		nmap[endPos]=1
    		path = ((1,7), (0,8), (1,9))
    		nmap[(1,9)]=0
    		nmap[(1,7)]=1
    	else:
    		print 'White queen castle!'
    		path = (startPos,endPos)
    		# serial(path)
    		nmap[startPos]=0
    		nmap[endPos]=1
    		path = ((1,2), (0,3), (0,4), (1,5))
    		nmap[(1,5)]=0
    		nmap[(1,2)]=1
    elif peice=='K' and abs(endPos[1]-startPos[1])>1:
    	if (endPos[1]-startPos[1])<-1:
    		print 'Black king castle!'
    		path = (startPos,endPos)
    		# serial(path)
    		nmap[startPos]=0
    		nmap[endPos]=1
    		path = ((8,2), (9,3), (8,4))
    		nmap[(8,2)]=0
    		nmap[(8,4)]=1
    	else:
    		print 'Black queen castle!'
    		path = (startPos,endPos)
    		# serial(path)
    		nmap[startPos]=0
    		nmap[endPos]=1
    		path = ((8,9), (9,8), (9,7), (8,6))
    		nmap[(8,9)]=0
    		nmap[(8,6)]=1
    elif peice=='n' or 'N':
    	print 'Night move!'
    	path = ()
    	nmap[startPos]=0
    	nmap[endPos]=1
    else:
    	print 'Standard move!'
    	path = (startPos,endPos)
    	nmap[startPos]=0
    	nmap[endPos]=1

    print path
    #for x in path:
    #    nmap[x]=5
    #serial(path)  
    print nmap
    print '\n'



move('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBKQBNR b KQkq - 1 2', 'b8', 'c6','N')

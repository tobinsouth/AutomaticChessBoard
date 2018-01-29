# Author: Christian Careaga (christian.careaga7@gmail.com)
# A* Pathfinding in Python (2.7)
# Please give credit if used

import numpy
from heapq import *


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

###########################################################################



# nmap = numpy.array([
#     #*,*,A,B,C,D,E,F,G,H,*,*
#     #0,1,2,3,4,5,6,7,8,9,0,1
#     [0,0,0,0,0,0,0,0,0,0,0,0], #0*
#     [0,0,0,0,0,0,0,0,0,0,0,0], #1
#     [0,0,0,0,0,0,0,0,0,0,0,0], #2
#     [0,0,0,0,0,0,0,0,0,0,0,0], #3
#     [0,0,0,0,0,0,0,0,0,0,0,0], #4
#     [0,0,0,0,0,0,0,0,0,0,0,0], #5
#     [0,0,0,0,0,0,0,0,0,0,0,0], #6
#     [0,0,0,0,0,0,0,0,0,0,0,0], #7
#     [0,0,0,0,0,0,0,0,0,0,0,0], #8
#     [0,0,0,0,0,0,0,0,0,0,0,0]])#9*


def kill(board,start,grave): # The kill function (board is the fen, start is the initial position of the peice, and grave determines where it will be layed to rest)

    board = board.split(' ', 1)[0] # Removes unneccesary fen
    print board

    start = list(start)
    start = (ord(start[0])-95,int(start[1]))

    print start 

    if grave[0]==0 and grave[1]<=8: # Determines gravesite
        end = (grave[1],0)
    elif grave[0]==0 and grave[1]>8:
        end = (grave[1]-8,1)
    elif grave[0]==1 and grave[1]<=8:
        end = (9-grave[1],11)
    else:
        end = (17-grave[1],10)


    def r(o):return('0,'*11+'0\n0,0,'+''.join(['0,'*int(h)if h.isdigit()else'0,0\n0,0,'if h=='/'else '1,' for h in o])+'0,0\n0'+',0'*11) # Converts fen to a map
    nmap = r(board)

    nmap = numpy.array([[int(j) for j in i.split(',')] for i in nmap.splitlines()]) # Converts map string to an array of integers

    nmap[start] = 2 # Marking start pos
    nmap[end] = 2 # Marking end pos

    print nmap
    print '\n'

    path = astar(nmap, end, start) # Pathfinding

    print path
    print '\n'

    for x in path: # Drawing path
        nmap[x]=5
    print nmap

    return path, end # Returns path and end cooordinates for the arduino


print kill('rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R b KQkq - 1 2', 'c4', (0,1))

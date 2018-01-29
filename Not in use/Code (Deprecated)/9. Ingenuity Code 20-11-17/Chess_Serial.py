from time import sleep

import serial

port = '/dev/cu.usbmodem1411' # For real arduinos on Thomas' Mac
# port = '/dev/cu.usbmodem1421' # For real arduinos on Tobin's Mac
# port = '/dev/cu.usbmodem14321' # For real arduinos on Tobin's New Mac
# port = '/dev/cu.wchusbserial1410' # For cheap arduinos on Thomas' Mac
# port = '/dev/cu.wchusbserial1420' # For cheap arduinos on Tobin's Mac

ser = serial.Serial(port, 9600)

sleep(3)

servoList = []
currentX = 0
currentY = 0
absX = 0
absY = 0
relX = 0
relY = 0
relA = 0
relB = 0
mag = 0



def splitMove(path):
    for move in path:
        writeMove(move)
    return 'Success'

def writeMove(move):
    # print ('make move ' , move)
    makeMove(move)

def toAscii(servoList):
    asciiList = []
    # print (servoList)
    for x in range(0,len(servoList)):
        if servoList[x] <-30 or servoList[x]>30:
            print('WARNING, the carriage is going too far! Relative coordinate set to 0')
            asciiList.append(chr(70))
        else:
            asciiList.append(chr(servoList[x]+70))
    task = asciiList
    # print task, '\n'

    # print (task)
    for char in task:
        ser.write(char.encode())
        # print(char)
    # byte = 'x'
    # counter = 0
    # while counter < 10:
    #     byte = ser.read(size=1)
    #     # print byte
    #     if byte  == 'x':
    #         counter = counter + 1
         

def makeMove(posList):
    global absX
    global absY
    global relX
    global relY
    global relA
    global relB
    global mag
    global currentX
    global currentY
    global ready
    # ready = False

    for i in range(0,len(posList)):
        posList[i] = [x for x in posList[i]]

    x = 0
    
    for coords in posList:
        servoList = []
        relX = 0
        relY = 0
        relA = 0
        relB = 0
        absX = coords[1]
        absY = coords[0]
        relX = absX - currentX
        relY = absY - currentY
        if relX == relY:
            relA = relX
            relX = 0
            relY = 0
        if (relX == -relY):
            relB = -relX
            relX = 0
            relY = 0

        servoList.append(int(2*relX))
        servoList.append(int(2*relY))
        servoList.append(int(2*relA))
        servoList.append(int(2*relB))
        if x==0:
            mag = 1
        if x==len(posList)-1:
            mag = 0
        servoList.append(int(2*mag))

        currentX = absX
        currentY = absY
        x = x + 1
        toAscii(servoList)
    # print posList
    # print servoList
    




# for x in range(1,8):
#     splitMove(moveList)
#     sleep(15)




# moveList = [[(7, 8), (6.5, 8.5)], [(8, 8), (7, 8), (6, 7)], [(6.5, 8.5), (7, 8)], [(0,5), (0,0)]]










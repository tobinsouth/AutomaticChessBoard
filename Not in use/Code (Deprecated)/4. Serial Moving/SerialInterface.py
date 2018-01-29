# pip install pySerial
from time import sleep
import serial
# ser = serial.Serial('/dev/cu.usbmodem1411', 9600)
# # print ser
# sleep(4)

# data = str('0,0,0,20,0')
# ser.write(data)

# sleep(2)
# print "hi"
# while True:
#     print ser.readline()
#     if ser.readline() != "":
#         break
# status = "yes"

# waiting = True
# while waiting:
#         status = str(ser.readline())
#         if status == "Done":
#             waiting = False

# for x in xrange(1,10):
#     print x*3

currentX = 0
currentY = 0
absX = 0
absY = 0
relX = 0
relY = 0
relA = 0
relB = 0

arr = [[2,2],[3,4],[4,0],[5,1],[6,0]]




def runMove(data):
    ser = serial.Serial('/dev/cu.usbmodem1411', 9600)
    sleep(2)
    global ready
    ser.write(data)

    # while True:
    #     line = ser.readline()
    #     # print type(line)
    #     # print s
    #     # print line
    #     if line == '6':
    #         # print 'asdas'
    #         # var = False
    #         break

    ready = True




def sendSerial(posList):
    
    # ser.open()
    global absX
    global absY
    global relX
    global relY
    global relA
    global relB
    global currentX
    global currentY
    global ready
    ready = False
    

    for i in range(0,len(posList)):
        mag = 0
        relX = 0
        relY = 0
        relA = 0
        relB = 0
        absX = posList[i][0]
        absY = posList[i][1]
        relX = absX - currentX
        relY = absY - currentY
        if relX == relY:
            relA = relX
            relX = 0
            relY = 0
        elif (relX == -relY):
            relB = -relX
            relX = 0
            relY = 0

        print "Coord",i+1
        print relX
        print relY
        print relA
        print relB

        move = str(str(relX)+','+str(relY)+','+str(relA)+','+str(relB)+','+str(mag))
        print move

        runMove(move)

        while ready == False:
            print "Waiting"





sendSerial(arr)
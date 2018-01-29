import serial
from time import sleep
ser = serial.Serial('/dev/cu.usbmodem1411', 9600, timeout = 1)
sleep(2)

# data = str('0,0,0,2,0')
# ser.write(data)



# var = True

# while True:
#     line = ser.readline()
#     # print type(line)
#     # print s
#     # print line
#     if line == '6':
#     	# print 'asdas'
#     	# var = False
#     	break

# print "Done"

def runMove(data):
	ser.write(data)

	while True:
	    line = ser.readline()
	    # print type(line)
	    # print s
	    # print line
	    if line == '6':
	    	# print 'asdas'
	    	# var = False
	    	break

   	return True


print runMove("0,0,2,0,0")
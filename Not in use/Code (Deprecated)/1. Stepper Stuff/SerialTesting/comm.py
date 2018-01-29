
import serial
from random import randint
import time


# port = '/dev/cu.usbmodem1411'
port = '/dev/cu.wchusbserial1410'

ser = serial.Serial(port, 9600)




incoming = 12

while True:
	# waitting = 1
	# while waitting:
	# 	try:
	# 		incoming = int(ser.readline())
	# 		break
	# 	except ValueError:
	# 		print("no data yet, just wait")
	# 		waitting = 0
	for x in xrange(1,2):
		try:
			incoming = int(ser.readline())
			break
		except ValueError:
			print("no data yet, just wait")
			waitting = 0

	print incoming
	if incoming % 5 == 0:
		print "div by 5"








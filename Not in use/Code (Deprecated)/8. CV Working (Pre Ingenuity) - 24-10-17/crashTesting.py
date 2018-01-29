import Computer_Vision as cv
from time import sleep

[x, y, w, h] = cv.setup()

for x in xrange(1,10):
	sleep(40)
	Out = cv.openCV(x, y, w, h)
	print Out

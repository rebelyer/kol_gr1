import random
import time

current_angle = 0.0

def correction(angle):
	if(angle > 7):
		return -7
	elif(angle < -7):
		return 7
	else:
		return -angle	

while(1):
	print 'Current angle: '
	print current_angle
	print 'Applied correction: '
	print correction(current_angle)
	print '\n'

	current_angle += correction(current_angle)
	current_angle += random.gauss(0,5)

	time.sleep(1)

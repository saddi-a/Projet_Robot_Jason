
from Motor import Motor
import time    # Import necessary modules



if __name__ == '__main__':
	m=Motor()
	m.setSpeed(50)
	m.forward()
	time.sleep(3)
	m.backward()
	time.sleep(3)
	# m.stop()
	# time.sleep(3)
	# m.turn_left()
	# time.sleep(3)
	# m.turn_right()
	# time.sleep(3)
	# m.turn_center()
	# m.stop()



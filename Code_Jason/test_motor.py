
from Motor import Motor
import time    # Import necessary modules



if __name__ == '__main__':
	m=Motor()
	m.setSpeed(50)
	time.sleep(2)
	m.forward()
	time.sleep(2)
	m.backward()
	time.sleep(2)
	m.stop()
	time.sleep(2)
	m.turn_left()
	time.sleep(2)
	m.turn_right()
	time.sleep(2)
	m.turn_center()
	m.stop()



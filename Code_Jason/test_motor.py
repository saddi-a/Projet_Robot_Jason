
from Motor import Motor
import time    # Import necessary modules



if __name__ == '__main__':
	m=Motor()
	m.setSpeed(50)
	m.forward()
	time.sleep(2)
	m.backward()
	time.sleep(2)
	m.stop()
	m.turn_left()
	time.sleep(2)
	m.turn_right()
	time.sleep(2)
	m.turn_center()
	time.sleep(2)
	m.setSpeed(50)
	m.turn_right()
	m.forward()
	time.sleep(1)
	m.stop()



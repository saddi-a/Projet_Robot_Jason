
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
	m.turnLeft()
	time.sleep(2)
	m.turnRight()
	time.sleep(2)
	m.turnCenter()
	time.sleep(2)
	m.setSpeed(50)
	m.turnRight()
	m.forward()
	time.sleep(2)
	m.stop()



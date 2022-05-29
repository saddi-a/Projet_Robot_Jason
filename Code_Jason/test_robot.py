from Robot import Robot
import time    # Import necessary modules



if __name__ == '__main__':
	robot=Robot()
	for i in range(200) :
		robot.readSensors()
		robot.move()
		print(i)
	
	robot.clean()
from Robot import Robot



if __name__ == '__main__':
	robot=Robot()
	for i in range(200) :
		robot.readSensors()
		robot.move()
		print(i)
	
	robot.clean()
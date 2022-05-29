
import RPi.GPIO as GPIO
import PCA9685 as p




class Motor:

	def __init__(self):
		# # ===========================================================================
		# # Raspberry Pi pin11, 12, 13 and 15 to realize the clockwise/counterclockwise
		# # rotation and forward and backward movements
		# # ===========================================================================
		self.Motor0_A = 11  # pin11
		self.Motor0_B = 12  # pin12
		self.Motor1_A = 13  # pin13
		self.Motor1_B = 15  # pin15

		# # ===========================================================================
		# # Set channel 4 and 5 of the servo driver IC to generate PWM, thus 
		# # controlling the speed of the car
		# # ===========================================================================
		self.EN_M0    = 4  # servo driver IC CH4
		self.EN_M1    = 5  # servo driver IC CH5
		self.stearingChanel = 0 # servo driver IC CH0

		self.pins = [self.Motor0_A, self.Motor0_B, self.Motor1_A, self.Motor1_B]

		self.forward0 = 'True'
		self.forward1 = 'True'
		self.backward1 = 'False'
		self.backward0 = 'False'
		self.speed = 25
		self.pwm = p.PWM()                  # Initialize the servo controller.

		self.rightStearing=500
		self.leftStearing=320
		self.centertStearing=410
		
		self.setup()




	# ===========================================================================
	# Adjust the duty cycle of the square waves output from channel 4 and 5 of
	# the servo driver IC, so as to control the speed of the car.
	# ===========================================================================
	def setSpeed(self,speed):
		self.speed = speed*45
		print('speed is: ', self.speed)
		self.pwm.write(self.EN_M0, 0, self.speed)
		self.pwm.write(self.EN_M1, 0, self.speed)

	def setup(self):

		GPIO.setwarnings(False)
		GPIO.setmode(GPIO.BOARD)        # Number GPIOs by its physical location
		self.pwm.frequency = 60
		for pin in self.pins:
			GPIO.setup(pin, GPIO.OUT)   # Set all pins' mode as output
		self.turnCenter()

	# ===========================================================================
	# Control the DC motor to make it rotate clockwise, so the car will 
	# move forward.
	# ===========================================================================

	def motor0(self):
		if self.forward0 == 'True':
			GPIO.output(self.Motor0_A, GPIO.HIGH)
			GPIO.output(self.Motor0_B, GPIO.LOW)
		elif self.forward0 == 'False':
			GPIO.output(self.Motor0_A, GPIO.LOW)
			GPIO.output(self.Motor0_B, GPIO.HIGH)
		else:
			print('Config Error')

	def motor1(self):
		if self.forward1 == 'True':
			GPIO.output(self.Motor1_A, GPIO.HIGH)
			GPIO.output(self.Motor1_B, GPIO.LOW)
		elif self.forward1 == 'False':
			GPIO.output(self.Motor1_A, GPIO.LOW)
			GPIO.output(self.Motor1_B, GPIO.HIGH)

	def forward(self):
		self.forward0 = 'True'
		self.forward1 = 'True'
		self.backward1 = 'False'
		self.backward0 = 'False'
		self.motor0()
		self.motor1()

	def backward(self):
		self.forward0 = 'False'
		self.forward1 = 'False'
		self.backward1 = 'True'
		self.backward0 = 'True'
		self.motor0()
		self.motor1()

	def stop(self):
		self.setSpeed(0)
		self.turnCenter()

	def turnRight(self):
		self.pwm.write(self.stearingChanel, 0, self.rightStearing)

	def turnLeft(self):
		self.pwm.write(self.stearingChanel, 0, self.leftStearing)
		
	def turnCenter(self):
		self.pwm.write(self.stearingChanel, 0, self.centertStearing)

	# # ===========================================================================
	# # The first parameter(status) is to control the state of the car, to make it 
	# # stop or run. The parameter(direction) is to control the car's direction 
	# # (move forward or backward).
	# # ===========================================================================
	# def ctrl(self,status, direction=1):
	# 	if status == 1:   # Run
	# 		if direction == 1:     # Forward
	# 			forward()
	# 		elif direction == -1:  # Backward
	# 			backward()
	# 		else:
	# 			print('Argument error! direction must be 1 or -1.')
	# 	elif status == 0: # Stop
	# 		stop()
	# 	else:
	# 		print('Argument error! status must be 0 or 1.')


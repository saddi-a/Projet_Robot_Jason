from Camera import Camera
from Motor import Motor
from Ultrasonic import Ultrasonic
from Line import Line
import RPi.GPIO as GPIO

class Robot:

    def __init__(self):

        self.motor=Motor()
        self.camera=Camera()
        self.ultrasonic=Ultrasonic()
        self.line=Line()

    
    def readSensors(self):
        self.camera.readLight()
        print("The traficlight color is :",self.camera.trafficlightColor)
        self.ultrasonic.measure()
        print("The distance is:", self.ultrasonic.distance)
        self.line.read()
        print("Right sensor is :",self.line.right)
        print("Left sensor is :",self.line.left)

    def move(self):
        if (self.camera.trafficlightColor=='red' or  self.ultrasonic.distance<10):
            self.motor.stop()
        else:
            self.turn()
            if(self.camera.trafficlightColor=='orange' or  self.ultrasonic.distance<20):
                self.motor.setSpeed(30)
            elif(self.camera.trafficlightColor=='green'):
                self.motor.setSpeed(50)
            else:
                self.motor.setSpeed(40)
            self.motor.forward()

    
    def turn(self):

        if (self.line.right != self.line.right):
            if(self.line.left==1):
                self.motor.turnRight()
                print("turn right")
            elif(self.line.right==1):
                self.motor.turnLeft()
                print("turn left")
        else:
            self.motor.turnCenter()
            print("turn center")
            print(self.line.right==self.line.right)

    def clean(self):
        GPIO.cleanup()
        GPIO.setwarnings(True)
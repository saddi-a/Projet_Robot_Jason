import time
import RPi.GPIO as GPIO
from Camera import Camera
from Motor import Motor
from Ultrasonic import Ultrasonic

class Robot:

    def __init__(self):

        self.motor=Motor()
        self.camera=Camera()
        self.ultrasonic=Ultrasonic()

    
    def readSensors(self):
        self.camera.readLight()
        print("The traficlight color is :",self.camera.trafficlightColor)
        self.ultrasonic.measure()
        print("The distance is:", self.ultrasonic.distance)

    def move(self):

        if (self.camera.trafficlightColor=='red' or  self.ultrasonic.distance<10):
            self.motor.stop()
        elif(self.camera.trafficlightColor=='orange' or  self.ultrasonic.distance<20):
            self.motor.setSpeed(20)
            self.motor.forward()
        elif(self.camera.trafficlightColor=='green'):
            self.motor.setSpeed(50)
            self.motor.forward()
        else:
            self.motor.setSpeed(30)
            self.motor.forward()


    def clean(self):
        GPIO.cleanup()
        GPIO.setwarnings(True)


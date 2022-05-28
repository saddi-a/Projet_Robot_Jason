import RPi.GPIO as GPIO
import time

class Ultrasonic:

    def __init__(self):
        self.trig=23
        self.echo=24
        self.setup()
        self.distance=self.measure()
        #distance in cm
    
    def setup(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.trig,GPIO.OUT)
        GPIO.setup(self.echo,GPIO.IN)
        GPIO.output(self.trig, False)
        
    def measure(self):
        GPIO.output(self.trig, True)
        time.sleep(0.00001)
        GPIO.output(self.trig, False)
        while GPIO.input(self.echo)==0:
            pulse_start = time.time()
        while GPIO.input(self.echo)==1:
            pulse_end = time.time()
        pulse_duration = pulse_end - pulse_start
        self.distance = pulse_duration * 17150
        #Speed of sound = 34300 cm/s 
        #Divided by 2 for the two way travel


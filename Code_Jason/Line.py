import RPi.GPIO as GPIO


class Line:
    def __init__(self):
        self.pinright=16#gpio23
        self.pinleft=18#gpio24
        self.right=None
        self.left=None
        self.setup()

    def setup(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        GPIO.setup(self.pinright,GPIO.IN)
        GPIO.setup(self.pinleft,GPIO.IN)
        self.read()
    
    def read(self):
        self.right=int(GPIO.input(self.pinright))
        self.left=int(GPIO.input(self.pinleft))
        

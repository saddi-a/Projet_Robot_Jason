import RPi.GPIO as GPIO


class Line:
    def __init__(self):
        self.pinright=16#gpio23
        self.pinleft=18#gpio24
        self.right=False
        self.left=False
        self.setup()

    def setup(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        GPIO.setup(self.pinright,GPIO.IN)
        GPIO.setup(self.pinleft,GPIO.IN)
        self.read()
    
    def read(self):
        if(GPIO.input(self.pinright)==1):
            self.right=True
        else:
            self.right=False
        if(GPIO.input(self.pinleft)==1):
            self.left=True
        else:
            self.left=False   


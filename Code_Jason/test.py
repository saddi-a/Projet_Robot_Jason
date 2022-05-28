import time
import RPi.GPIO as GPIO
from Camera import Camera
from Motor import Motor
from Ultrasonic import Ultrasonic

if __name__ == '__main__':
    m=Motor()
    c=Camera()
    u=Ultrasonic()

    for i in range(200) :
        c.readLight()
        u.measure()
        print("The traficlight color is :",c.trafficlightColor)
        print("The distance is:",u.distance)

        if (c.trafficlightColor=='red' or u.distance<10):
            m.stop()
        elif(c.trafficlightColor=='orange' or u.distance<20):
            m.setSpeed(20)
            m.forward()
        elif(c.trafficlightColor=='green'):
            m.setSpeed(50)
            m.forward()
        else:
            m.setSpeed(30)
            m.forward()


        time.sleep(0.1)

    GPIO.cleanup()
    GPIO.setwarnings(True)



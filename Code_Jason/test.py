import re
import time
from Camera import Camera
from Motor import Motor

if __name__ == '__main__':
    m=Motor()
    c=Camera()

    while(1):
        c.readLight()
        print("The traficlight color is :",c.trafficlightColor)

        if (c.trafficlightColor=='red'):
            m.stop()
        elif(c.trafficlightColor=='orange'):
            m.setSpeed(20)
            m.forward()
        elif(c.trafficlightColor=='green'):
            m.setSpeed(50)
            m.forward()
        else:
            m.setSpeed(30)
            m.forward()


        time.sleep(0.3)





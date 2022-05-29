from re import L
from Line import Line
import RPi.GPIO as GPIO
import time

if __name__ == '__main__':
    l=Line()

    for i in range(400) :
        l.read()
        print("Right sensor is :",l.right)
        print("Left sensor is :",l.left)

        time.sleep(0.1)
        print(i)


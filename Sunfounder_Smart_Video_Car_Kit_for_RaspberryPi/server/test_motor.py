#!/usr/bin/env python
import RPi.GPIO as GPIO
import PCA9685 as p
import Motor
import time    # Import necessary modules



if __name__ == '__main__':
	m=Motor()
	m.setSpeed(10)
	m.forward()
	time.sleep(3)
	m.backward()
	time.sleep(3)
	m.stop()

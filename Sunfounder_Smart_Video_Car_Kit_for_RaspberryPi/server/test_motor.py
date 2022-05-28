#!/usr/bin/env python
import RPi.GPIO as GPIO
import PCA9685 as p
import motor
import time    # Import necessary modules


if __name__ == '__main__':
	setup()
	setSpeed(10)
	forward()
	time.sleep(5)
	backward()
	time.sleep(5)
	stop()


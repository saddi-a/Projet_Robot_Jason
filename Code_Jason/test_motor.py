#!/usr/bin/env python
from Motor import Motor
import time    # Import necessary modules



if __name__ == '__main__':
	m=Motor()
	m.setSpeed(1)
	m.forward()
	time.sleep(2)
	m.backward()
	time.sleep(2)
	m.stop()

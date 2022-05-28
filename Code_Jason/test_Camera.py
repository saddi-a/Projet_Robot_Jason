#!/usr/bin/env python
from Camera import Camera
import time    # Import necessary modules



if __name__ == '__main__':
	c=Camera()
	
	while(1):
		c.readLight()
		print("The traficlight color is :",c.trafficlightColor)
		time.sleep(0.3)

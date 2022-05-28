# Python code for Multiple Color Detection 
import time
import numpy as np 
import cv2 


class Camera:

	def __init__(self):
		
		self.camera = cv2.VideoCapture(0) 
		self.imageFrame = None
		self.hsvFrame = None

		self.red_mask = None
		self.res_red = None
		
		self.green_mask = None 
		self.res_green = None

		self.orange_mask = None
		self.res_orange = None

		# Set range for red color
		self.red_lower = np.array([160, 160, 150], np.uint8) 
		self.red_upper = np.array([200, 200, 255], np.uint8) 

		# Set range for green color 
		self.green_lower = np.array([50, 52, 72], np.uint8) 
		self.green_upper = np.array([102, 255, 255], np.uint8) 

		# Set range for orange color
		self.orange_lower = np.array([10, 130, 150], np.uint8) 
		self.orange_upper = np.array([50, 255, 255], np.uint8) 

		# Filter size for morphological transformation
		self.kernal = np.ones((5, 5), "uint8") 

		self.traficlightColor="not read"
		

	def readLight(self):
		#Read the frame
		self.readFrame()

		#Setup color masks
		self.setMask()

		#Reading traficlight color
		self.readColor()
		

	def readFrame(self):

		# Reading the video from the  in image frames
		_, self.imageFrame = self.camera.read()
		# Convert the imageFrame in BGR(RGB color space) from 
		# HSV(hue-saturation-value) color space 
		self.hsvFrame = cv2.cvtColor(self.imageFrame, cv2.COLOR_BGR2HSV) 

	def setMask(self):
		
		# define mask 
		self.red_mask = cv2.inRange(self.hsvFrame, self.red_lower, self.red_upper)
		self.green_mask = cv2.inRange(self.hsvFrame, self.green_lower, self.green_upper) 
		self.orange_mask = cv2.inRange(self.hsvFrame, self.orange_lower, self.orange_upper) 
		
		# Morphological Transform, Dilation 
		# for each color and bitwise_and operator 
		# between imageFrame and mask determines 
		# to detect only that particular color
		
		# For red color 
		self.red_mask = cv2.dilate(self.red_mask, self.kernal) 
		self.res_red = cv2.bitwise_and(self.imageFrame, self.imageFrame, mask = self.red_mask) 
		
		# For green color 
		self.green_mask = cv2.dilate(self.green_mask, self.kernal) 
		self.res_green = cv2.bitwise_and(self.imageFrame, self.imageFrame, mask = self.green_mask) 
		
		# For orange color 
		self.orange_mask = cv2.dilate(self.orange_mask, self.kernal) 
		self.res_orange = cv2.bitwise_and(self.imageFrame, self.imageFrame, mask = self.orange_mask)
	
			
	def readColor(self) :
		
		# Creating contour to track green color 
		contours, hierarchy = cv2.findContours(green_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
		
		for pic, contour in enumerate(contours): 
			area = cv2.contourArea(contour) 
			if(area > 300): 
				color ="green"
		# Creating contour to track orange color 
		contours, hierarchy = cv2.findContours(orange_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
		for pic, contour in enumerate(contours): 
			area = cv2.contourArea(contour) 
			if(area > 300):
				color="orange"

		# Creating contour to track red color 
		contours, hierarchy = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
	
		for pic, contour in enumerate(contours): 
			area = cv2.contourArea(contour) 
			if(area > 300): 
				color="red"

		print("The traficlight color is :",color)
		self.traficlightColor="not read"


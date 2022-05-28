# Python code for Multiple Color Detection 
import time
import numpy as np 
import cv2 

# Capturing video through webcam 
webcam = cv2.VideoCapture(0) 

# Start a while loop 
while(1): 
	
	# Reading the video from the 
	# webcam in image frames 
	_, imageFrame = webcam.read() 

	# Convert the imageFrame in 
	# BGR(RGB color space) to 
	# HSV(hue-saturation-value) 
	# color space 
	hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV) 

	# Set range for red color and 
	# define mask 
	red_lower = np.array([160, 160, 150], np.uint8) 
	red_upper = np.array([200, 200, 255], np.uint8) 
	red_mask = cv2.inRange(hsvFrame, red_lower, red_upper) 

	# Set range for green color and 
	# define mask 
	green_lower = np.array([50, 52, 72], np.uint8) 
	green_upper = np.array([102, 255, 255], np.uint8) 
	green_mask = cv2.inRange(hsvFrame, green_lower, green_upper) 

	# Set range for orange color and 
	# define mask 
	orange_lower = np.array([10, 130, 150], np.uint8) 
	orange_upper = np.array([50, 255, 255], np.uint8) 
	orange_mask = cv2.inRange(hsvFrame, orange_lower, orange_upper) 
	
	# Morphological Transform, Dilation 
	# for each color and bitwise_and operator 
	# between imageFrame and mask determines 
	# to detect only that particular color 
	kernal = np.ones((5, 5), "uint8") 
	
	# For red color 
	red_mask = cv2.dilate(red_mask, kernal) 
	res_red = cv2.bitwise_and(imageFrame, imageFrame, mask = red_mask) 
	
	# For green color 
	green_mask = cv2.dilate(green_mask, kernal) 
	res_green = cv2.bitwise_and(imageFrame, imageFrame, mask = green_mask) 
	
	# For orange color 
	orange_mask = cv2.dilate(orange_mask, kernal) 
	res_orange = cv2.bitwise_and(imageFrame, imageFrame, mask = orange_mask)
	
	color="aucun"


	# Creating contour to track green color 
	contours, hierarchy = cv2.findContours(green_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
	
	for pic, contour in enumerate(contours): 
		area = cv2.contourArea(contour) 
		if(area > 300): 
			color ="vert"
			#x, y, w, h = cv2.boundingRect(contour) 
			#imageFrame = cv2.rectangle(imageFrame, (x, y), (x + w, y + h), (0, 255, 0), 2) 
			#cv2.putText(imageFrame, "Green Colour", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0))
            
	# Creating contour to track orange color 
	contours, hierarchy = cv2.findContours(orange_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
	for pic, contour in enumerate(contours): 
		area = cv2.contourArea(contour) 
		if(area > 300):
			color="orange"
			#x, y, w, h = cv2.boundingRect(contour) 
			#imageFrame = cv2.rectangle(imageFrame, (x, y), (x + w, y + h), (0, 165, 255), 2) 
			#cv2.putText(imageFrame, "orange Colour", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 165, 255) )
			
	# Creating contour to track red color 
	contours, hierarchy = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
	
	for pic, contour in enumerate(contours): 
		area = cv2.contourArea(contour) 
		if(area > 300): 
			color="rouge"
			#x, y, w, h = cv2.boundingRect(contour) 
			#imageFrame = cv2.rectangle(imageFrame, (x, y), (x + w, y + h), (0, 0, 255), 2) 
			#cv2.putText(imageFrame, "Red Colour", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255))

	print("Couleur du feu tricolor :",color)
	# Program Termination 
# 	cv2.imshow("Multiple Color Detection in Real-TIme", imageFrame) 
# 	if cv2.waitKey(10) & 0xFF == ord('q'): 
# 		cap.release() 
# 		cv2.destroyAllWindows() 
# 		break

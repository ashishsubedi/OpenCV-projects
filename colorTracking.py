# -*- coding: utf-8 -*-
"""
Created on Sun May 26 01:53:10 2019

@author: Dell
"""

import cv2
import numpy as np

def main():
	
	cap = cv2.VideoCapture(0)
	ret = True
	if cap.isOpened():
		while ret:	
			ret, frame = cap.read()
			
			#To detect color nicely, we convert original BGR image to HSV image
			hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
			
			#Tracking color in range of something
			
			# Blue color of my tee or that polythene beisde me
			low = np.array([100,70,100])
			high = np.array([250,255,255])
			
			# Green color of that polythene beisde me
#			low = np.array([20,100,100])
#			high = np.array([100,255,255])
			
			#Red color is very hard to detect
			
			

			#Creating image mask of color in range
			
			image_mask = cv2.inRange(hsv,low,high)
			
			output = cv2.bitwise_and(frame,frame,mask = image_mask)
			
			
			
			cv2.imshow("Image Mask Video", image_mask)
			cv2.imshow("HSV Video", hsv)
			cv2.imshow("Real Video", frame)
			cv2.imshow("Output Video", output)
			if cv2.waitKey(1) == 27:
				break
	else:
		ret = False
	
	cv2.destroyAllWindows()
	cap.release()
	
if __name__ == '__main__':
	main()
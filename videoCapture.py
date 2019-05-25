# -*- coding: utf-8 -*-
"""
Created on Sun May 26 00:35:29 2019

@author: Dell
"""

import cv2



def main():

	windowName  = 'Live Video'
	cv2.namedWindow(windowName)
	cap = cv2.VideoCapture(0)
	
	if cap.isOpened():
		ret = True
		
		while ret:
			ret, frame = cap.read()
			
			cv2.imshow(windowName,frame)
			if cv2.waitKey(1) == 27:
				break
		
		cv2.destroyAllWindows()
			
	else:
		ret = False
	
	cap.release()
	
	
if __name__ == '__main__':
	main()
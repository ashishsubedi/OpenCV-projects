# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 09:15:41 2019

@author: Dell
"""

import numpy as np
import cv2


image = cv2.imread("C:/Users/Dell/Desktop/ImageProcessing/messi.jfif")
img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print(image.shape)

template = img[30:50,100:150]
h,w = template.shape
cv2.imshow('Image', image)
cv2.imshow('template', template)
cv2.waitKey(0)

result =  cv2.matchTemplate(img,template,cv2.TM_CCOEFF_NORMED)

print(result)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
print(min_loc)
topLeft = max_loc
bottomRight = (topLeft[0] + w, topLeft[1] + h)
cv2.rectangle(image, topLeft,bottomRight,(0,0,255),2)


cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows();
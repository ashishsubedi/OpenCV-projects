# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 21:24:45 2019

@author: Dell
"""

import cv2
import numpy as np

img = cv2.imread('C:/Users/Dell/Desktop/ImageProcessing/house.tif',0)

roi = img[100:150,:]

cv2.imshow('Image', roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
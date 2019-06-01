# -*- coding: utf-8 -*-
"""
Created on Mon May 27 02:13:08 2019

@author: Dell
"""

import cv2
import numpy as np

img1 = np.zeros((100,100),np.uint8)
img2 = np.zeros((100,100),np.uint8)

img1[0:60, 0:60] = 255
img2[40:100, 40:100] = 255

img = cv2.add(img1,img2)
cv2.imshow('img',img)






cv2.imshow('img1',img1)
cv2.imshow('img2',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 21:24:45 2019

@author: Dell
"""

import cv2
import numpy as np

img = cv2.imread('C:/Users/Dell/Desktop/ImageProcessing/4x4.bmp',0)

print(sum(sum(img)))

moments = cv2.moments(img)
print(moments)
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
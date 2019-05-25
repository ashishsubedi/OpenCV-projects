# -*- coding: utf-8 -*-
"""
Created on Sat May 25 23:35:14 2019

@author: Dell
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

imgpath = "C:\\Users\\Dell\\Desktop\\ImageProcessing\\lena_color_512.tif"

imgBGR = cv2.imread(imgpath)
imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

plt.imshow(imgHSV)
plt.show()

plt.imshow(imgRGB)
plt.show()


print(imgBGR)
print(imgRGB)
print(imgHSV)

#plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
#plt.show()


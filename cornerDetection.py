import cv2
import numpy as np


image = cv2.imread("C:/Users/Dell/Desktop/ImageProcessing/house.tif")
cv2.imshow("image",image)
cv2.waitKey(0)

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)
features = cv2.cornerHarris(gray,2,5,0.05)

cv2.imshow("image",features)
cv2.waitKey(0)

features = cv2.dilate(features,None)

image[features> 0.01*features.max()] = [0,0,255]
cv2.imshow("image",image)
cv2.waitKey(0)

cv2.destroyAllWindows()
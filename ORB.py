import cv2
import numpy as np

img = cv2.imread("C:/Users/Dell/Desktop/ImageProcessing/house.tif",0)

#Initiate ORB Object with 1000 max points
orb = cv2.ORB_create(1000)


#finding and drawing keypoints
#Alternatively you can use orb.detectAndCompute
kp = orb.detect(img,None)
kp,des = orb.compute(img,kp)
img2 = img.copy()
img2 = cv2.drawKeypoints(img,kp,img2,color=(0,255,0))

cv2.imshow('Image',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
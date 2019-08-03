import cv2
import numpy as np

img = cv2.imread("C:/Users/Dell/Desktop/ImageProcessing/house.tif",0)

#Initiate FAST Object
fast = cv2.FastFeatureDetector_create()

#finding and drawing keypoints

kp = fast.detect(img,None)
img2 = img.copy()
img2 = cv2.drawKeypoints(img,kp,img2,color=(0,0,255))

# Print all default params
print ("Threshold: ", fast.getThreshold())
print ("nonmaxSuppression: ", fast.getNonmaxSuppression())
print ("neighborhood: ", fast.getType())
print ("Total Keypoints with nonmaxSuppression: ", len(kp))


cv2.imshow('Image',img2)
cv2.waitKey(0)

#Disable nomaxSuppression
fast.setNonmaxSuppression(False)
kp = fast.detect(img,None)
print ("Total Keypoints without nonmaxSuppression: ", len(kp))

img2 = cv2.drawKeypoints(img,kp,img2,color=(255,0,0))



cv2.imshow('Image',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
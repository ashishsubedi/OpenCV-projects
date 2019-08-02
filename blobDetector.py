import cv2
import numpy as np

img = cv2.imread("C:/Users/Dell/Desktop/ImageProcessing/blob.jpg",cv2.IMREAD_GRAYSCALE)

params = cv2.SimpleBlobDetector_Params()

params.minThreshold = 10
params.maxThreshold = 200

params.filterByArea = True
params.minArea = 1000

params.filterByCircularity = True
params.minCircularity = .6

params.filterByConvexity = True
params.minConvexity = 0.8

params.filterByInertia = True;
params.minInertiaRatio = 0.1





detector = cv2.SimpleBlobDetector_create(params)

keypoints = detector.detect(img)
image = img.copy()

image = cv2.drawKeypoints(img,keypoints,image, (0,0,255),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
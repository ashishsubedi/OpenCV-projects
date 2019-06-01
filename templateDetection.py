import cv2
import numpy as np

img = cv2.imread('original_image.jpg')
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

template = cv2.imread('template_image.jpg')
template_gray = cv2.cvtColor(template,cv2.COLOR_BGR2GRAY)

w,h = template_gray.shape[::-1]

res = cv2.matchTemplate(img_gray,template_gray,cv2.TM_CCOEFF_NORMED)
threshold = 0.7
loc = np.where(res >= threshold)

pts = zip(*loc[::-1])

for pt in pts:
    cv2.rectangle(img,pt,(pt[0]+w,pt[1]+h),(0,255,255),2)


cv2.imshow('original',img)
cv2.imshow('gray',img_gray)
cv2.imshow('template',template)

cv2.waitKey(0)
cv2.destroyAllWindows()

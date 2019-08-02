import numpy as numpy
import cv2


'''
    1) Convert to grayscale
    2) Blur using Gaussian filter
    3) Edge Detecting
    4) Thresholding?

'''


def sketch(image):
    img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    img_blur = cv2.GaussianBlur(img, (5, 5), 0)

    edges = cv2.Canny(img_blur,10,80)
    mask1 = cv2.bitwise_not(edges)
    _,mask2 = cv2.threshold(edges, 100, 255, cv2.THRESH_BINARY_INV)
    
    return mask1,mask2


cap = cv2.VideoCapture(0)

if cap.isOpened():
    ret = True
    while(ret):
        ret, frame = cap.read()
        img1,img2 = sketch(frame)
        cv2.imshow("Sketch using bitwise not", img1)
        cv2.imshow("Sketch using threshold", img2)
        if cv2.waitKey(1) == 27:
            break


cv2.destroyAllWindows()
cap.release()

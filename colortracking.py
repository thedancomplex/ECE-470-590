import cv2
import numpy as np

while(1):

    frame = cv2.imread('robot.png')
    frame = cv2.resize(frame, (0,0), fx=0.2, fy=0.2) 
#    frameBGR = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of white color in HSV
    # change it according to your need !
    # blue
    upper_white = np.array([130,255,255], dtype=np.uint8)
    lower_white = np.array([110,0,0], dtype=np.uint8)

    # green
    upper_white = np.array([70,255,255], dtype=np.uint8)
    lower_white = np.array([50,0,0], dtype=np.uint8)

    # red
    upper_white = np.array([20,255,255], dtype=np.uint8)
    lower_white = np.array([0,100,100], dtype=np.uint8)

    # Threshold the HSV image to get only white colors
    mask = cv2.inRange(hsv, lower_white, upper_white)
    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()

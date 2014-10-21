import cv2
import numpy as np

while(1):

    frame = cv2.imread('robotnoise2.png')
    frame = cv2.resize(frame, (0,0), fx=0.2, fy=0.2) 
    height, width = frame.shape[:2]
    print 'width = ' , width , ' height = ', height
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
    mask0 = cv2.inRange(hsv, lower_white, upper_white)

    kernel = np.ones((5,5),np.uint8)
    maskErode = cv2.erode(mask0,kernel,iterations = 1)

    mask = maskErode
    x0 = 0
    y0 = 0
    i = 1
    for x in range(0,width):
      for y in range(0,height):
        if mask[y,x] != 0:
          x0 = x0 + x
          y0 = y0 + y
          i  = i  + 1  

    print 'x0 = ', x0, ' y0 = ', y0, ' i = ', i 
    xf = int(np.floor(x0/i))
    yf = int(np.floor(y0/i))
    
    print 'xf = ', xf, ' yf = ', yf 
    # Draw Circle
    im = frame
    cv2.circle(im,(xf,yf), 10, (255,0,255),-1)

    # Bitwise-AND mask and original image
#    res = cv2.bitwise_and(frame,frame, mask= maskErode)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask0)
    cv2.imshow('mask erode',maskErode)
#    cv2.imshow('res',res)
    cv2.imshow('img',im)

    k = cv2.waitKey(100) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()

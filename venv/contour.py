import numpy as np
import cv2

img = cv2.imread('openCVimage.png',1)
imggray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imggray,150,255,0)

contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

print('Number of contours : '+ str(len(contours)))
print(contours[0])

cv2.drawContours(img,contours,-1,(0,255,0),1)
cv2.imshow('Image',img)
cv2.imshow('Image Gray',imggray)

cv2.waitKey(0)
cv2.destroyAllWindows()
import numpy as np
import cv2

img = cv2.imread('lena.png',1)

#img = cv2.line(img,(0,0),(255,255), (0,0,255), 5)

img = cv2.rectangle(img,(0,0),(255,255), (0,0,255), -1)#-1 dunnama rectrangleeka fill wenaw adilatyna color eken

img = cv2.circle(img,(450,75),63,(0,0,255),-1)

cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()


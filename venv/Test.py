import cv2

img = cv2.imread('lena.png',0)

print(img)

cv2.imshow('imageWindow',img)

keyValue = cv2.waitKey(0)##0 dunnama close wewenne ne

print(keyValue)#press karana key eke value eka ganna pluwan meken

if keyValue == 27:
    cv2.destroyAllWindows()
elif keyValue == ord('s'):
    cv2.imwrite('lenaWriteGray.png', img)
    cv2.destroyAllWindows()



#cv2.imwrite('lenaWriteGray.png',img)


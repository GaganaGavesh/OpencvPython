import cv2
import numpy as np

cap = cv2.VideoCapture('vtest.avi')
ret, frame1 = cap.read()
ret, frame2 = cap.read()
#ret, frame3 = cap.read()

count = 0

while(cap.isOpened()):
    difference = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY)
    gussianBlur = cv2.GaussianBlur(gray, (5, 5), 0)  # zigma value eka thama 0
    ret, thresholdImage = cv2.threshold(gussianBlur, 30, 255, cv2.THRESH_BINARY)
    dilatedImage = cv2.dilate(thresholdImage, None, iterations=3)
    contours, hierarchy = cv2.findContours(dilatedImage, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    # print(str(len(contours)))

    contCount = 0

    for contour in contours:

        (x,y,w,h) = cv2.boundingRect(contour)

        if cv2.contourArea(contour) < 700:
            continue
        elif cv2.contourArea(contour) > 10000:
            continue
        else:
            cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)
            contCount = contCount+1

    print('Moving People Count : '+ str(contCount))
    cv2.putText(frame1,"MovingPeopleConunt : {}".format(str(contCount)),(10,50),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),3)
    # cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)

    cv2.imshow('VideoFeed',frame1)

    fullImage = cv2.imshow('VideoFeed', frame1)

    frame1 = frame2
    ret, frame2 = cap.read()

    if cv2.waitKey(40) == 27:
        break
    elif cv2.waitKey(40) == ord('c'):
        cv2.imwrite('random'+str(count)+'.png',fullImage)
        count = count + 1

# cv2.imshow('frame1',frame1)
# cv2.imshow('frame2',frame3)
# cv2.imshow('Difference12',difference)
# cv2.imshow('Gray',gray)
# cv2.imshow('GussianBlur',gussianBlur)
# cv2.imshow('ThresholdImage',thresholdImage)
# cv2.imshow('DilatedImage',dilatedImage)

# cv2.waitKey(0)
cap.release()
cv2.destroyAllWindows()
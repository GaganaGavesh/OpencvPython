import cv2

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('OutputVideo.avi',fourcc,20.0,(640,480))

while(cap.isOpened()):
    ret, frame = cap.read()#frame ekata frame eka enawa ret kiyana ekat true enawa

    if ret == True:
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        #print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        #print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

        #out.write(frame)

        cv2.imshow('frame',frame)


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break

cap.release()
cv2.destroyAllWindows()
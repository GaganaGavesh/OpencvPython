import cv2

cv2.namedWindow("test")

img_counter = 0

while img_counter < 51:
    img_name = "Dematagod_junction_730_830_{}.png".format(img_counter)
    img = cv2.imread(img_name)

    frame = cv2.GaussianBlur(img, (3, 3), 0)
    # frame = cv2.medianBlur(img, 5)

    cv2.imshow("test", frame)


    cv2.imwrite(img_name, frame)
    print("{} written!".format(img_name))
    img_counter += 1

    cv2.waitKey(10)

# img_name = "Central_Bus_Stand_2_730_830_{}.png".format(img_counter)
# img = cv2.imread(img_name)
#
# g_frame = cv2.GaussianBlur(img, (3, 3), 0)
# frame = cv2.medianBlur(g_frame, 5)
#
# cv2.imshow("test", frame)
#
# cv2.imwrite(img_name, frame)
# print("{} written!".format(img_name))
# img_counter += 1
#
# cv2.waitKey(0)
# img.release()

cv2.destroyAllWindows()
import cv2


image = cv2.imread('1_0024.png')
gauss = cv2.GaussianBlur(image, (5,5), 0)
median = cv2.medianBlur(image, 31)
cv2.imshow("image",image)
cv2.imshow("gauss",gauss)
cv2.imshow("median",median)
cv2.waitKey(0)
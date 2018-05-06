import cv2
img = cv2.imread('lena.png')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('img',img)
cv2.imshow('hsv',hsv)
cv2.waitKey(0)

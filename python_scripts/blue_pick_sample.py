import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([100, 50, 50])
    upper_blue = np.array([150, 255, 255])
    img_mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
    img_color_blue = cv2.bitwise_and(frame, frame, mask=img_mask_blue)

    cv2.imshow("SHOW COLOR DEFAULT", frame) 
    cv2.imshow("SHOW COLOR BLUE", img_color_blue)

    k = cv2.waitKey(1)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()

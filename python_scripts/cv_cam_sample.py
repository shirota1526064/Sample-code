#!/usr/bin/python

import cv2

cap = cv2.VideoCapture(0)

try:
    while(True):
        ret, frame = cap.read()

        if ret == False:
            print "no camera"
            break
        else:
            cv2.imshow('cam_capture0',frame)
            k = cv2.waitKey(1)
            if k == 27:
                break
except KeyboardInterrupt:
    print "Ctl+C"

cap.release()
cv2.destroyAllWindows()

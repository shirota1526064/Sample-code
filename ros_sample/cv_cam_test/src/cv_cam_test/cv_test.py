#!/usr/bin/env python

import roslib
import rospy
import cv2

def cv_test(cv_image):
    cv2.imshow("cv_image",cv_image)
    cv2.waitKey(1)

if __name__=="__main__":
    pass

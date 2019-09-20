#!/usr/bin/env python

import roslib
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from cv_cam_test.cv_test import cv_test

class Image_converter:
    def __init__(self):
        self.img_sub = rospy.Subscriber("/usb_cam/image_raw",Image,self.callback)
        self.bridge = CvBridge()

    def callback(self,data):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
            cv_test(cv_image)
        except CvBridgeError as e:
            print e

if __name__ == "__main__":
    image_converter = Image_converter()

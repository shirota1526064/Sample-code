#!/usr/bin/env python

import rospy
import numpy as np
import math
import tf
from std_msgs.msg import String
from apriltags2_ros.msg import AprilTagDetectionArray

class Tag_listener(object):
    def __init__(self):
        self._sub_tag = rospy.Subscriber('/tag_detections',AprilTagDetectionArray,self._callback_tag)
        self._tag_position = np.zeros(4, dtype = 'float64')
        self._base_position = np.zeros(7, dtype = 'float64')

    def _get_pose(self,p_list, name, base_name):
        br = tf.TransformBroadcaster()
        br.sendTransform(
            p_list[0:3],
            p_list[3:7],
            rospy.Time.now(),
            name,
            base_name)

    def _change_angle(self,quaternion):
        #External parameters
        e = tf.transformations.euler_from_quaternion(quaternion)    #change angle
        return e

    def main(self):
        rospy.init_node('tag_listener')
        rospy.set_param('target_int',1)
        self._listener = tf.TransformListener()
        rospy.spin()

    def _callback_tag(self,messege):

        if len(messege.detections) > 0:
            '''
            angle_q = messege.detections[0].pose.pose.pose.orientation
            angle_r = self._change_angle([angle_q.x,angle_q.y,angle_q.z,angle_q.w])

            self._tag_position[0] = messege.detections[0].pose.pose.pose.position.x
            self._tag_position[1] = messege.detections[0].pose.pose.pose.position.y
            self._tag_position[2] = messege.detections[0].pose.pose.pose.position.z
            self._tag_position[3] = math.degrees(angle_r[2])

            if messege.detections[0].id[0] == 0:
                self._base_position = [self._tag_position[0],self._tag_position[1],self._tag_position[2],
                    angle_q.x, angle_q.y, angle_q.z, angle_q.w]

            #rospy.loginfo("x : %s",self._tag_position[0])
            #rospy.loginfo("y : %s",self._tag_position[1])
            #rospy.loginfo("z : %s",self._tag_position[2])
            #self._get_pose(self._base_position,"base","usb_cam")
            #print self._base_position
            '''
            param_name = rospy.search_param('target_int')
            target_str = 'tag'+str(rospy.get_param(param_name))
            try:
                (trans1,rot1) = self._listener.lookupTransform('tag0', target_str, rospy.Time(0))
                self.camera_data = trans1 + list(self._change_angle(rot1))
                #print 'cm:0 position',self.camera_data[0:3]
                print self.camera_data[0],',',self.camera_data[1],',',self.camera_data[5]
            except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
                pass
        else:
            print "nothing"

if __name__ == "__main__":
    tag_listener = Tag_listener()
    tag_listener.main()

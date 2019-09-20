#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import numpy as np
import tf
import math

class Coordinate(object):
    # 座標系の設定するクラス
    def __init__(self, name, base_name, position):
        rospy.init_node('tf_set', anonymous=True)
        self._name = name # 生成する座標系の名前
        self._base_name = base_name # 基準となる座標系
        self._position = position[0:3]+ list(self._angle_conversion(position[3:6])) # 姿勢(角度はオイラー)

    def _angle_conversion(self,euler_angle):
        # 角度をオイラーからクオータニオンに変換
        e = tf.transformations.quaternion_from_euler(euler_angle[0],euler_angle[1],euler_angle[2])
        return e

    def _set_pose(self):
        # 座標系を公開する関数
        br = tf.TransformBroadcaster()
        br.sendTransform(self._position[0:3], self._position[3:7], rospy.Time.now(), self._name, self._base_name)

if __name__ == "__main__":
    sigma1 = Coordinate('sigma1', 'map', [0.5, 0.0, 0.0, 0.0, 0.0, 0.0]) # 座標系sigma1を生成
    sigma2 = Coordinate('sigma2', 'sigma1', [0.0, 0.25, 0.0, 0.0, 0.0, math.pi/6]) # 座標系sigma2を生成
    listener = tf.TransformListener() # tfの情報を受け取るTransformListenerオブジェクトを生成

    r = rospy.Rate(10)

    while not rospy.is_shutdown():
        sigma1._set_pose() # sigma1の座標系を更新
        sigma2._set_pose() # sigma2の座標系を更新

        # 相対的な姿勢を求める
        base_name = 'map' # 基準となる座標系
        target_name = 'sigma2' # 目標の座標系

        try:
            (trans,rot) = listener.lookupTransform(base_name, target_name, rospy.Time(0))
            # transは位置, rotは姿勢(クオータニオン)
            print "Relative pose", trans, rot
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            # 相対姿勢が出せないときの処理
            print "no data"

        r.sleep()

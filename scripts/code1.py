#!/usr/bin/env python
# -*- coding:utf-8 -*-

import rospy
from std_msgs.msg import Int32

def counter():
    rospy.init_node('count') # rospyにcountのノードを通知
    pub = rospy.Publisher('counter1', Int32, queue_size=1) # ノードがcounter1というTopicにInt32のメッセージタイプで送る
    rate = rospy.Rate(10)   # 10Hz
    n = 0
    while not rospy.is_shutdown(): # rospyがshutdownしない時の構成
        n += 1
        pub.publish(n)
        rate.sleep()

if __name__ == '__main__': # main program
    try:
        counter()  # counterの関数にjump
    except rospy.ROSInterruptException: pass # 例外における対処

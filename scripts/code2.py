#!/usr/bin/env python
# -*- coding:utf-8 -*-

import rospy
from std_msgs.msg import Int32

n = 0

def rcv(message):
    global n
    n = message.data*0.1

def receiver():
    rospy.init_node('receiver')
    sub = rospy.Subscriber('counter1', Int32, rcv)
    pub = rospy.Publisher('receiver', Int32, queue_size=1)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        pub.publish(n)
        rate.sleep()

if __name__ == '__main__':
    receiver()

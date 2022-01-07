#SPDX-License-Identifier: BSD 3-Clause "New" or "Revised" License                                                                                                                            #Copyright (C) 2022 Hayato Sakurai and Ryuichi Ueda. All rights reserved
#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

n = 0

def cb(message):
    global n
    n = message.data*2
    rospy.loginfo(n)

if __name__ == '__main__':
    rospy.init_node('fourth')
    sub = rospy.Subscriber('twice', Int32, cb)
    pub = rospy.Publisher('fourth', Int32, queue_size=1)
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        pub.publish(n)
        rate.sleep()

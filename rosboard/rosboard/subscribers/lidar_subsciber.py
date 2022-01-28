#!/usr/bin/env python
import roslib
import rospy
import os
from std_msgs.msg import String
def callback(data):
    if data.data=='start':
       print("recording the bag")
       cmd = 'rosbag record -a'
       os.system(cmd)
    elif data.data=="stop":
       print("stop recording data")
       os._exit(0)
def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("lidar_control", String, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()

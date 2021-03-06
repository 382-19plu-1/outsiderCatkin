#!/usr/bin/env python3

import rospy
import message_filters # To Achieve Multiple subscriber
from std_msgs.msg import Float64
from std_msgs.msg import String

class VESC_Node(object):
    def __init__(self):

        rospy.init_node("test_pub_py", anonymous=True)

        # Rate
        self.loop_rate = rospy.Rate(60)

        # Node is publishing to the topic
        self.vesc1_pub = rospy.Publisher('vesc1_speed', Float64, queue_size=10)
        self.vesc2_pub = rospy.Publisher('vesc2_speed', Float64, queue_size=10)
        self.state_pub = rospy.Publisher('state', String, queue_size=10)

    def callback(self):
        rospy.loginfo("this is a info - 1")

        

    def start(self):

        # spin() simply keeps python from exiting until this node is stopped
        #rospy.spin()
        self.state ="W"
        while not rospy.is_shutdown():
            self.vesc1_pub.publish(5.1)
            self.vesc2_pub.publish(1.1)
            self.state_pub.publish(self.state)
            self.loop_rate.sleep()
        

if __name__ == '__main__':
    import threading
    import time

    my_node = VESC_Node()

    def job():
        my_node.start()
    
    t = threading.Thread(target = job,daemon = True)

    t.start()

    

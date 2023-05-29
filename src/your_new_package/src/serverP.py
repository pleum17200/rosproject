#! /usr/bin/env python3
from std_srvs.srv import Empty, EmptyResponse
import rospy
import time

def server_go_home_callback(req):
    rospy.loginfo("Going to home.")
    time.sleep(2)
    rospy.loginfo("Arrived.")
    return EmptyResponse()

def server_go_to_kitchen_callback(req):
    rospy.loginfo("Going to kitchen.")
    time.sleep(2)
    rospy.loginfo("Arrived.")
    return EmptyResponse()

def server_stop_callback(req):
    rospy.loginfo("Stop!")
    return EmptyResponse()

if __name__ == "__main__":
    rospy.init_node('service_server_node')
    
    rospy.Service('go_home', Empty, server_go_home_callback)
    rospy.Service('go_to_kitchen', Empty, server_go_to_kitchen_callback)
    rospy.Service('stop', Empty, server_stop_callback)
    
    rospy.loginfo("Service server node ready!")
    rospy.spin()
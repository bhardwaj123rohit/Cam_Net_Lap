#!/usr/bin/env python
import rospy
from learn_ball.msg import ballCor

def callback(data):
  rospy.loginfo("x: %d y: %d radius: %d UpperH %d UpperS %d UpperV %d LowerH %d LowerS %d LowerV %d" % (data.x, data.y,data.radius,data.upperH,data.upperS,data.upperV,data.lowerH,data.lowerS,data.lowerV))
 
def listener():
  rospy.init_node('green_listener', anonymous=True)
  rospy.Subscriber("green_chatter", ballCor, callback)
 
     # spin() simply keeps python from exiting until this node is stopped
  rospy.spin()
 
if __name__ == '__main__':
  listener()

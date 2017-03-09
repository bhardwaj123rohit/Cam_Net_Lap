#!/usr/bin/env python
import rospy
from learn_ball.msg import ballCor
from collections import deque
import numpy as np
import argparse
import imutils
import cv2

# Working Red - RPI
greenLower = (10,200,110)
greenUpper = (25,255,180)


msg = ballCor()
msg.heading="SIR"
msg.color="RED"
msg.x = 0
msg.y = 0
msg.radius = 0
msg.upperH = greenUpper[0]
msg.upperS = greenUpper[1]
msg.upperV = greenUpper[2]
msg.lowerH = greenLower[0]
msg.lowerS = greenLower[1]
msg.lowerV = greenLower[2]

def talker():
	global msg

	pub = rospy.Publisher('topic_sir', ballCor, queue_size=50)

	rospy.init_node('Sir', anonymous=True)
	#rospy.loginfo("Sir Initialized Default Color: RED")
	rospy.loginfo("Sir's default searching color: "+msg.color)
	#msg.heading="SIR"
	#pub.publish(msg)

	r = rospy.Rate(10) #10hz
	# global detected
	detected = False
    # Initialize the Green ball color 
	pts = deque(maxlen=64)
	while not rospy.is_shutdown():
		col = raw_input("Enter the color(RED/GREEN)")
		if col == "RED":
			msg.x=0;
			msg.y=0;
			msg.radius=0;
			msg.color="RED"
			#RPI Cam RED
			greenLower = (10,200,110)
			greenUpper = (25,255,180)

			msg.upperH = greenUpper[0]
			msg.upperS = greenUpper[1]
			msg.upperV = greenUpper[2]
			msg.lowerH = greenLower[0]
			msg.lowerS = greenLower[1]
			msg.lowerV = greenLower[2]
			rospy.loginfo("Sending Command to Detect RED Color")
			msg.heading="SIR"
			pub.publish(msg)

		elif col == "GREEN":
			msg.x=0;
			msg.y=0;
			msg.radius=0;
			msg.color="GREEN"
			#RPI Cam Green
			greenLower = (30,150,40)
			greenUpper = (45,255,150)

			msg.upperH = greenUpper[0]
			msg.upperS = greenUpper[1]
			msg.upperV = greenUpper[2]
			msg.lowerH = greenLower[0]
			msg.lowerS = greenLower[1]
			msg.lowerV = greenLower[2]
			rospy.loginfo("Sending Command to Detect GREEN Color")
			msg.heading="SIR"
			pub.publish(msg)
		else:
			rospy.loginfo("Wrong Input ")


if __name__ == '__main__':
	try:
		talker()
		
	except rospy.ROSInterruptException: 
		pass

			
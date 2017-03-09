#!/usr/bin/env python
import rospy
from learn_ball.msg import ballCor
from collections import deque
import numpy as np
import argparse
import imutils
import cv2

# Working Green Rohit's Laptop
#greenLower = (29,86,100)
#greenUpper = (60,255,255)

# Working Red Rohit's Laptop
greenLower = (10,100,100)
greenUpper = (25,200,200)

pub = rospy.Publisher('topic_laptop', ballCor, queue_size=50)
msg = ballCor()
msg.heading="Laptop"
msg.color="RED - default"
msg.x = 0
msg.y = 0
msg.radius = 0
msg.upperH = greenUpper[0]
msg.upperS = greenUpper[1]
msg.upperV = greenUpper[2]
msg.lowerH = greenLower[0]
msg.lowerS = greenLower[0]
msg.lowerV = greenLower[0]
detected = False

def combine():
	rospy.init_node('laptop', anonymous=True)
	rospy.Subscriber("topic_rpi_1", ballCor, callback)

	rospy.Subscriber("topic_rpi_2", ballCor, callback)
	# For second rpi
	
	# Initial Publishing
	rospy.loginfo("laptop Initialized Default Color: RED")
	rospy.loginfo("laptop searching for Ball "+msg.color)
	pub.publish(msg)
	talker()
	rospy.spin()





def callback(data):
	rospy.loginfo("Node: %s ordered you to detect color: %s" % (data.heading,data.color))
  #rospy.loginfo("x: %d y: %d radius: %d UpperH %d UpperS %d UperV %d LowerH %d LowerS %d LowerV %d" % (data.x, data.y,data.radius,data.upperH,data.upperS,data.upperV,data.lowerH,data.lowerS,data.lowerV))
	global msg
	rospy.loginfo("laptop searching for Ball "+data.color)
  #msg.heading=data.heading
	msg.color = data.color
	msg.upperH = data.upperH
	msg.upperS = data.upperS
	msg.upperV = data.upperV
	msg.lowerH = data.lowerH
	msg.lowerS = data.lowerS
	msg.lowerV = data.lowerV
	talker()

def talker():
	global msg
	r = rospy.Rate(10) #10hz
	global detected
	detected = False
    # Initialize the Green ball color 
	pts = deque(maxlen=64)


	#Grab webCam
	camera = cv2.VideoCapture(0)

	while not rospy.is_shutdown():
		# grab the current frame
		(grabbed, frame) = camera.read()

		# resize the frame, blur it, and convert it to the HSV
		# color space
		frame = imutils.resize(frame, width=600)
		# blurred = cv2.GaussianBlur(frame, (11, 11), 0)
    	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

		# construct a mask for the color "green", then perform
		# a series of dilations and erosions to remove any small
		# blobs left in the mask
    	mask = cv2.inRange(hsv, greenLower, greenUpper)
    	mask = cv2.erode(mask, None, iterations=2)
    	mask = cv2.dilate(mask, None, iterations=2)

		# find contours in the mask and initialize the current
		# (x, y) center of the ball
    	cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
				cv2.CHAIN_APPROX_SIMPLE)[-2]
    	center = None

		# only proceed if at least one contour was found
    	if len(cnts) > 0:
			# find the largest contour in the mask, then use
			# it to compute the minimum enclosing circle and
			# centroid
			c = max(cnts, key=cv2.contourArea)
	  		((x, y), radius) = cv2.minEnclosingCircle(c)
	  		M = cv2.moments(c)
	  		center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

			# only proceed if the radius meets a minimum size
	  		if radius > 5:
	  			cv2.circle(frame, (int(x), int(y)), int(radius),(0, 255, 255), 2)
	  			cv2.circle(frame, center, 5,(0, 0, 255), -1);
				msg.x=int(x)
				msg.y=int(y)
				msg.radius=int(radius)
				#rospy.loginfo(detected)
        		if detected == False:
          			rospy.loginfo(" "+ msg.color+" ball detected ")
          			detected = True
		else:
			if detected == True:
				rospy.loginfo("Can't find the ball")
            	rospy.loginfo("Sending request to neighbours to find "+msg.color+" ball.")
            	rospy.loginfo(msg)
            	msg.heading="laptop"
            	pub.publish(msg)
            	detected = False
              

	

if __name__ == '__main__':
	try:
		combine()
		
	except rospy.ROSInterruptException: 
		pass

			
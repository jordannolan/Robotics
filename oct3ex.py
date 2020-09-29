#!/usr/bin/env python
from std_msgs.msg import Int64
import rospy
import math
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Pose
from time import sleep

pub_vel = rospy.publisher('/mobile_base/commands/velocity',Twist,queue_size=10)
pose = pose()
t = Twist()

def odomCb(data):
	global pose
	print('In odomCb')
	pose = data.pose.pose
	print('pose in odomCb: is' str(% pose))

def turnToTheta(theta):
	print('In turnToTHeata')

def moveDist(d, speed):
	print('In moveDist')
	
	#the position before we move
	p_start = pose.position
	
	dRelative = 0

	t = Twist()
	t.linear.x = speed

	r = rospy.rate(30)
	
	while dRealtive < d and not rospy.is_shutdown():
		dRealative = math.sqrt(math.pow(pose.position.x - p_start.x,2)+math.pow(pose.position.y - p_start.y,2))

	pub_vel.publish(t)
	r.sleep()

def turnRad(rad, speed):
	print('In turnRad')
	
	#the position before we move
	thetaStart = tf.transformations.euler_from_quaternion([pose.orientation.x,pose.orientation.y,pose.orentation.z,pose.orentation.w])[2]
	thetaRelative = 0

	print(thetaStart)
	
	t = Twist()
	t.linear.x = 0
	t.linear.z = speed
	
	r = rospy.rate(30)
	
	while thetaRelative < rad and not rospy.is_shutdown():
		tempRealative = tf.transformations.euler_from_quaternion([pose.orientation.x,pose.orientation.y,pose.orentation.z,pose.orentation.w])[2]

	thetaRelative = tempTheta - thetaStart
	pub_vel.publish(t)
	r.sleep()


def main():
	print("In main")
	rospy.init_node('move_on_path',anonymous=True)

	#Subscribers
	sub_odom = rospy.Subscriber('/odom',Odometry,odomCb)

	initSleep = rospy

	turnRad(0.785,0.785)

	rospy.spin()
	print("Exiting Normally")

if __name__ == '__main__':
	main()


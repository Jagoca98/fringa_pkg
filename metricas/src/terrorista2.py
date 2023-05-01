#!/usr/bin/env python3
import rospy

rospy.init_node('my_node', anonymous=True)

# print(rospy.has_param('my_param'))
my_param = rospy.get_param('my_node/my_param')
print("The value of my_param is:", my_param)
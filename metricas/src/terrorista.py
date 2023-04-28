#!/usr/bin/env python3
# license removed for brevity

import rospy
import subprocess
from std_msgs.msg import Bool
import rospy
from move_base_msgs.msg import MoveBaseActionGoal


cmd_find = ["rospack", "find", "metricas"]


class Terroristas():
    def __init__(self):
            self.end = False
            self.initialPose = MoveBaseActionGoal()
            self.initialPose.goal.target_pose.header.frame_id = 'map'
            self.initialPose.goal.target_pose.pose.position.x = 1
            self.initialPose.goal.target_pose.pose.position.y = -4
            self.initialPose.goal.target_pose.pose.position.z = 0
            self.initialPose.goal.target_pose.pose.orientation.x = 0
            self.initialPose.goal.target_pose.pose.orientation.y = 0
            self.initialPose.goal.target_pose.pose.orientation.z = 0
            self.initialPose.goal.target_pose.pose.orientation.w = 1
            self.listener()
            

    def callback(self, data):
        if data.data == True:
            rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
            pwd = subprocess.run(cmd_find, capture_output=True, text=True)
            path = str(pwd.stdout).split('\n')[0] + '/maps/map'
            # print(str(pwd.stdout.split('\n')[0]))
            # print(path)
            # cmd_save = ["rosrun", "map_server", "map_saver", "-f", str(path)]
            # subprocess.run(cmd_save, stdout = True)
            self.end = True

            
        
    def listener(self):

        # In ROS, nodes are uniquely named. If two nodes with the same
        # name are launched, the previous one is kicked off. The
        # anonymous=True flag means that rospy will choose a unique
        # name for our 'listener' node so that multiple listeners can
        # run simultaneously.
        rospy.init_node('carloYagus', anonymous=True)

        rospy.Subscriber("/the_end_of_explorations", Bool, self.callback)

        # spin() simply keeps python from exiting until this node is stopped
        # rospy.spin()

if __name__ == '__main__':
    
    pub = rospy.Publisher("/move_base/goal", MoveBaseActionGoal, queue_size=10)    
    carlosYagus = Terroristas()
    carlosYagus.listener()
    rate = rospy.Rate(1)
    
    while not rospy.is_shutdown():
        if carlosYagus.end:
            pub.publish(carlosYagus.initialPose)
        rate.sleep()
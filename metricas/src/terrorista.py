#!/usr/bin/env python3
# license removed for brevity

import rospy
import subprocess
from std_msgs.msg import Bool
import rospy
from move_base_msgs.msg import MoveBaseActionGoal
from metricas import EvalMap


cmd_find = ["rospack", "find", "metricas"]
# token = 'escenario1'

# print(rospy.has_param('metricas/world_name_tag'))
token = rospy.get_param('carlosYagus/world_name_tag', 'escenario1')
print(token)
pwd = subprocess.run(cmd_find, capture_output=True, text=True)
path_server = str(pwd.stdout).split('\n')[0] + '/maps/explored_maps/' + token
path_gt = str(pwd.stdout).split('\n')[0] + '/maps/gt_maps/' + token + '_gt.pgm'
save_path = str(pwd.stdout).split('\n')[0] + '/maps/differences/' + token + '_differences.jpg'
path = str(pwd.stdout).split('\n')[0] + '/maps/explored_maps/' + token + '.pgm'


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
            print(path_server)
            cmd_save = ["rosrun", "map_server", "map_saver", "-f", str(path_server)]
            subprocess.run(cmd_save, stdout = True)
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
            EvalMap.run(path_gt=path_gt, path=path)
            break
        rate.sleep()
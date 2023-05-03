#!/usr/bin/env python3
# license removed for brevity

import rospy
import subprocess
from std_msgs.msg import Bool
import rospy
from move_base_msgs.msg import MoveBaseActionGoal
from metricas import EvalMap
from metricas.msg import Errores


cmd_find = ["rospack", "find", "metricas"]
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
            self.errores = Errores()
            rospy.init_node('carloYagus', anonymous=True)
            rospy.Subscriber("/the_end_of_explorations", Bool, self.callback)
            self.pub = rospy.Publisher("/move_base/goal", MoveBaseActionGoal, queue_size=10)
            self.pub_error = rospy.Publisher("/errores", Errores, queue_size=10)
            
            

    def callback(self, data):
        
        rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
        print(path_server)
        cmd_save = ["rosrun", "map_server", "map_saver", "-f", str(path_server)]
        subprocess.run(cmd_save, stdout = True)
        self.pub.publish(carlosYagus.initialPose)
        errores = EvalMap.run(path_gt=path_gt, path=path)
        self.pub_error.publish(errores)        

if __name__ == '__main__':
    
    pub = rospy.Publisher("/move_base/goal", MoveBaseActionGoal, queue_size=10)

    carlosYagus = Terroristas()
    rospy.spin()

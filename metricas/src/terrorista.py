#!/usr/bin/env python3
# license removed for brevity

import rospy
import subprocess
from std_msgs.msg import Bool

cmd_find = ["rospack", "find", "metricas"]


def callback(data):
    if data.data == True:
        rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
        pwd = subprocess.run(cmd_find, capture_output=True, text=True)
        path = str(pwd.stdout).split('\n')[0] + '/maps/map'
        # print(str(pwd.stdout.split('\n')[0]))
        # print(path)
        cmd_save = ["rosrun", "map_server", "map_saver", "-f", str(path)]
        subprocess.run(cmd_save, stdout = True)
        
    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("/the_end_of_explorations", Bool, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
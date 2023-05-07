#!/usr/bin/env python3
# license removed for brevity

import rospy
from nav_msgs.msg import Odometry
from std_msgs.msg import Bool, Float64
from metricas.msg import Errores, Metricas
from time import time

trajectory = Float64()
exploration_time = Float64
trajectory.data = 0
tiempo_fin = time()
tiempo_init = time()
first_time = True
exploration_on = True
pub = rospy.Publisher("/metrics", Metricas, queue_size=10)

def callback_trajectory(msg):
    global trajectory, tiempo_init, tiempo_fin, first_time, exploration_on
    vel = abs(msg.twist.twist.linear.x)
    tiempo_init = tiempo_fin
    tiempo_fin = msg.header.stamp.to_sec()
    delta_tiempo = tiempo_fin - tiempo_init
    if not first_time and exploration_on:
        trajectory.data += vel * delta_tiempo
    first_time = False
    # print(exploration_on, trajectory)


def callback_end(msg):
    global exploration_on, trajectory, exploration_time
    exploration_time = msg.data
    exploration_on = False

def callback_errores(msg):
    global trajectory, pub, exploration_time
    metricas = Metricas()
    metricas.distance = trajectory.data
    metricas.exploration_time = exploration_time
    metricas.errors = msg
    pub.publish(metricas)


rospy.init_node('trajectory', anonymous=True)
rospy.Subscriber("/odom", Odometry, callback_trajectory)
rospy.Subscriber("/the_end_of_explorations", Float64, callback_end)
rospy.Subscriber("/errores", Errores, callback_errores)
rospy.spin()


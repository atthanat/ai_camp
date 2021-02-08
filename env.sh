#!/bin/bash

export ROS_IP=10.204.226.85
export ROS_MASTER_URI=http://10.204.226.83:11311

source /opt/ros/kinetic/setup.bash
source ~/catkin_ws/devel/setup.bash

exec "$@"


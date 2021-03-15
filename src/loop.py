#!/usr/bin/python
import time
import rospy
from api import Turtlebot


def tester():

    robot = Turtlebot()

    print "bringup finished"
    rate = rospy.Rate(200)
    state = 0
    while not rospy.is_shutdown():
    
        ir_left = robot.get_sensor(0) #get value from 1st sensor
        ir_right = robot.get_sensor(1) #get value from 2nd sensor
        if ir_right > 50 and ir_left > 50 :
            state = 0
        elif ir_right > 50 and ir_left < 50 :
            state = 1
        elif ir_left > 50 and ir_right < 50 :
            state = 2
        elif ir_left < 50 and ir_right < 50 :
            if state == 1 or state == 3 :
                state = 3
            if state == 2 or state == 4 :
                state = 4
        
        if state == 0 :
            robot.move_robot(20,20)
        elif state == 1 :
            robot.move_robot(20,15)
        elif state == 2 :
            robot.move_robot(15,20)
        elif state == 3 :
            robot.move_robot(20,10)
        elif state == 4 :
            robot.move_robot(10,20)
        
        print "Infrared sensor left:" + str(ir_left) + " Infrared sensor right:" + str(ir_right)

        rate.sleep()



    robot.stop()
    print "stop"
    print "current velocity is "
    print robot.get_vel()

if __name__ == '__main__':
    try:
        tester()
    except rospy.ROSInterruptException:
        pass
